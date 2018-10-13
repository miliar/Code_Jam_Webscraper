# -*- coding: utf-8 -*-
"""
Created on Sat May  3 23:27:15 2014

@author: poonna
"""

test = [ 'aabc', 'abbc', 'abcc' ]

def collect(data, pos):
    n = len(data)
    lst = []
    for i in range(n):
        if pos[i] < len(data[i]):
            lst.append(data[i][pos[i]])
        else:
            lst.append(None)
    return lst

def count_char(c, data, pos):
    n = len(data)
    count = 0
    for i in range(n):
        if pos[i] < len(data[i]) and data[i][pos[i]] == c:
            count = count + 1
    return count

def move_if(c, data, pos):
    n = len(data)
    for i in range(n):
        if pos[i] < len(data[i]) and data[i][pos[i]] == c:
            pos[i] = pos[i] + 1
    return pos

def align(data):
    n = len(data)
    last = None
    changes = 0
    pos = [ 0 ] * n
    lst = collect(data, pos)
    while not all(map(lambda x:x==None, lst)):
        if all(map(lambda x:x==lst[0], lst)):
            last = lst[0]
            #print '#1', last, pos
            pos = move_if(last, data, pos)
        elif last == None:
            # Failed
            last = False
            #print '#2 Failed', pos
            break
        else:
            count = count_char(last, data, pos)
            if count == 0:
                last = False
                break
            if count > n - count:
                changes = changes + (n-count)
                pos = move_if(last, data, pos)
                #print '#3', last, pos
            else:
                changes = changes + count
                pos = move_if(last, data, pos)
                #print '#4', last, pos
                #last = None
        lst = collect(data, pos)
    if last == False:
        return None
    else:
        return changes

num_tests = int(raw_input())
for i in range(num_tests):
    num_data = int(raw_input())
    data = []
    for j in range(num_data):
        data.append(raw_input())
    result = align(data)
    if result != None:
        print 'Case #' + str(i+1) + ': ' + str(result)
    else:
        print 'Case #' + str(i+1) + ': Fegla Won'
