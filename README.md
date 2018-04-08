# clashofclans - A Python Async wrapper made for the Clash of Clans API.

**Setting 'em up!**

To install the package, open a Command Prompt and run this:

```pip install git+https://github.com/bananaboy21/clashofclans```

Note: Make sure this is run in the PC that is using the clashofclans wrapper. 


**Updating it later...**
Updates will be announced in the support server (read below for the link). If you need to update it, open the Command Prompt and run this:

```pip install -U git+https://github.com/bananaboy21/clashofclans```


**Requirements to use clashofclans:**
-Python, v3.5 or higher.
-aiohttp, v2.0.0 or higher.
-A brain.


**An example of usage:**
```py
import clashofclans
client = clashofclans.Client("token, token, BLAH BLAH BLAH")
profile = await client.get_profile('#PP98PGGJJ')
print(profile.name)
```
This will print my profile's name, banana boy. 
In the above example, printing `dir(profile)` will get a list of all the possible attributes to `profile`.


**Support/Feedback**
-You can join our support server: https://discord.gg/3Nxb7yZ


**Contributing**
I suck at coding, so if you see any rough spots, or anywhere that you can't scroll past without it catching your eye, feel free to make a pull request. If you joined my support server, you will also get a shiny, clean "Contributor" role!


