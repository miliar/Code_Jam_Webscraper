import sys

f = open(sys.argv[1],'r')
o = open(sys.argv[2],'w')

cases = int(f.readline().split()[0])

case = 1
while case<=cases:
    test = f.readline().split()
    maxshy = int(test[0])
    people = test[1]
    total = int(people[0])
    invite = 0
    for i in range(1,maxshy+1):
        if total<i:
            invite += i-total
            total = i
        total += int(people[i])
    o.write("Case #{}: {}\n".format(case,invite))
    case += 1

o.close()
f.close()
