#!/usr/bin/env python

##Qualification Round
##Problem 2
##sellers
##Public Domain

import sys,os,fileinput

class Input:
    def __init__(self):
        if 'large.in' in os.listdir('.'):
            self.f = fileinput.input('large.in')
        elif 'small.in' in os.listdir('.'):
            self.f = fileinput.input('small.in')
        elif 'test.txt' in os.listdir('.'):
            self.f = fileinput.input('test.txt')

    def get_line(self):
        return self.f.next().strip('\n')

    def get_int(self):
        return int(self.get_line())

def output_case(case,data):
    sys.stdout.write("Case #"+str(case)+": [")
    for i in range(0,len(data)-1):
        sys.stdout.write(data[i]+', ')
    if len(data) != 0:
        sys.stdout.write(data[len(data)-1])
    sys.stdout.write(']\n')

def solve_case(input,case):
    data = input.get_line().split(' ')
    combo = int(data.pop(0))
    combos =[]
    for i in range(0,combo):
        n_c = data.pop(0)
        combos.append(([n_c[0],n_c[1]],n_c[2]))
    kill = int(data.pop(0))
    kills = []
    for i in range(0,kill):
        n_k = data.pop(0)
        kills.append((n_k[0],n_k[1]))
    spell = data.pop()
    cast_spell = []
    last = ''
    for char in spell:
        done = False
        for combo in combos:
            if char == combo[0][0]:
                if last == combo[0][1]:
                    cast_spell.pop()
                    cast_spell.append(combo[1])
                    last=combo[1]
                    done = True
            elif char == combo[0][1]:
                if last == combo[0][0]:
                    cast_spell.pop()
                    cast_spell.append(combo[1])
                    last=combo[1]
                    done=True
        if not done:
            for kill in kills:
                if char == kill[0]:
                    if kill[1] in cast_spell:
                        cast_spell = []
                        last = ''
                        done = True
                if char == kill[1]:
                    if kill[0] in cast_spell:
                        cast_spell = []
                        last = ''
                        done = True
        if not done:
            cast_spell.append(char)
            last=char
    output_case(case,cast_spell)

if __name__ == '__main__':
    input = Input()
    cases = input.get_int()

    for i in range(0,cases):
        solve_case(input,i+1)
