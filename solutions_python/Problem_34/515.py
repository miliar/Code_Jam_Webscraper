#!/usr/bin/env python

def parse_pattern(pattern):
    p_list = []
    flag = False
    for i in pattern:
        if i == '(':
            flag = True
            tmp = []
        elif i == ')':
            flag = False
            p_list.append(tmp)
        else:
            if flag == False:
                p_list.append([i])
            elif flag == True:
                tmp.append(i)

    return p_list

def group_words(L, D_list):
    d_list = []
    for i in range(L):
        d = {}
        for item in D_list:
            if not d.has_key(item[i]):
                d[item[i]] = [item]
            else:
                d[item[i]].append(item)
        d_list.append(d)

    return d_list

#   def build_tree(L, D_list):
#       root = {}
#       for i in range(L):
#           if 

def decipher(L, words_list, pattern):
    p_list = parse_pattern(pattern)
    n = 1
    for i in range(L):
        if n == 0:
            break
        n = 0
        d_list = group_words(L, words_list)
        words_list = []
        keys = d_list[i].keys()
        p_words = p_list[i]
        for k in keys:
            if k in p_words:
                words_list.extend(d_list[i][k])
                n = n + 1
    return n
