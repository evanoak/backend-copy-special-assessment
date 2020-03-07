#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "Evan Ochs"


# +++your code here+++
def get_special_paths(dir):
    abspath = os.path.abspath(dir)
    dir_list = os.listdir(dir)
    special_list = []
    for item in dir_list:
        match = re.search(r'[\w]*\_{2}\.[\w]*', item)
        if match:
            abspath = abspath + '/' + str(match.group())
            special_list.append(abspath)
            abspath = os.path.abspath(dir)
    return special_list
            

def copy_to(paths, dir):
    for file in paths:
        shutil.copy(file, dir)

def zip_to(paths, zippath): 
    for file in paths:
        try:
            subprocess.call(["zip", "-j", zippath, file])
        except IOError:
            print('Error')
# Write functions and modify main() to call them

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='directory to search for files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    to_dir = args.todir
    to_zip = args.tozip
    from_dir = args.fromdir

    if os.path.exists(from_dir):
        paths = get_special_paths(from_dir)
    else:
        print('Directory doesn\'t exist')

    if to_dir:
        if os.path.exists(to_dir):
            copy_to(paths, to_dir)
        else:
            os.makedirs(to_dir)
            copy_to(paths, to_dir)

    if to_zip:
        output = 'zip -j' + to_zip
        for file in paths:
            output += ' ' + file
        print("Command I'm going to do:")
        print(output)
        zip_to(paths, to_zip)
        

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
