from itertools import permutations as pnr, combinations as cnr

def isRe(x, y):
    a, b = list(str(x)), list(str(y))
    for i in range(len(a)):
        a.insert(0, a.pop())
        if a == b:
            return True
    return False    

if __name__ == "__main__":
    
    fi = open("input.txt", "r")
    fo = open("output", "w")

    tests = int(fi.readline())
    
    for test in range(tests):

        line = fi.readline()
        nums = line.split()
        
        a = int(nums[0])
        b = int(nums[1])
        res = 0
        ans = []
        for x in xrange(a, b + 1):
            perm = []
            for p in pnr(list(str(x))):
                n = int("".join(p))
                if n >= a and n <= b and n not in perm:
                    perm.append(n)
                #print "p" ,p
            perm.sort()
            #print perm
            if len(perm) > 1 and perm not in ans:
                    ans.append(perm)
                        
        for a in ans:
            if len(a) > 2:
                for f in cnr(a, 2):
                        #print a, f, isRe(f[0], f[1])
                        if isRe(f[0], f[1]):
                            res += 1
            else:
                #print a, isRe(a[0], a[1])
                if isRe(a[0], a[1]):
                    res += 1   
                    
        fo.write("Case #" + str(test + 1) + ": " + str(res) + "\n")

    fo.close()
    fi.close()
