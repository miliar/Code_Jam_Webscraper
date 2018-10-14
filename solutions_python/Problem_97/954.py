#!/usr/bin/python -tt

def ispair(a,b):
    if a==b:
        return False
    if len(a)!=len(b):
        return False
    for i in range(0,len(a)):
        if a[i:]+a[:i]==b:
            return True
    return False

def rangepairs(start,end):
    i=0
    j=0
    array = range(start,end+1)
    count = 0
    while i<len(array):
        ele = array[i]
        j=i+1
        while j<len(array):
            if ispair(str(ele),str(array[j])):
                count = count+1
            j=j+1
        i=i+1
    return count

def main():
    ifile = open("C:\\C-small-attempt1.in","r")
    ofile = open("C:\\outputc2.txt","w")
    t=int(ifile.readline())
    i=1
    while i<=t:
        line = ifile.readline()
        line = line.split()
        ans = rangepairs(int(line[0]),int(line[1]))
        ofile.write("Case #"+str(i)+": "+str(ans)+"\n")
        i=i+1
    ifile.close()
    ofile.close()

if __name__ == '__main__':
    main()
