
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

# inp = open("in", "r")
# out = open("ou", "w")
# inp = open("A-small-attempt1.in", "r")
# out = open("A-small-output", "w")
# inp = open("A-small-2-attempt0.in", "r")
# out = open("A-small-2-output", "w")
inp = open("A-large.in", "r")
out = open("A-large-output", "w")
tt = int(inp.readline())
for i in xrange(tt):
    r, c = map(int, inp.readline().split())
    a = []
    for j in xrange(r):
        a.append(map(str, ' '.join(inp.readline().split())))

    for j in xrange(r):
        for k in xrange(c):
            if (a[j][k] != '?'):
                idx = 0
                while idx < c:
                    if (a[j][idx] == '?'):
                        a[j][idx] = a[j][k]
                    
                    if (a[j][idx] != '?' and idx > k):
                        break

                    idx += 1                

    for j in xrange(c):
        for k in xrange(r):
            if (a[k][j] == '?'):
                idx = k
                this = '?'
                while (idx < r):
                    if (a[idx][j] != '?'):
                        this = a[idx][j]
                        break

                    idx += 1

                if (idx == r):
                    idx = r-1
                    this = '?'
                    while (idx >= 0):
                        if (a[idx][j] != '?'):
                            this = a[idx][j]
                            break

                        idx -= 1

                    idx1 = j
                    while (idx1 < c):
                        # print idx, idx1, i
                        if (a[idx][idx1] != this):
                            break

                        idx1 += 1
                    
                    idx2 = k                    
                    while idx2 > idx:
                        temp = j
                        while (temp < idx1):
                        # print 'lol', idx2, temp, a[idx2][temp]
                            if (a[idx2][temp] == '?'):
                                a[idx2][temp] = this
                        
                            temp += 1
                    
                        idx2 -= 1

                else:                    
                    idx1 = j
                    while (idx1 < c):
                        # print idx, idx1, i
                        if (a[idx][idx1] != this):
                            break

                        idx1 += 1

                # idx1 -= 1
                    idx2 = k
                # print 'asdf', 'idx', idx, k, 'idx1', idx1, j, 'idx2', idx2, a[idx], this
                    while idx2 < idx:
                        temp = j
                        while (temp < idx1):
                        # print 'lol', idx2, temp, a[idx2][temp]
                            if (a[idx2][temp] == '?'):
                                a[idx2][temp] = this
                        
                            temp += 1
                    
                    # if (a[idx][j] == '?'):
                    #     a[idx][j] = a[k][j]

                    # if (a[j][idx] != '?' and idx > k):
                    #     break
                        idx2 += 1

    out.write("Case #%d:\n" % (i+1))
    for j in xrange(r):
        out.write(''.join(a[j]))
        if (i == tt-1):
            if (j == r-1):
                break

        out.write("\n")


inp.close()
out.close()