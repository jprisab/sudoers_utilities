#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
reportunusedsudoersalias.py
Script to analyze and report non used Defined aliases in a sudoers file for linux systems
set
- the folder that contains the sudoer file to analyze (or several files if you want)
"""


import os
from pysudoers import Sudoers

FOLDERNAME="C:\javier\\sudoers\IAAS-1005"
FILENAMESTARTCOND=""


if __name__ == '__main__':

    for subdir, dirs, files in os.walk(FOLDERNAME):

        for filename in files:

            if filename.startswith(FILENAMESTARTCOND):
                completefilename = subdir + "\\" + filename

                sobj = Sudoers(path=completefilename)
                lista_cmd_aliases = sobj.cmnd_aliases
                lista_hst_aliases = sobj.host_aliases
                lista_usr_aliases = sobj.user_aliases

                print("--------------------------------------")
                print("NEVER USED USER ALIAS In The File: " + completefilename)

                for usr_alias in sobj.user_aliases:
                    # print (cmd_alias)
                    used = 'false'
                    for rule in sobj.rules:

                        for user in rule["users"]:
                            usertolist = user
                            if usertolist == usr_alias:
                                used = 'true'
                                break



                    if used == 'false':
                        print(usr_alias)


                print("--------------------------------------")
                print("NEVER USED COMMAND ALIAS In The File: " + completefilename)

                for cmd_alias in sobj.cmnd_aliases:
                   # print (cmd_alias)
                    used = 'false'
                    for rule in sobj.rules:

                        for comando in rule["commands"]:
                            comandotolist = comando["command"]
                            if comandotolist == cmd_alias:
                                used = 'true'
                                break
                    if used=='false':
                        print(cmd_alias )

                print("--------------------------------------")
                print("NEVER USED HOST ALIAS In The File: " + completefilename)
                for host_alias in sobj.host_aliases:
                    # print (host_alias)
                    used = 'false'
                    for rule in sobj.rules:

                        for host in rule["hosts"]:
                            hosttolist = host
                            if hosttolist == host_alias:
                                used = 'true'
                                break

                    if used == 'false':
                        print(host_alias)
