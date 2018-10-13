def possible(rating, p):
    for delta in range(1,3):
        for n1 in range(10,p-1,-1):
            rating2 = rating - n1
            for n2 in range(n1-delta,n1+delta):
                n3 = rating2 - n2
                if(n3 >= 0 and n2 >= 0 and n2 <= 10 and n3 <= 10 and
                abs(n1-n2) <= delta and abs(n3-n2) <= delta and abs(n1-n3) <= delta and n1+n2+n3 == rating):
                    #print("{3}: {0} {1} {2}, {4}".format(n1,n2,n3,rating,delta))
                    return delta
    return 0

f = open('c.in','r')
cases = int(f.readline())
for c in range(cases):

    values = f.readline().rstrip().split(' ')
    googlers = int(values[0])
    surprising = int(values[1])
    p = int(values[2])
    ratings = values[3:]
    #print("p = {0}".format(p))
    sum = 0
    for rating in ratings:
        res = possible(int(rating),p)
        if(res == 1):
            sum += 1
        if(res == 2 and surprising > 0):
            sum += 1
            surprising -= 1
    print("Case #{0}: {1}".format(c+1,sum))