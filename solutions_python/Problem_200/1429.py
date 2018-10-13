def tidy(N):
    string = str(N)
    for i in range(len(string)-1):
        if string[i] > string[i+1]:
            j = i
            while(j>0):
                if int(string[j])-1 >= int(string[j-1]):
                    break;
                j-=1
            string = string[:j] + str(int(string[j])-1) + '9'*(len(string)-j-1)
            break
    return int(string)
            

def f(inFile,outFile):
    T = int(inFile.readline())
    for i in range(T):
        N = int(inFile.readline())
        maxTidy = tidy(N)
        outFile.write("Case #" + str(i+1) + ": " + str(maxTidy) + "\n")


inFile = open("C:/Users/USER/Downloads/B-large.in","r")
outFile = open("C:/Users/USER/Downloads/B-large.out","w")
f(inFile,outFile)
inFile.close()
outFile.close()
