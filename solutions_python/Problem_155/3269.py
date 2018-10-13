import sys

lines = [line.strip() for line in open(sys.argv[1])]

ntests = int(lines[0])

tests = [line.split() for line in lines[1:]]
instances = []

for test in tests:
    instances.append([int(i) for i in list(test[1])])
    #if int(test[0])+1 != len(instances[-1]):
        #print instances[-1],test[0]

guests = [0] * ntests
for j,inst in enumerate(instances):
    count = 0
    for k,i in enumerate(inst):
        if k > count:
            guests[j] += k-count
            count = k
        count += i
    print "Case #{0}: {1}".format(j+1,guests[j])

