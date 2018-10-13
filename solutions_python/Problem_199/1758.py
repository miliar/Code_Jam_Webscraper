def flip(x,i,k):
    n = x[:]
    for j in range(i,i+k):
        n[j] = '+' if x[j] == '-' else '-'
    return n
def flippy(x,k):
    # Build the Graph
    x = list(x)
    flipc = 0
    for i in range(0,len(x)-k+1):
        #print(i)
        if x[i] != '+':
            #print("Flippy is flippin")
            x = flip(x,i,k)
            flipc += 1
    for i in range(len(x)-k,len(x)):
        if x[i] != '+':
            flipc = "IMPOSSIBLE"
    return flipc

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  tc,m = (input().split(" "))  # read a list of integers, 2 in this case
  k = int(m)
  print("Case #{}: {}".format(i, flippy(tc,k)))