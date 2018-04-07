import setuptools

description = "clashofclans - A Python Async wrapper made for the Clash of Clans API"
long_description = open("README.md").read()
version="1.0.0"

packages = ['clashofclans']

setuptools.setup(
    name='clashofclans',
    version=version,
    description=description,
    long_description=long_description,
    url='https://github.com/bananaboy21/clashofclans',
    author='dat banana boi',
    author_email='kang.eric.hi@gmail.com',
    license='MIT',
    packages=packages,
    include_package_data=True,
    install_requires=['aiohttp>=2.0.0']
)
