import time
import subprocess
import sys

import os

def set_name(name):
    name = now + "_" + name
    return name

now = time.strftime("%Y%m%d")

name = set_name(sys.argv[1])
path = os.getcwd()
path = path +'\\' + name

result = subprocess.run(['mkdir', name], stdout=subprocess.PIPE,shell=True)
result.stdout

result = subprocess.run(['mkdir', path+"\\" + 'Code', path+"\\" + 'Analysis', path+"\\" + 'Presentation'], stdout=subprocess.PIPE,shell=True)
result.stdout

