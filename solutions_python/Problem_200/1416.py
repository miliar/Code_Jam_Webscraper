def tidy1(n):
    m = str(n)
    i = 0
    while (i < len(m) - 1 and m[i] <= m[i+1]):
        i += 1
    if (i == len(m) - 1):
        return n
    elif (m[i] == str(1) and m[i+1] == str(0)):
        return int(str(9)*(len(m)-1))
    else:
        z = str(0)
        j = -1
        for j in range(0,i):
            if m[j] == m[i]:
                j -= 1
                break
            z = z + m[j]
        z = z + str(int(m[j+1])-1)
        for k in range(j+2,len(m)):
            z = z + str(9)
        return int(z)

t = int(raw_input())  # read a line with a single integer
for hom in xrange(1, t + 1):
    n =  int(raw_input()) # read a list of integers, 2 in this case
    print "Case #{}: {}".format(hom, tidy1(n))


