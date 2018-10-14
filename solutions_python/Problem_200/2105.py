n = int(raw_input())

for xi in xrange(n):
    string = raw_input()
    list_val = [int(i) for i in string]
    for i in range(1,len(list_val)):
        if list_val[i] < list_val[i-1]:
            list_val[i-1] -= 1
            for j in range(i, len(list_val)):
                list_val[j] = 9
            for k in range(i-1,0,-1):
                if list_val[k] < list_val[k-1]:
                    list_val[k] = 9
                    list_val[k-1] -= 1

    while(list_val[0] == 0):
        list_val = list_val[1:]

    print "Case #{}: {}".format(xi+1,''.join([str(i) for i in list_val]))