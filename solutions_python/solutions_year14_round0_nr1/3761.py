f = open("A-small-attempt1.in",'r')
fo = open("test.out",'w')

t = int(f.readline())

def readMat():
    M = []
    num = int(f.readline())
    for line in range(4):
        lst = []
        for n in f.readline().split(" "):
            lst.append(int(n))
        M.append(lst)
    return M[num-1]

def dup(l):
    c = 0
    for n in l:
        if n:
            c+=1
    return c


for x in range(t):
    x+=1
    ls1 = readMat()
    ls2 = readMat()
    boolean = []

    for u in range(4):
        boolean.append(ls1[u] in ls2)

    print ls1
    print ls2
    print boolean
    # print True in boolean

    
    if dup(boolean) > 1:
        fo.write("Case #"+str(x)+": Bad magician!\n") 
        print "bad magician"
    elif not(True in boolean): 
        fo.write("Case #"+str(x)+": Volunteer cheated!\n")
        print "cheated"
    else:
        fo.write("Case #"+str(x)+": "+str(ls1[boolean.index(True)])+"\n")
        print ls1[boolean.index(True)]



