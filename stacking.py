# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 02:13:30 2022

@author: Nalyne
"""
import numpy as np
#import math

AA = np.array([12,12,11,10],dtype=int)
AB = np.array([12,15,1,7],dtype=int)
BA = np.array([0,0,0,0],dtype=int)
BB = np.array([14,8,13,10],dtype=int)

OO = np.array([AA,AB,BA,BB])
v999 = " │ "
v0 = "   "
v1 = "┃ "
v2 = " ┃ "
v3 = " ┃"
l1 = "┏━━━┯━━━┳━━━┯━━━┓"
l3 = "┠─ ─┼─ ─╂─ ─┼─ ─┨"
l5 = "┣━━━┿━━━╋━━━┿━━━┫"
l7 = "┠─ ─┼─ ─╂─ ─┼─ ─┨"
l9 = "┗━━━┷━━━┻━━━┷━━━┛"
lA = "┏━━━┯━━━┓"
lC = "┠─ ─┼─ ─┨"
lE = "┗━━━┷━━━┛"

def hexcnv(val):
    if val < 0: return("error")
    elif val < 10: return(str(val))
    elif val == 10: return("A")
    elif val == 11: return("B")
    elif val == 12: return("C")
    elif val == 13: return("D")
    elif val == 14: return("E")
    elif val == 15: return("F")
    else: return("error") 

def tablePrint():
    l2 = v1 + hexcnv(OO[0][0]) + v0 + hexcnv(OO[0][1]) + v2 + hexcnv(OO[1][0]) + v0 + hexcnv(OO[1][1]) + v3
    l4 = v1 + hexcnv(OO[0][2]) + v0 + hexcnv(OO[0][3]) + v2 + hexcnv(OO[1][2]) + v0 + hexcnv(OO[1][3]) + v3
    l6 = v1 + hexcnv(OO[2][0]) + v0 + hexcnv(OO[2][1]) + v2 + hexcnv(OO[3][0]) + v0 + hexcnv(OO[3][1]) + v3
    l8 = v1 + hexcnv(OO[2][2]) + v0 + hexcnv(OO[2][3]) + v2 + hexcnv(OO[3][2]) + v0 + hexcnv(OO[3][3]) + v3
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)

def layerPrint(Layer):
    LayerT = np.array(["","","",""],dtype=str)
    for i in range(4):
        if (Layer[i] == 0): LayerT[i] = " "
        else: LayerT[i] = "■"
    LayerT
    lB = v1 + LayerT[0] + v0 + LayerT[1] + v3
    lD = v1 + LayerT[2] + v0 + LayerT[3] + v3
    print(lA)
    print(lB)
    print(lC)
    print(lD)
    print(lE)
    
def layerRead(ix, h, prnt = False):
    Layer = OO[ix] - h
    for i in range(4):
        if Layer[i] < 1: Layer[i] = 0
        else: Layer[i] = 1
    if prnt: layerPrint(Layer)
    return(Layer)
    
def Inint(prompt, maxv, minv = 0):
    flag = True
    while flag:
        Temp = input(prompt)
        if (not("." in Temp)) and Temp.isnumeric:
            Vt = int(Temp)
            if (Vt > minv-1) and (Vt < maxv+1):
                flag = False
                break
            else:
                print("Out of Range "+str(minv)+" . . "+str(maxv))
        else:
            print("Invalid Input.")
    return(Vt)
    
def LASelect():
    print("Layer add selection")
    val = np.array([0,0,0,0], dtype=int)
    print("Which block do you wish to be added?")
    print("┏━━━┳━━━┓")
    print("┃ 0 ┃ 1 ┃")
    print("┣━━━╋━━━┫")
    print("┃ 2 ┃ 3 ┃")
    print("┗━━━┻━━━┛")
    ix = Inint("Please enter integer between 0 and 3. . . ", 3)
    print("What shape do you wish to add?")
    print("┏━━━┳━━━┓")
    print("┃ 1 ┃ 2 ┃")
    print("┣━━━╋━━━┫")
    print("┃ 4 ┃ 8 ┃")
    print("┗━━━┻━━━┛")
    flag = True
    while flag:
        flag = False
        valhex = Inint("Please enter integer between 0 and 15. . . ", 15)
        Vt = valhex
        for i in range(4):
            val[i] = np.mod(Vt , 2)
            Vt = np.divmod(Vt,2)[0]
        layerPrint(val)
        print("Is this shape correct?")
        Temp = input("(Y/N) Default answer is 'Y'. . . ")
        if ("n" in Temp) or ("N" in Temp): flag = True
        else: break
    print("Current table:")
    layerAdd(ix, val)

def layerAdd(ix, val, prnt = True):
    OO[ix] += val
    if prnt: tablePrint()

def layerTranslate(fromIx, toIx, fromH, prnt = False):
    Layer = layerRead(fromIx, fromH)
    layerAdd(toIx, Layer)
    layerAdd(fromIx, -1 * Layer)
    if prnt: tablePrint()

def LayerRotate(ix, h, r, prnt = False):
    CC = layerRead(OO[ix], h)
    DD = np.array([0,0,0,0])
    for i in range(4):
        j = np.mod(i + r)
        DD[j] = CC[i]
    OO[ix] = OO[ix] - CC + DD
    if prnt: tablePrint()
    
tablePrint()
layerRead(0,1,True)
LASelect()