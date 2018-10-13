import math

def isPalindrome(number):
    number = str(number)
    return (number == number[::-1])




# Qualification round
inp = open("input.txt")
outp = open("output.txt","w")

CASES = int(inp.readline())

for case in range(CASES):
    count = 0
    interval = inp.readline().split()
    for i in range(int(interval[0]),int(interval[1])+1):
        number = i
        if isPalindrome(number):
            number = math.sqrt(number)
            if (number - int(number)) == 0:
                if isPalindrome(int(number)):
                    count += 1
            
    outp.write("Case #%s: %s\n" % (case+1,count)) 
    
           
inp.close()
outp.close()