import os, sys
from pprint import *

inFile = None
outFile = None

def isPalindrome(b):
	a = str(b)
	return a == ''.join(reversed(a))

def isPalindrome(b):
    a = str(b)
    return a == ''.join(reversed(a))

def add(k,n):
    k = ''.join(reversed(str(k))) + '0'*n
    return int(k[:n])

ans = []
def go(current, pos, n):
    if pos > (n+1)/2:
        return

    value = current
    if n%2 != 0:
        rev = add(current%(10**((n-1)/2)), n)
    else:
        rev = add(current%(10**((n)/2)), n)
    value = current + rev
    
    if isPalindrome(value) and isPalindrome(value*value):
        if value:
            ans.append(value)
        go(current + (10**pos)*1, pos+1, n)
        go(current + (10**pos)*2, pos+1, n)
        go(current, pos+1, n)

all = [3]
for n in range(1, 52):
    ans = []
    go(0, 0, n)
    actual = sorted(list(set(ans)))
    all.extend(actual)


fairs = []

def printAnswer(case, answer):
	outFile.write('Case #{0}: {1}\n'.format(case+1, answer))

def solveCase(caseNo):
	(a,b) = map(int, inFile.readline().strip().split())

	ans = 0
	for fair in fairs:
		if fair >= a and fair <= b:
			ans += 1

	printAnswer(caseNo, ans)

def main():
	for x in all:
		fairs.append(x*x)

	print 'preprocess done'

	cases = int(inFile.readline().strip())
	for case in range(cases):
		solveCase(case)

if __name__ == '__main__':
	inFile = open('in.txt','rt')
	outFile = open('out.txt', 'wt')
	main()