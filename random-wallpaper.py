# -*- coding: utf-8 -*-
from time import sleep
from sys import path as systemPath
import click
import os

#@click.command()
#@click.option()

sleep_time = int(0)

def set_wallpaper():
    """ Set the wallpaper """
    a = 1
    # Check if the system has feh or hsetroot on it's path
    #path = os.system('echo $PATH')
    #if ('feh', 'hsetroot') not in (systemPath):
    #	print("You doesn't appear to have feh or hsetroot installed (on your path). Please, install one of those to continue.")
    #	exit(1)
    if a == 1:
        # Get the list of files to use
        wpp_list = list(os.listdir())
        # Remove the script name so it doesn't get among the filenames
        wpp_list.remove(os.path.basename(__file__))
        # Get the extension of the files to know if it is a image or not
        for file in wpp_list:
            file = 0
            print(wpp_list)
            print(file)
            filename, file_extension = os.path.splitext(wpp_list[file])
            if file_extension not in ('.jpg', '.jpeg', '.png', ".tif", ".tiff"):
                wpp_list.remove(file)
                print(wpp_list)
                print(file)
                sleep(30)
                exit(1)
            else:
                while True:
                    for file in wpp_list:
                        # Change the '--bg-fill' part to set your bg according to feh's man page
                        os.system('feh --bg-fill ' + file)
                        sleep(1)
                        print(wpp_list)
if __name__ == "__main__":
	set_wallpaper()


