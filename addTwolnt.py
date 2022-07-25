#!/bin/bash/env python

import sys

def add(a,b):
sum = a + b
print(sum)

try:
a =int( sys.argv[1] )
b =int( sys.argv[2] )
except IndexError:
print("Add only 2 Arguments")
raise(SystemExit)


add(a,b)


