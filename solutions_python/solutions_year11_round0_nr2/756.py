f = open('B-large.in', 'r')
line = f.readline()
count = 0
while line:
    count += 1
    line = f.readline()
    data = line.split()
    if len(data) < 2:
        break
    combines = []
    opposed = []
    pos = 1
    for m in xrange(0,int(data[0])):
#        print m
        combines.append(list(data[pos]))
        pos+=1
    for m in xrange(0,int(data[pos])):
#        print m
        pos+=1
        opposed.append(list(data[pos]))
    pos+=2

    invoke_list = []
    for m in list(data[pos]):
#        print invoke_list, m
        # first, try to combine
        ix = 0
        len_combines = len(combines)
        while ix < len_combines:
            i = combines[ix]
            if len(invoke_list) > 0:
                l = invoke_list[-1]
                if (m == i[0] and l==i[1]) or (m==i[1] and l==i[0]):
#                    print "combining %c and %c to get %c" % (m, l, i[-1])
                    m = i[-1]
                    invoke_list.pop()
                    ix = -1
            ix += 1
            len_combines = len(combines)

        k = False
        ix = 0
        while ix < len(opposed):
            i = opposed[ix]
            for l in invoke_list:
                if (m==i[0] and l==i[1]) or (l==i[0] and m==i[1]):
#                    print m,l, "clearing list!"
                    k = True
            ix += 1

        if k:
            invoke_list = []
#            print "clearing list due to %c" % m
        else:
#            print "adding %c" % m
            invoke_list.append(m)

    a = "Case #%d: " % count
    print a + "[" + ", ".join(invoke_list) + "]"
    
    
    
