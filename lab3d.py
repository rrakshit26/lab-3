#!/usr/bin/env python3

'''Lab 3d script - system commands'''
# Author ID: rrakshit

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0].decode('utf-8').strip()
    return output

if __name__ == '__main__':
    print(free_space())
