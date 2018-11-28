import time

in_file = "A-small.in"
out_file = "A-small.out"

happy = {}
not_happy = {}

def start():
    f_in = file(in_file, "r")
    f_out = file(out_file, "w")    
    T = int(f_in.readline().strip())

    global m
    for i in xrange(T):
        bases = []
        parts = f_in.readline().strip().split(" ")
        for j in xrange(len(parts)):
            b = int(parts[j])
            bases.append(b)
            if not happy.has_key(b):
                happy[b] = set()
            if not not_happy.has_key(b):
                not_happy[b] = set()

        n = getHappyNo(bases)
        f_out.write("Case #" + str(i+1) + ": " + str(n) + "\n")

    f_in.close()
    f_out.close()
    
def getHappyNo(bases):
    num = 2
    while num:
        if isHappyNum(num, bases):
            return num
        else:
            num = num +1
                                        
def convertToBase(num, base):
    s = ""
    while num:
        r = num%base
        s = str(r) + s
        num = int(num/base)
    return s


def isHappy(n_str, base, chkd_for):
    chkd_for.add(n_str)

    global happy
    global not_happy
    s1 = happy[base]
    s2 = not_happy[base]
    if s1.__contains__(n_str):
        return True
    if s2.__contains__(n_str):
        return False    
    
    t = 0
    for i in xrange(len(n_str)):
        t = t + int(n_str[i])*int(n_str[i])

    if(t == 1):
        s1.add(n_str)
        return True
    
    else:
        new_n_str = convertToBase(t, base)
        if chkd_for.__contains__(new_n_str):                            
            s2 = s2.union(chkd_for)
            return False
        return isHappy(new_n_str, base, chkd_for)
        
def isHappyNum(num, bases):
    for i in xrange(len(bases)):
        base = bases[i]
        n_str = convertToBase(num, base)
        if n_str == "1":
            continue
        if not isHappy(n_str, base, set()):
            return False
    return True
    
t1 = time.time()   
start()
print "total time: " + str(time.time()-t1)
           
