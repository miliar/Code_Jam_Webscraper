#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    a=file1.readlines()
    cases=int(a.pop(0))
    booleans=[]
    for x in range(cases):
        booleans.append(boolean(a[x]))
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        if booleans[x]:
            string1+=": ON"
        else:
            string1+=": OFF"
        strings.append(string1)
    f=open("Output.txt","w")
    for x in strings:
        f.write(x+"\n")
    
def boolean(value):
    
    blah=value.split()
    power=int(blah[0])
    base=int(blah[1])+1
    return base%2**power==0
    


if __name__ == "__main__":
    main()


