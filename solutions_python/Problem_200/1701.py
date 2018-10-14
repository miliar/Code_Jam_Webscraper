ouf = open('output.txt', 'w')

with open('B-large.in', 'r') as inf:
    t = int(inf.readline())
    for i in range(1, t + 1):
        inp = inf.readline().strip()
        n = [int(x) for x in list(inp)]
        #print(n)
        if len(n) == 1:
            ouf.write("Case #{}: {}\n".format(i, n[0]))
        else:
            for j in range(2, len(n)+1):
                if n[-j] > n[1-j]:
                    n[-j] -= 1
                    k = j-1
                    while k > 0 and n[-k] < 9:
                        n[-k] = 9
                        k -= 1
            value = 0
            multiplier = 1
            for j in range(1, len(n) + 1):
                value += n[-j] * multiplier
                multiplier *= 10
                
            ouf.write("Case #{}: {}\n".format(i, value))
