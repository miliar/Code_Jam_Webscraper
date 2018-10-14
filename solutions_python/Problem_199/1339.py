import sys

sys.setrecursionlimit(2000)

def firstMinus(s):
    try:
        return s.index('-')
    except:
        return -1

def flipped(s,i):
    if s[i]=='+': return '-'
    return '+'

def solved(s):
    for i in s:
        if i!='+': return False
    return True

def solve(s, k, count):
    if solved(s): return count
    fm = firstMinus(s)
    if fm+k > len(s): return -1  # no solution

    #flip k pancakes from fm to fm+(k-1)
    for i in range(fm,fm+k):
        s[i]=flipped(s,i)
    return solve(s,k,count+1)


    

t = int(input())
for i in range(t):
    line = input()
    s = line.split()[0]
    k = int(line.split()[1])

    #print (s,k)
    #print(firstMinus(s))
    sol=solve(list(s),k,0)
    if sol==-1: sol="IMPOSSIBLE"
    print("Case #%i:"%(i+1), sol)
