#!/usr/bin/python3

t = int(input())

for i in range (1, t+1):
    line = input()
    audience = line.split()[1]
    counter = 0
    total = 0
    for k in range(len(audience)):
        if not k == 0 and int(audience[k]) > 0 and total < k:
            counter += k-total
            total += k-total
        total += int(audience[k])   
        
    print("Case #{}: {}".format(i, counter))

