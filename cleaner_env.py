import os
import datetime
import platform
import sys


message = """
Environment variables not found. Emergency stop!

Please set variables before run this program.

Windows:
    set age=20
    set folder='C:\dir\subgir','H:\dir'

Gitlab 
"""

if "folder" in os.environ:
    pass

else:
    print(message)
    sys.exit(0)

if "age" in os.environ:
    pass

else:
    print(message)
    sys.exit(0)

if platform.system() == 'Windows':

    cleanpath = os.environ.get('folder').split(",")
    cleanage = os.environ.get('age')
    today = datetime.datetime.today()
    clean_age = -3600.0 * 24 * int(cleanage)

    for path in cleanpath:
        pathpart = path.split("\\")
        truepath = []

        for part in pathpart:
            truepath.append(part.replace(r"'",r""))

        winpath = str('\\'.join(truepath))

        if os.path.isdir(winpath):
            os.chdir(winpath)

            for root, directories, files in os.walk(winpath, topdown=False):

                for name in files:
                    t = os.stat(os.path.join(root, name))[8]  # st_mtime
                    filetime = float(t) - today.timestamp()

                    if filetime <= clean_age:
                        print("Old - ", os.path.join(root, name))

                        try:
                            os.remove(os.path.join(root, name))

                        except PermissionError:
                            print("Make sure that you have access to specified path:", os.path.join(root, name))
                            continue

                        except FileNotFoundError:
                            print("Sorry, file does not exist:", os.path.join(root, name))
                            continue

                    else:
                        print("Less - ", os.path.join(root, name))

        else:
            print("The path is not exist:", winpath)

    sys.exit(0)

else:
    print('We need linux version.')
    sys.exit(1)
