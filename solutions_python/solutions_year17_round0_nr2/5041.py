import sys
import profile
import itertools


def ordertest(mylist):
    return all(b >= a for a, b in zip(mylist, itertools.islice(mylist, 1, None)))

def istidy(N):
    mylist = []
    for d in str(N):
        mylist.append(int(d))

    if mylist.count(mylist[0]) == len(mylist):
        return True
    elif ordertest(mylist) is True:
        return True
    else:
        return False


def solve(N) :

    for i in range(N,0,-1):
        if istidy(i) is True:
            return i
            break

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    arr=[]
    testcases = input()

    for caseNr in range(1, int(testcases) + 1):
            N = int(input())
            print("Case #%i: %s" % (caseNr, solve(N)))
