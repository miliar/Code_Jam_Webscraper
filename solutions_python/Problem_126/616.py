#!/urs/bin/env python3

glas = ['a','e','u','i','o']
A = []

with open ('input.txt') as input:
    input.readline()
    k = 1
    for line in input:
        A = [] 
        sum = 0
        c = -1
        before = 0
        last = 0
        name,n = line.split(' ')
        n = int(n)
        for i in range(len(name)):

            count = 0
            for j in name[i:i+n]:
                if not j in glas:
                    count+=1
                else:
                    break
            if count >= n:
                if before:
                    last += before
                before = i+1-last
                after = len(name)-(i+n-1)
                sum += before*after
        print('Case #{}: {}'.format(k,sum))
        k+=1