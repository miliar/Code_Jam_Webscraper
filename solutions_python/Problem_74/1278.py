#!/usr/bin/env python
# coding:utf-8
import math

n = int(input())
string=[]
for i in range(n):
    bot = [1,1]
    commands = input().split(" ")[1:]
    turn = 0 if commands[0] == "O" else 1
    acc = 0
    time = 0
    for j in range(len(commands)//2):
        if j != 0 and commands[j*2] != commands[j*2-2]:
            turn = 1-turn
            if acc >= math.fabs(bot[turn]-int(commands[j*2+1])):
                bot[turn] = int(commands[j*2+1])
            else:
                if bot[turn]<int(commands[j*2+1]):
                    bot[turn]+=acc
                else:
                    bot[turn]-=acc
            acc=0
        if bot[turn] == int(commands[j*2+1]):
            time+=1
            acc+=1
        else:
            if bot[turn]<int(commands[j*2+1]):
                time+=int(commands[j*2+1])-bot[turn]+1
                acc+=int(commands[j*2+1])-bot[turn]+1
                bot[turn]=int(commands[j*2+1])
            else:
                time+=bot[turn]-int(commands[j*2+1])+1
                acc+=bot[turn]-int(commands[j*2+1])+1
                bot[turn]=int(commands[j*2+1])

    string.append("Case #{0}: {1}".format(i+1,time))
for i in string:
    print(i)
