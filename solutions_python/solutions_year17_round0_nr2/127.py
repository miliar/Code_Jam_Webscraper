import sys, copy;
def tidy(n):
    s=str(n);
    for i in range(0,len(s)-1):
        if int(s[i])>int(s[i+1]):
            return False;
    return True;
def solve(n):
    s=str(n)[::-1]
    #print s;
    s=list(s);
    for i in range(0,len(s)):
        if tidy(n):
            return n;
        #print int(s[i])
        #print (int(s[i])+1)*10**i;
        n-=(int(s[i])+1)*10**i;
        s=str(n)[::-1];
        #print s;
        s=list(s);
    
    return "error";

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    #print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n = int(f.readline())
        file.write(str(solve(n)) + "\n")
file.close()            








