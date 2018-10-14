import sys
sys.stdin = open("InfhouseIn.txt","r")
sys.stdout = open("InfhouseOut.txt","w")
tests = int(raw_input())
for t in range(1,tests+1):
    n = int(raw_input())
    pancakes = map(int,raw_input().split())
    queue = []
    queue.append([pancakes,0])
    best = 999999999
    vis = set()
    vis.add(tuple(sorted(pancakes)))
    while queue:
        state,time = queue.pop(-1)
        state.sort()
       # print state
        best = min(best,time+state[-1])
        if state[-1]>2:
            big = state[-1]
            for left in range(1,big):
                add = [state[-1]-left]
                state[-1] = left
                if (tuple(sorted(state+add))) not in vis:
                    queue.append([state+add,time+1])
                    vis.add(tuple(sorted(state+add)))
                state[-1] = big

    print "Case #"+str(t)+":",best
sys.stdout.close()
