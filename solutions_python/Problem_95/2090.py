#! /usr/bin/python3.2

input_f = input()

f = open(input_f, 'r')
lines = f.readlines()
lines = [l.strip('\n') for l in lines]
f.close()

strings = lines[1:]

from_s = ' acbedgfihkjmlonqpsrutwvyxz'
to_s   = ' yehosvcdxiulgkbzrntjwfpamq'

table = str.maketrans(from_s, to_s)

translated = [l.translate(table) for l in strings]

f = open('speaking_output.out', 'w')
cpt = 1
for line in translated:
    f.write('Case #'+str(cpt)+': '+line+'\n')
    cpt += 1
f.close()
