#!/bin/bash/env python

import sys

def add(a,b):
	sum = a + b
	print(sum)

a = int( sys.argv[1] )
b = int( sys.argv[2] )


try:
	a = int( sys.argv[1] )
	b = int( sys.argv[2] )
except IndexError:
	print("ERROR! 2 Numerical value")
	a = int(input("Please insert the first value: "))
	b = int(input("Please insert the second value: "))
	add(a,b)
	raise(SystemExit)


add(a,b)


