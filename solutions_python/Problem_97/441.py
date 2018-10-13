import string

def numofrecycled(lower, upper):
    amount = 0
    for number in xrange(lower,upper):
        number_str = str(number)
        candidate_str = number_str
        length=len(number_str)
        recycled = set()
        for i in xrange(length - 1):
             candidate_str = candidate_str[-1] + candidate_str[0:-1]
             candidate = int(candidate_str)
             if candidate > number and candidate <= upper:
                 recycled.add(candidate_str)
        amount += len(recycled)
    return amount

f = open("input")
file = f.readlines()

ctr = 0
for line in file:
    if ctr == 0:
        ctr += 1
        continue
    values = string.split(line,' ')
    print "Case #" + str(ctr) + ":" , numofrecycled(int(values[0]),int(values[1]))
    ctr += 1

