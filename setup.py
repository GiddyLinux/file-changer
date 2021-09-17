import shutil
import os
import sys
import stat
import time

py = "bfm.py"

bin = "/bin"

os.chmod("bfm.py", stat.S_IRWXO)

print("Made file executale")
print()
print("Preparing to move")

shutil.move(py, bin)

print()
print("Moved")
print()
time.sleep(2)
print("Completed!")
print()
print()
print()
print()
print("Setup finished!")
print()
print("You can run sudo bfm.py from any Directory")
print("To run it")
