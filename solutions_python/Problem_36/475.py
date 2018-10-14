#! /usr/bin/python

N = input()
pattern = "welcome to code jam"

def solve(index,data):
	if index < (len(pattern)-1):
		result = 0
		pos = data.find(pattern[index])
		while pos != -1:
			result += solve(index+1,data[pos+1:])
			data = data[pos+1:]
			pos = data.find(pattern[index])
		return result	
	else: 
		return data.count(pattern[index])
		


for i in range(N): 
	result = solve(0,raw_input())
	print "Case #%d: %04d" % ((i+1), (result%10000))
    	
