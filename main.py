#!/usr/bin/python

import sys

# Function to check if one to one mapping exist from string s1 to string s2
def checkOneToOneMapping(s1, s2):

    s1_length = len(s1)

    # If two strings have different lengths then one to one mapping does not exist
    if s1_length != len(s2):
        return False

    # Dictionary to store character mapping from String1 to String2
    character_dict = {}

    for i in range(s1_length):
        # If character in string 1 is present in dictionary then
        # check if current string 2 character is same as that of the
        # value associated with string 1 character in dictionary
        if s1[i] in character_dict:
            if character_dict[s1[i]] != s2[i]:
                return False
        # Assign string 2 character as value of the string 1 character in dictionary
        else:
            character_dict[s1[i]] = s2[i]
    return True


result = checkOneToOneMapping(sys.argv[1], sys.argv[2])

if result:
    print("true")
else:
    print("false")
