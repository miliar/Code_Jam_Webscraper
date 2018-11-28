#! /usr/bin/python2.7
#-*-coding:utf-8-*


def t(n,C,F):
    return C/(F*n+2)



def case3(C,F,X):
    Tlast = 0
    Tcurrent = 0
    n =0
    while True:
        Tcurrent = t(n,C,F) + Tlast

        if Tcurrent + t(n+1,X,F) > t(n,X,F)+Tlast:
            return t(n,X,F)+Tlast

        n+=1
        Tlast = Tcurrent






def main():
    e = open("in", "r")
    s = open("sortie", "w")
    # case2(500.0,4.0,2000.0)
    T = int(e.readline().split()[0])
    # print T
    print case3(30.0,1.0,2.0)
    # cases=[[500.0,4.0,2000.0]]
    cases=[]
    for i in xrange(0,T):
        cases.append([float(num) for num in e.readline().split()])
    print cases

    for i in xrange(0,len(cases)):
        # print "Case #"+str(i+1)+": "+str(case2(cases[i][0],cases[i][1],cases[i][2]))
        s.write("Case #"+str(i+1)+": "+"{0:.15f}".format(round(case3(cases[i][0],cases[i][1],cases[i][2]),9))+"\n")


    e.close()
    s.close()







if __name__ == '__main__':
    main()



