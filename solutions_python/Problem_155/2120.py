__author__ = 'Andy'

input = open('input')
input.readline();
count = 0
for i in [i.strip('\n') for i in input.readlines()]:
    test = i.split(' ')[1]
    sum = 0
    si = 0
    min = []
    for k in test:
        sum += int(k)
        min.append(si - sum)
        si+=1
    print("Case #"+str(count+1)+": "+ str((max(min)+1) if (max(min)+1) >=0 else 0))
    count+=1
