from math import *

def integral_in_point(R,x):
    return ((R*R)/2.0)*(asin(x/R))+(x/2.0)*sqrt(R*R-x*x)

def integral(R,x1,x2):
    return integral_in_point(R,x2)-integral_in_point(R,x1)

def findxy(R,x):
    return sqrt(R*R - x*x)

def solve(f,R,t,r,g):
    x=y=r+f
    fly_face=0.0
    racquet_face=pi*R*R
    while hypot(x,r+f)<R-t-f:
        y=r+f
        while hypot(x,y)<R-t-f:
            print "%f %f" % (x,y)
            if hypot(x+g-2*f,y+g-2*f)<=R-t-f:
                fly_face+=(g-2*f)*(g-2*f)
                print "easy"
            elif hypot(x,y+g-2*f)<=R-t-f:
                if hypot(x+g-2*f,y)<=R-t-f:
                    print "first"
                    x1=findxy(R-t-f,y+g-2*f)
                    fly_face+=max(0,(g-2*f)*(x1-x)+max(0,integral(R-t-f,x1,x+g-2*f)-(x+g-2*f-x1)*y))
                else:
                    print "second"
                    x1=findxy(R-t-f,y+g-2*f)
                    x2=findxy(R-t-f,y)
                    fly_face+=max(0,(g-2*f)*(x1-x)+max(0,integral(R-t-f,x1,x2)-(x2-x1)*y))
            elif hypot(x+g-2*f,y)<=R-t-f:
                print "third"
                fly_face+=max(0,max(0,integral(R-t-f,x,x+g-2*f)-(g-2*f)*y))
            else:
                print "fourth"
                x2=findxy(R-t-f,y)
                fly_face+=max(0,integral(R-t-f,x,x2)-(x2-x)*y)
            print fly_face
            y+=g+2*r
        x+=g+2*r
    fly_face*=4.0
    return 1.0-(fly_face/racquet_face)

def main():
    infile=open("input.txt","r")
    outfile=open("output.txt","w")
    tests=int(infile.readline()[:-1])
    for i in range(tests):
        [f,R,t,r,g]=map(float,infile.readline()[:-1].split(" "))
        print i
        if (g<2*f):
            outfile.write("Case #%d: 1.000000\n" % i+1);
        else:
            outfile.write("Case #%d: %f\n" % (i+1,solve(f,R,t,r,g)));
    infile.close()
    outfile.close()

if __name__=="__main__":
    main()
