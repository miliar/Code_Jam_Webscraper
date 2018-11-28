__author__ = 'achhangani'

loop = int(raw_input())

for i in range(loop):
    standing =0
    added =0
    arr = raw_input().split(" ")
    num = arr[1]
    for j in range(len(arr[1])):
        standing += int(num[j])
        if (j+1) > standing:
            added += abs(standing-(j+1))
            standing+=1
        else:
            added += 0
    print "Case #"+str(i+1)+":",added