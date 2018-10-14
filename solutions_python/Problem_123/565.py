theInput = open('A-small-attempt1.in','r')
theOutput = open ('output.out','w')
def find_number(my_size,remaining):
    if len(remaining) == 0:
        return 0
    if remaining[-1] < my_size:
        return 0
    while True:
        if len(remaining) == 0:
            return 0
        if my_size > remaining[0]:
            my_size = my_size + remaining.pop(0)
        else:
            break;
    temp = remaining[:]
    temp.pop()
    remove = find_number(my_size,temp) + 1
    if my_size == 1:
        return remove
    add = find_number(my_size*2-1,remaining) + 1
    return min(remove,add)
numTest = int(theInput.readline())
for x in xrange(0,numTest):
    first_line = theInput.readline().split(" ")
    my_size = int(first_line[0].rstrip())
    #sizeRem = int(first_line[1])
    remaining = theInput.readline().split(" ")
    remaining = map(int,remaining)
    print "my_size="+ str(my_size)+"remaining"
    print remaining
    sol = find_number(my_size,sorted(remaining))
    theOutput.write("Case #"+str(x+1)+": "+str(sol)+"\n")


theInput.close()
theOutput.close()
