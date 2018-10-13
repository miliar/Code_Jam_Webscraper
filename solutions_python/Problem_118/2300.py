from math import sqrt

def is_palindrome(n):
    return str(n) == str(n)[::-1]

with open("C-small-attempt0.in","r") as fp:
    with open("ouput.out","w") as out:
        cases = fp.readline()
        
        for i in range(0,int(cases)):
            lines = fp.readline()
            lines = lines.split()
            acc=0
            
            for j in range(int(lines[0]),int(lines[1])+1):
                if(is_palindrome(str(int(j)))):
                    #Palindrome
                    square=sqrt(int(j))
                    if(square.is_integer()): 
                        #If is integer is square
                        if(is_palindrome(int(square))): 
                            #Palindrome of the square
                            acc+=1
                    
            out.write("Case #" + str(i+1) + ": " + str(acc) + "\n")