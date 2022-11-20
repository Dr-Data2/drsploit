import os
import sys
import time
import json
import errno
import base64
import ctypes
import ftplib
import struct
import socket
import signal
import logging
import functools
import threading
import subprocess
import collections
import logging.handlers
from .banners import *
import ast
#import rich
#from rich.table import Table
#from rich.console import Console  
#console = Console()
g='\033[1;32m'
wr = "\033[0m"
if sys.version_info[0] < 3:
    from urllib import urlretrieve
    from urllib2 import urlopen, urlparse
    import StringIO
else:
    from urllib import parse as urlparse
    from urllib.request import urlopen, urlretrieve
    from io import StringIO

# modules
try:
    from util import *
    from loader import *
    from security import *
except ImportError:
    pass



class command():
  
    def pwd(*args):
            """
            Show name of present working directory

            """
            print(f"[{g}+{wr}] exec: pwd")
            print(f"\n[{g}+{wr}] "+os.getcwd()+"\n")

    #@config(platforms=['win32','linux','linux2','darwin'], command=True, usage='cd <path>')
    def cd(xx ,path='.'):
        """
            Change current working directory

            `Optional`
            :param str path:  target directory (default: current directory)

            """
        
        new_path = xx.strip("cd ")
        if os.path.exists(new_path):
            os.chdir(new_path)
            print(f"[{g}+{wr}] exec: {xx}")
            print(f"\n[{g}+{wr}] "+os.getcwd()+"\n")
                #continue
             
        else:
            print("{}: No such file or directory".format(path))
            #os.chdir(path)
            #return os.getcwd()
       


    def ls(path='.'):
        """
        List the contents of a directory

        `Optional`
        :param str path:  target directory

        """
        output = []
        if os.path.isdir(path):
            print(f"[{g}+{wr}] exec: ls\n")
            for i in range(6):
                for line in os.listdir(path):
                    if len('\n'.join(output + [line])) < 2048:
                        output.append(line)
                    else:
                        break
                
                return '   '.join(output)
                
                
            
        else:

            return "Error: path not found"
    def use(xx):
        """
            Change current working directory

            `Optional`
            :param str path:  target directory (default: current directory)

            """
        
        new_path = xx.strip("use ")
        
        id  = "id"
        option = "option"
        path = "path"

        try:
            file = open("datasheet.txt","r+")
            d = file.read()
            r = ast.literal_eval(d)

            dict2={id:path}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open("datasheet.txt","w")
            w = file.write(str(r))

        except:
            file = open("datasheet.txt","w")
            pp = str({'id':'path'})
            file.write(pp)
            file.close()


        files = open('datasheet.txt','r')
        dd=files.read()
        rr= ast.literal_eval(d)
        files.close()
        print(rr.keys())
        print(rr.values())
        print(rr[id])
        print(f"Fk U : {new_path}")



    def cat(path):
        """
        Display file contents

        `Required`
        :param str path:  target filename

        """
        
        output = []
        if not os.path.isfile(path):
            return "Error: file not found"
        for line in open(path, 'rb').read().splitlines():
            if len(line) and not line.isspace():
                if len('\n'.join(output + [line])) < 48000:
                    output.append(line)
                else:
                    break
        return '\n'.join(output)
   
    def wget(self, url, filename=None):
        """
        Download file from URL

        `Required`
        :param str url:         target URL to download ('http://...')

        `Optional`
        :param str filename:    name of the file to save the file as

        """
        if sys.version_info[0] < 3:
            from urllib import urlretrieve
            from urllib2 import urlopen, urlparse
            import StringIO
        else:
            from urllib import parse as urlparse
            from urllib.request import urlopen, urlretrieve
        if url.startswith('http'):
            try:
                path, _ = urlretrieve(url, filename) if filename else urlretrieve(url)
                return path
            except Exception as e:
                log("{} error: {}".format(self.wget.__name__, str(e)))
        else:
            return "Invalid target URL - must begin with 'http'"
    def run(self):
        try:
             # run command as module if module exists.
                            # otherwise, run as shell command in subprocess
            command = self._get_command(cmd)
            if command:
                result = command(action) if action else command()
            else:
                result, reserr = subprocess.Popen(task['task'].encode(), 0, None, subprocess.PIPE, subprocess.PIPE, subprocess.PIPE, shell=True).communicate()
                if result == None:
                    result = reserr

                            # format result
            if result != None:
                if type(result) in (list, tuple):
                    result = '\n'.join(result)
                elif type(result) == bytes:
                    result = str(result.decode())
                else:
                    result = str(result)
        except Exception as e:
            result = "{} error: {}".format(self.run.__name__, str(e)).encode()
            
            log(result)
def runn():
    
    sem()
    O2()

    while True:

        x = input(f"{wr}msi>")
        xs = x.split(" ")
        try:
            if xs[0] == "ls":
                print(command.ls())
            elif x == "pwd":
                command.pwd()
            elif x.startswith("cd"):
                command.cd(x)
            elif x.startswith("use"):
                command.use(x[1])
            elif x == "cat":
                command.cat(x)
            elif x == "":
                continue
            elif x == "banner":
                sem()
                O2()
            elif x == "dir":
                print(subprocess.run(x,shell=True))
            else :
                print("[-] command is Error ")
            
        except:
            print("[-] command not found ")