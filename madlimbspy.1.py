#!/usr/bin/env python3

"""
File: madlibs.py
Name:
A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
   name = input("enter name")
   place = input("enter a place")
   vehicle = input("enter a vehicle")
   verb = input("enter a verb")
   adverb = input("enter an adverb")
   print(name,"went to",place,"with his",adverb,vehicle,"while",verb)
   
if __name__ == "__main__":
   main()