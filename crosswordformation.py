#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:00:44 2017

@author: goodwin
"""
import itertools


def crosswordFormation(words):
    count = 0
    perms = itertools.permutations(words)
    for perm in perms:
        north = perm[0]
        east = perm[1]
        west = perm[2]
        south = perm[3]
        for i in range(2, len(north)):
            for j in range(len(east)-2):
                if north[i] == east[j]:
                    for k in range(i-1):
                        for l in range(len(west)-2):
                            if north[k] == west[l]:
                                for m in range(l+2, len(west)):
                                    if j+m-l < len(east):
                                        for n in range(len(south)-(i-k)):
                                            if n+i-k < len(south):
                                                if west[m] == south[n]:
                                                    if south[n+i-k] == east[j+m-l]:
                                                        count+=1
                                            else:
                                                break
                                    else:
                                        break
    return count