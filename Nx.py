import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from bboy import xsxsxlll
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    xsxsxlll()
elif bit == '32bit':
    from f32 import xsxsxlll
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    xsxsxlll()
 
