#!/usr/bin/env python
#coding:utf-8

import math

def gen_template(x):
    return "%0"+str((int(math.log10(x))+1))+"d"

def rec(n,m):
    for x in range(len(n)):
        if m == (n[x:] + n[0:x]):
            return 1
    return 0

def in_number(x):
    dic = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
    for a in x:
        dic[a] = dic[a] + 1
    return dic

def solve(A,B):
    temp = gen_template(A)
    ret = 0
    for n in range(A,B):
        tempn = temp%n
        k = []
        for x in range(len(tempn)):
            tp = int(tempn[x:]+tempn[0:x])
            if not tp in k:
                if(n+1 <= tp <= B):
                    ret = ret + 1
            k.append(tp)

    return ret


def main():
    T = int(input())
    for i in range(T):
        inp = input().strip().split(' ')
        inp = [int(i) for i in inp]
        print("Case #%d: "%(i+1)+str(solve(inp[0],inp[1])))

if __name__ == "__main__":
    main()
