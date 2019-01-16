#author: Thien P.
#list of functions that is useful to me
import os

#function to convert var multiple new line into a list
#e.g. lines = os.popen('ls -a |sort'); list=vartolist(lines); print list
def vartolist(lines):
  lines = lines.readlines()
  lines[:] = [line.rstrip('\n') for line in lines]
  return lines

