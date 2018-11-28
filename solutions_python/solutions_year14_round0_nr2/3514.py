#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     13/04/2014
# Copyright:   (c) Admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f = open(r'C:\Users\Admin\Downloads\B-small-attempt0.in', 'r');
    n=int(f.readline());
    for x in range(0,n):
        s = f.readline().replace("\n","");
        arr = s.split(" ");
        for i in range(0,len(arr)):
            arr[i]=float(arr[i]);
        rate=2;
        num=0;
        target=arr[2];
        addRate=arr[1];
        farm=arr[0];
        cancel=False;
#starthere
        prevT=9999999999999999999999999999999999999999999999999999999999999999;
        numFarm=-1;
        while (cancel!=True):
            numFarm+=1;
            t=0
            cRate=rate;
            for i in range(0,numFarm):
                t+=farm/cRate;
                cRate+=addRate;
            t+=target/cRate;
            if (t>prevT):
                cancel=True;
                break;
            prevT=t;
        print("Case #"+str(x+1)+": "+str(prevT));
    pass

if __name__ == '__main__':
    main()
