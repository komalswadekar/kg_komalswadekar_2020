#!/usr/bin/python

import sys

def checkOneToOneMapping(s1, s2):
    print("String 1 is : ", s1)
    print("String 2 is : ", s2)

    s1_length = len(s1)

    # If two strings have different lengths then one to one mapping does not exist
    if s1_length != len(s2):
        return False
        

print(checkOneToOneMapping(sys.argv[1], sys.argv[2]))
