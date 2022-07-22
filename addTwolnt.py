#!/bin/bash/env python

import sys

def add(a,b):
sum = a + b
print(sum)


a =int( sys.argv[1] )
b =int( sys.argv[2] )

add(a,b)


