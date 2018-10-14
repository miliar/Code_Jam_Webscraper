#!/usr/bin/env python
import numpy as np


def getField(field):
    # print field
    # print "#################################"
    nRows = len(field)
    nCols = len(field[0])
    if(nRows*nCols == 1):
        if(field[0][0] == '?'):
            return (field, False)
        else:
            return (field, True)
    if(np.array_equal(field, np.array([['?']*nCols]*nRows))):
        return (field, False)
    if(nRows > nCols):
        split = int(np.ceil(nRows/2.0))
        field1, bool1 = getField(field[:split, :])
        field2, bool2 = getField(field[split:, :])
        # print field
        # print "---------------------------------------"
        # print field1
        # print "---------------------------------------"
        # print field2
        # print "---------------------------------------"
        # print "#######################################"
        if(bool1 and bool2):
            return (np.concatenate((field1, field2)), True)
        if((not bool1) and (not bool2)):
            return (np.concatenate((field1, field2)), False)
        if(not bool1):
            temp = np.array([field2[0][:]]*len(field1))
            return (np.concatenate((temp, field2)), True)
        temp = np.array([field1[-1][:]]*len(field2))
        return (np.concatenate((field1, temp)), True)
    else:
        split = int(np.ceil(nCols/2.0))
        field1, bool1 = getField(field[:, :split])
        field2, bool2 = getField(field[:, split:])
        # print field
        # print "---------------------------------------"
        # print field1
        # print "---------------------------------------"
        # print field2
        # print "---------------------------------------"
        # print "#######################################"
        if(bool1 and bool2):
            return (np.concatenate((field1, field2), axis=1), True)
        if((not bool1) and (not bool2)):
            return (np.concatenate((field1, field2), axis=1), False)
        if(not bool1):
            temp = np.repeat(field2[:, :1], len(field1[0]), axis=1)
            # temp = np.array([field2[0][:]]*len(field1))
            return (np.concatenate((temp, field2), axis=1), True)
        temp = np.array([field1[-1][:]]*len(field2))
        temp = np.repeat(field1[:, -1:], len(field2[0]), axis=1)
        return (np.concatenate((field1, temp), axis=1), True)


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    r, c = map(int, inFile.readline().split(' '))
    field = []
    for i in range(r):
        temp = inFile.readline().strip()
        x = []
        for letter in temp:
            x.append(letter)
        field.append(x)
    field = np.array(field)
    ansField, ansBool = getField(field)
    outFile.write("Case #{}:\n".format(test))
    for row in ansField:
        for letter in row:
            outFile.write(letter)
        outFile.write("\n")
    # emptyRows = set()
    # emptyCols = set()
    # for i in range(r):
    #     temp_set = set(field[i])
    #     if('?' in temp_set and len(temp_set) == 1):
    #         emptyRows.add(i)
    # for j in range(c):
    #     temp_set = set()
    #     for i in range(r):
    #         temp_set.add(field[i][j])
    #     if('?' in temp_set and len(temp_set) == 1):
    #         emptyCols.add(i)
    #
    # for i, row in enumerate(field):
    #     if (i in emptyRows):
    #         continue
    #     for j, letter in enumerate(row):
    #         if(letter == '?' and j not in emptyCols):
    #             up = (min(0, i-1), j)
    #             down = (max(len(field) - 1, i+1), j)
    #             left = (i, min(0, j-1))
    #             right = (i, max(len(row) - 1, j+1))
