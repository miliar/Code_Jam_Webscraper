

def divide(i, j):
    return i/j == i//j or j/i == j//i

def solve(low, high, players):
    for i in range(low, high + 1):
       alll = True
       for j in players:
           if not divide(i, j):
               alll = False
               break
       if alll:
           return i
    return False

n_tests = int(input())
for t in range(0, n_tests):
    nplayers, low, high = [ int(i) for i in input().split(" ") ]
    players = [ int(i) for i in input().split(" ") ]
               

    ret = solve(low, high, players)
    if ret:
        print ("Case #"+str(t+1)+": "+str(int(ret)))
    else:
        print ("Case #"+str(t+1)+": NO")