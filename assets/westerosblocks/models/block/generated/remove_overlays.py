import os
import re

RE_PATTERN = r'"parent": "([a-z:/_]*)_overlay"'
RE_SUB = r'"parent": "\1"'

for dir, _, _ in os.walk('.'):
  if dir != '.':
    for modelname in os.listdir(dir):
      fname = dir + '/' + modelname
      with open(fname, 'r') as f:
        str = f.read()
      str1 = re.sub(RE_PATTERN, RE_SUB, str)
      with open(fname, 'w') as f:
        f.write(str1)