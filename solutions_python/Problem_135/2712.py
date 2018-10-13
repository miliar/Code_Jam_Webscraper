

def findsc(str1,str2):
    strc1 = str1.split();
    strc2 = str2.split();
    #print strc1,strc2
    target = []
    for s1 in strc1:
        for s2 in strc2:
            if s1 == s2:
                target.append(s1);
                break;
    return target;
#print findsc("1 2 3 4","3 4 5 6")

if __name__ == "__main__":
    input = open("input.txt",'rb');
    output = open("output.txt",'w');
    num = int(input.readline());
    i = 1;
    try:
        while i<=num:
            r1 = int(input.readline());
            a1 = []
            a1.append(input.readline())
            a1.append(input.readline())
            a1.append(input.readline())
            a1.append(input.readline())

            r2 = int(input.readline());
            a2 = []
            a2.append(input.readline())
            a2.append(input.readline())
            a2.append(input.readline())
            a2.append(input.readline())

            rlist = findsc(a1[r1-1],a2[r2-1])

            res = ''
            if len(rlist) == 0:
                res = 'Volunteer cheated!'
            elif len(rlist) == 1:
                res = rlist[0]
            else:
                res = 'Bad magician!'
            
            #print "Case #%d: %s"%(i,res)
            output.write("Case #%d: %s\n"%(i,res));
            i = i+1;
    finally:
        input.close();
        output.close();
    













