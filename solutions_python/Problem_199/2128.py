infilecode = "ALI"
##infilecode = 'XI'

import sys


def allHappy(pancakes):
	for i in pancakes:
		if(i == '-'): return False
	return True


def flip(pancakes, flipperLen, index):
	pancakes = list(pancakes)
	for i in range(index,index+flipperLen):
		if pancakes[i] == '+': pancakes[i] = '-'
		else: pancakes[i] = '+'
	return "".join(pancakes)


mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}

infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())
for case in range(1,T+1):
    ## Read inputs and calculate answer
    S = input()
    #print(S)
    things = S.split()
    flipperLen = int(things[1])
    pancakes = things[0]
    ##    
    count = 0
    for i in range(len(pancakes)-flipperLen+1):
    	if(pancakes[i] == '-'): 
    		pancakes = flip(pancakes,flipperLen,i)
    		count+=1

    if(allHappy(pancakes)): answer = count
    else: answer = 'IMPOSSIBLE'

    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)

