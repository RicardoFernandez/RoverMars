#!C:\Users\ricki\PycharmProjects\RoverMars\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rover==1.0.5','console_scripts','rover'
__requires__ = 'rover==1.0.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rover==1.0.5', 'console_scripts', 'rover')()
    )
