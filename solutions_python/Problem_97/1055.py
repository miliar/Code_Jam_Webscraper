from sys import stdin

def get_trans(istr, b, nset):
    length = len(istr)
    res = 0
    iset = []
    for i in range(1, length):
        ip1 = istr[0:i]
        ip2 = istr[i:]
        newstr = ip2 + ip1
        if int(newstr) == int(istr):
            continue
        if len(str(int(newstr))) != len(istr):
            continue
        if int(newstr) <= b:
            if int(newstr) > int(istr):
                nset.append(int(newstr))
                if int(newstr) not in iset:
                    iset.append(int(newstr))


    return res + len(iset)
    
def count(astr, bstr, nset):
    anum = int(astr)
    bnum = int(bstr)
    res = 0
    for i in range(anum, bnum + 1):
        istr = str(i)
        res = res + get_trans(istr, bnum, nset)
    return res
        
    
def main():
    T = int(stdin.readline())
    for i in range(1, T+1):
        nset = []
        res = 0
        line = stdin.readline()
        astr, bstr = line.split();

        if len(bstr) <= 1:
            res = 0
        else:
            res = count(astr, bstr, nset)
        #print "Case #"+str(i)+": "+str(res)
        print "Case #"+str(i)+": "+str(res)
        #print nset
    
if __name__ == "__main__":
    main()
