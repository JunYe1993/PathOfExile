#!/bin/python3
import sys, re

if __name__ == "__main__":
    with open(sys.argv[1], "r") as html:
        print(html.read())