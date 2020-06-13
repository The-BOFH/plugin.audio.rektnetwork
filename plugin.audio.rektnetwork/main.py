import sys
import xbmcgui
import xbmcplugin
# We include the things we need.


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')
# Puts This Addon in the Audio section of the Kodi Addons.


#--Based_Skid here
#We Need to Add in code that will allow us to define the station list from a url, say a txt file on the git for example
#If this addon ever were to be made "official" this txt file should be hosted on the anonops site example: radio.anonops.com/stationlist.txt
#Same with the images. example:radio.anonops.com/imgs. but for now they are on the git 
#-----

url = 'https://rekt.network/stream/rekt.ogg' # Rather straightforward, here.
li = xbmcgui.ListItem('Rekt', iconImage='https://rekt.network/static/img/favicon.png')  #Name, then the icon. I'm pleasantly surprised it accepts URLs!
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)



url = 'https://rekt.network/stream/nightride.ogg'
li = xbmcgui.ListItem('Nightride', iconImage='https://rekt.network/static/img/favicon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://rekt.network/stream/rektory.ogg'
li = xbmcgui.ListItem('Rektory', iconImage='https://rekt.network/static/img/favicon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://rekt.network/stream/rektify.ogg'
li = xbmcgui.ListItem('Rektify', iconImage='https://rekt.network/static/img/favicon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


xbmcplugin.endOfDirectory(addon_handle) # Here we tell the system that this is the end for now.
