
def mprint(a):
    print (a)

def docount(n,s, p, lst):
    mprint(n)
    mprint(s)
    mprint(p)
    mprint(lst)
    lst.sort()
    count = 0
    nsuprise = 0
    for i in lst:
        mprint("i is "+ str(i))
        if (i/3 >= p):
            count+=1
        elif (i/3 >= p-1 and i%3 > 0):
            count+=1
        elif ((p-1) >= 0 and i/3 >= p-1 and i>1 and nsuprise < s):
            count+=1
            nsuprise+=1
        elif ((p-2) >=0 and i/3 >= p-2 and (i%3 > 1) and nsuprise < s):
            count+=1
            nsuprise += 1
        mprint("count is " + str(count))
        mprint("nsuprise " + str(nsuprise))

    return count

def docount1(n,s, p, lst):
    mprint(n)
    mprint(s)
    mprint(p)
    mprint(lst)
    lst.sort()
    count = 0
    nsuprise = 0
    for i in lst:
        if (i >= 3*p):
            count+=1
        elif ((p-1) >= 0 and i >= (p-1)+(p-1)+p):
            count+=1
        elif ((p-2) >= 0 and i >= (p-2)+(p-1)+p and nsuprise < s):
            count+=1
            nsuprise+=1
        elif ((p-2) >= 0 and i >=  (p-2)+(p-2)+p and nsuprise < s):
            count+=1
            nsuprise += 1
    mprint("count is " + str(count))
    mprint("nsuprise " + str(nsuprise))

    return count

#f = open("dance.test","r")
#f = open("B-small-attempt2.in","r")
#f = open("B-small-attempt1.in","r")
#f = open("B-small-attempt0.in","r")
#f = open("B-small-attempt3.in","r")
f = open("B-large.in","r")

s = f.readline()
ntrials = int(s)

i =0

fout = open("dance.out","w")


for line in f:
    i+=1
    fields = line.split()
    n = int(fields.pop(0))
    s = int(fields.pop(0))
    p = int(fields.pop(0))
    lst = []
    for elt in fields:
        lst.append(int(elt))
    result = docount(n,s,p,lst)
    result1 = docount1(n,s,p,lst)
    if (result != result1):
        mprint("Result " + str(result1) + " and " + str(result))
        mprint("uh oh")
    print "Case #" + str(i) + ": "  + str(result1)
    fout.write("Case #" + str(i) + ": "  + str(result1) +"\n")

    
