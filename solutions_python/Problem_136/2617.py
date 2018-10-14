def Parsefloat(s):
    C= float(s[0:s.find(' ')])
    s=s[s.find(' ')+1:]
    F= float(s[0:s.find(' ')])
    s=s[s.find(' ')+1:]
    X=float(s)
    return [C,F,X]

def main():
    inputfile=open("B-large.in","r+")
    outputfile=open("f0.txt","wb")
    num_test=int(inputfile.readline())
    for t in range(num_test):
        line=inputfile.readline()
        [C0,F0,X0]=Parsefloat(line)
        speed=2
        time=0
        while ((X0-C0)/speed)>(X0/(speed+F0)):
            time += C0/speed
            speed += F0
        time += X0/speed
        outputfile.write("Case #"+`t+1`+": "+`time`+"\n")
    outputfile.close() 
    
    
if __name__=="__main__":
    main()


