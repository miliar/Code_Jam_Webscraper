def solve( cake, S, K):
    count = 0
    for i in range( S - K + 1):
        piece = cake[i]
        if piece is 1:
            continue
        count += 1
        for j in range(K):
            cake[i + j] = abs( cake[i + j] - 1)
    
    for i in range(K - 1):
        piece = cake[ S - K + 1 + i]
        if piece is 0:
            return -1
    
    return count


T = int( raw_input())

a = 1
for i in range(T):
    line = raw_input().strip()
    cake = []
    for j in line:
        if j is "-":
            cake.append(0)
        elif j is "+":
            cake.append(1)
    S = len( cake)
    K = int(line[(S+1):])
    outputline = "case #" + str(a) + ": "
    a += 1
    res = solve( cake, S, K)
    if res is -1:
        outputline += "IMPOSSIBLE"
    else:
        outputline += str(res)
    print outputline