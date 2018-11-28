#problem1


def problem1(fileName):
    f = open(fileName,'r')
    testNum = int( f.readline())


    output = open("Output.txt",'w')
    
    for i in range(testNum):
        t = f.readline().split()
        s = list(t[0])
        length = int(t[1])


        impossible = False
        c = 0
        for ii in range(len(s)):
            if s[ii] == '-':
                if ii+length> len(s) :
                    impossible = True
                else:
                    for index in range(length):
                        if s[ii+index] == '-':
                            s[ii+index] = '+'
                        elif s[ii+index] == '+':
                            s[ii+index] = '-'
                    c+=1
                    
        if impossible:
            output.write("Case #"+ str(i+1) +": IMPOSSIBLE")
        else:
            output.write("Case #"+ str(i+1) +": "+str(c))
        output.write("\n")
        

problem1("A-large.in.txt")
print("Complete")
