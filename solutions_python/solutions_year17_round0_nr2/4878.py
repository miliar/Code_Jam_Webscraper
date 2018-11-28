def minimumFlips(pancakes,k):
    groupedHeight = 1 + pancakes.count(k*'-')+pancakes.count((k-1)*'-'+'+') + pancakes.count('+'+(k-1)*'-')
    if groupedHeight == 1 and pancakes.count('+') != len(pancakes):
        return "IMPOSSIBLE"
    if pancakes.endswith('-'):
        return groupedHeight
    else:
        return groupedHeight - 1
def q1():
    #fname=input()
    #r=open(fname)
    N=int(input())
    for i in range(1, N + 1):
      S, K = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
      K=int(K)
      print("Case #{}: {}".format(i, minimumFlips(S,K)))
      # check out .format's specification for more formatting options

def testPassed(i):
    return list(str(i)) == sorted(list(str(i)))
    

def tidyNum(s):
    for i in range(s,0,-1):
        if testPassed(i):
            return i
    

def q2():
    N=int(input())
    for i in range(1, N + 1):
      S=int(input())
      print("Case #{}: {}".format(i, tidyNum(S)))
      # check out .format's specification for more formatting options

    
