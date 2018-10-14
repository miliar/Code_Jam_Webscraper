import sys, math

stdout = sys.stdout
stdin = sys.stdin
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
for CASE in range(1,n+1):
    N, R, O, Y, G, B, V = map(int, input().split())

    stable = []
    for i in range(R):
        stable.append('R')
    for i in range(O):
        stable.append('O')
    for i in range(Y):
        stable.append('Y')
    for i in range(G):
        stable.append('G')
    for i in range(B):
        stable.append('B')
    for i in range(V):
        stable.append('V')

    possible = True
    previous = set([])

    unsorted = True
    while unsorted and possible:
        s = str(stable)
        if s in previous:
            possible = False
            break
        previous.add(s)
        
        unsorted = False
        for i in range(len(stable)):
            ci = i + 1
            if ci == len(stable):
                ci = 0
            if stable[i] == stable[ci]:
                si = i + 2
                if si >= len(stable):
                    si -= len(stable)
                temp = stable[ci]
                stable[ci] = stable[si]
                stable[si] = temp

                unsorted = True                
    
    print('Case #' + str(CASE) + ': ', end='')
    if possible:
        s = ''
        for c in stable:
            s = s+c
        print(s)
    else:
        print('IMPOSSIBLE')

sys.stdout = stdout
sys.stdin = stdin
