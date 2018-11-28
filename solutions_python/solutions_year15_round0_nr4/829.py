import os, sys, math

__debug=True
#__debug=False

def debug(str):
    if __debug:
        print "[DEBUG] %s" % str

def main():
    no_cases=int(sys.stdin.readline().strip())
    for i in range(1,no_cases+1):
        variables=sys.stdin.readline().strip().split(' ')
        X=int(variables[0])
        R=int(variables[1])
        C=int(variables[2])
        if X==1:
            print "Case #%d: GABRIEL" % i
        elif X==2:
            if R==1 and C==1:
                print "Case #%d: RICHARD" % i
            elif R*C%2==0:
                print "Case #%d: GABRIEL" % i
            else:
                print "Case #%d: RICHARD" % i
        elif X==3:
            if R==1 or C==1:
                print "Case #%d: RICHARD" % i
            elif R*C%3==0:
                print "Case #%d: GABRIEL" % i
            else:
                print "Case #%d: RICHARD" % i
        elif X==4:
            if R<4 and C<4:
                print "Case #%d: RICHARD" % i
            elif R<3 or C<3:
                print "Case #%d: RICHARD" % i
            else:
                print "Case #%d: GABRIEL" % i
        else:
            print ">_<"
    return 0


if __name__ == "__main__":
    main()
