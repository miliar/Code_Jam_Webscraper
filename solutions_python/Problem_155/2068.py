__author__ = 'bharathramh'

import sys

def out(num):
    print(num)

def main():
    f = open(sys.argv[1], 'r')
    o=[]
    for line in f:
        o.append(line)
    f.close()
    cases = o[0]
    data =o[1:]
    # for case in range(0,int(cases)):
    #     # print(case)
    #     data.append(input())
    out=[]
    # print(data)
    count=0
    for i in data:
        count+=1
        sp = i.split()
        asu = 0         #already stood up
        yetto = 0       #number of people who has to stand
        tobe = 0        #final value
        total = int(sp[0])
        # print(total)
        for c in sp[1]:
            asu+=int(c)
            tobe+=1

            if(asu < tobe):
                yetto+=1
                asu+=1
            # print("asu ",asu, " yetto ", yetto, " tobe ",tobe)


        out.append("Case #%d: %d\n" %(count,yetto))
    # for e in data:

        f = open("output", 'w')
        for x in out:
            f.write(x)

        f.close()
if __name__ =="__main__":
    main()