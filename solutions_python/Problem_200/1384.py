#--- READ INPUT ---#
inp = open('B-large.in', 'r')
#inp = open('test.in', 'r')
o = open('output-large.txt', 'w')

n = int(inp.readline())
for i in range(n):
    num = inp.readline()[:-1]

    #--- SOLUTION ---#
    l = [int(c) for c in num]
    for j in range(len(l)-2, -1, -1):
        if l[j+1] < l[j]:
            l[j] -= 1
            l[j+1] = 9
            for k in range(j+1, len(l)):
                l[k] = 9

    l = [str(x) for x in l]
    res = int(''.join(l))

    #--- WRITE OUTPUT ---#
    s = 'Case #' + str(i+1) + ': ' + str(res)
    o.write(s + '\n')
inp.close()
o.close()
