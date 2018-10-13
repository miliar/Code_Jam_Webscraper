fin = open("input.txt", "r")

tests_num = int(fin.readline())

for i in xrange(tests_num):
    n =[int(x) for x in list(fin.readline().strip())]
    tidy = True
    ind = -1
    for j in xrange(len(n) - 1):
        if n[j] > n[j + 1]:
            tidy = False
            ind = j
            break

    if tidy:
        print "Case #" + str(i+1) + ": " + "".join([str(x) for x in n])
    else:
        k = ind
        while k > 0 and n[k] - 1 < n[k - 1]:
            k -= 1
        n[k] = n[k] - 1
        for j in xrange(k + 1, len(n)):
            n[j] = 9
        ind = 0
        while ind < len(n) and n[ind] == 0:
            ind += 1
        if ind == len(n):
            print "Case #" + str(i+1) + ": 0"
        else:
            print "Case #" + str(i+1) + ": " + "".join([str(x) for x in n[ind:]])

fin.close()