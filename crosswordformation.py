#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:00:44 2017

@author: goodwin
"""

def crosswordFormation(words):
    count = 0
    for north in words:
        words1 = words[:]
        words1.remove(north)
        for east in words1:
            words2 = words1[:]
            words2.remove(east)
            for south in words2:
                words3 = words2[:]
                words3.remove(south)
                for west in words3:
                    for i in range(2, len(north)):
                        for j in range(len(east)-2):
                            if north[i] == east[j]:
                                for k in range(i-1):
                                    for l in range(len(west)-2):
                                        if north[k] == west[l]:
                                            for m in range(l+2, len(west)):
                                                for n in range(len(south)-(i-k)):
                                                    try:
                                                        if (west[m] == south[n] and
                                                            south[n+i-k] == east[j+m-l]):
                                                                count+=1
                                                    except IndexError:
                                                        pass
    return count