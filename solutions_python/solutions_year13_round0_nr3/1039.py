import math

def solve(a,b):
    #prepopulate fairs
    fairs = {}
    sq_a = int(math.floor(math.sqrt(a)))
    if sq_a**2 == a:
        pass
    else:
        sq_a += 1
    sq_b = int(math.floor(math.sqrt(b)))
    count = 0
    for i in range(sq_a,sq_b+1):
        if is_p(i) and is_p(i*i):
            #print i
            count += 1
    return count
    
def is_p(n):
    list1 = toList(n)
    list2 = list1[:]
    list2.reverse()
    return list1==list2
def toList(n):
    li = []
    while n > 0:
        li.append(n%10)
        n = n/10
    li.reverse()
    return li


if __name__=="__main__":
    infile = open('/Users/matthewhalverson/Downloads/C-small-attempt0.in','r')
    outfile = open('C-small.out','w')
    
    t = int(infile.readline().strip())
    for i in range(t):
        a,b = map(int, infile.readline().strip().split(" "))
        num = solve(a,b)
        string = "Case #%d: %d\n" % (i+1, num)
        print string[:-1]
        outfile.write(string)
