T = int(raw_input())

def flip(s):
    if s == "-":
        return "+"
    elif s == "+":
        return "-"

def multiflip(pancakes, K):
    N = len(pancakes)
    numflips = 0
    for i in range(N):
        if pancakes[i] == "-":
            if i + K > N:
                return "IMPOSSIBLE"
            numflips = numflips + 1
            for j in range(K):
                pancakes[i+j] = flip(pancakes[i+j])
    return str(numflips)

for case in range(T):
    line = raw_input().split(" ")
    pancakes = list(line[0])
    K = int(line[1])
    print "Case #" + str(case+1) + ": " + multiflip(pancakes, K)
