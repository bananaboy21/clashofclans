import aiohttp
from box import Box
import urllib.parse


class CocError(Exception):
    '''
    The exception raised when the Clash of Clans API returns a status code
    other than 200 (success). You will have to handle this error yourself.
    '''
    pass


class NotInWar(CocError):
    '''
    The exception raised when a request is made with get_current_war
    but the clan was not currently in a war.

    You will have to handle this error yourself.
    '''
    pass



class Client:
    '''
    An object that represents the main Client of the clashofclans wrapper.
    Through this object, you can request from the endpoints here.
    '''

    def __init__(self, token, session=None):
        '''
        Constructs the Client used for requests. 

        ---Params---
        token (str): The API key received from the Clash of Clans API website.
        session (Optional, ClientSession): A ClientSession for this Client to use when making requests.
        Defaults to an aiohttp.ClientSession().
        '''
        self.token = "Bearer {}".format(token)
        self.session = aiohttp.ClientSession() if session is None else session
        self.headers = {'Authorization': self.token}
        self.baseurl = "https://api.clashofclans.com/v1/"


    async def _get(self, endpoint, query):
        '''
        This function requests to the API and returns the content that responds from it.
        It is called in each of the endpoints.

        You should never call this function directly. Instead, use a specified endpoint.
        '''
        query = urllib.parse.quote(str(query))
        async with self.session.get("{}{}{}".format(self.baseurl, endpoint, query), headers=self.headers) as resp:
            if resp.status != 200:
                errors = {
                    400: "Client provided incorrect parameters for the request.",
                    403: "Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.",
                    404: "Resource was not found.",
                    429: "Request was throttled, because amount of requests was above the threshold defined for the used API token.",
                    500: "Unknown error happened when handling the request.",
                    503: "Service is temprorarily unavailable because of maintenance."
                }
                raise CocError("An error occurred with Clash of Clans API. Error {}: {}".format(resp.status, errors[resp.status]))
            resp = await resp.json()
            return Box(resp)


    async def get_profile(self, query):
        '''
        Gets a COC profile of a player by the player tag.

        ---Params---
        query (str): The player's profile tag.
        Note that removing the '#' is optional, this wrapper does it for you.

        This requests to the /players/{playerTag} endpoint of the API.
        '''
        return await self._get("players/%23", query.strip("#"))


    async def get_clan(self, query):
        '''
        Gets information for a COC clan by the clan tag.

        ---Params---
        query (str): The clans's clan tag.
        Note that removing the '#' is optional, this wrapper does it for you.

        This requests to the /clans/{clanTag} endpoint of the API.
        '''
        return await self._get("clans/%23", query.strip("#"))


    async def get_clan_from_profile(self, query):
        '''
        A shortcut used to get information for a COC clan
        through a player's tag. This will return information 
        in the clan that they are currently in.

        ---Params---
        query (str): The players's player tag.
        Note that removing the '#' is optional, this wrapper does it for you. 

        This requests to:
        1) The /players/{playerTag} endpoint for the clan tag.
        2) The /clans/{clanTag} endpoint for clan information.
        '''
        profile = await self._get("players/%23", query.strip("#"))
        clantag = profile.clan.tag
        return await self._get("clans/%23", clantag.strip("#"))


    async def get_current_war(self, query):
        '''
        Gets information for a clan's current war.

        ---Params---
        query (str): The clans's clan tag.
        Note that removing the '#' is optional, this wrapper does it for you.

        This requests to the /clans/{clanTag}/currentwar endpoint of the API.
        '''
        data = await self._get("clans/%23", "{}{}".format(query.strip("#"), "/currentwar"))
        try:
            data.teamSize
        except AttributeError:
            raise NotInWar("The clan is currently not in a war.")
        return data


    async def get_clan_members(self, query):
        '''
        Gets a list of members in a COC clan, from the clan tag.

        ---Params---
        query (str): The clans's clan tag.
        Note that removing the '#' is optional, this wrapper does it for you.

        This requests to the /clans/{clanTag}/members endpoint of the API.
        '''
        return await self._get("clans/%23", "{}{}".format(query.strip("#"), "/members"))
        

    
