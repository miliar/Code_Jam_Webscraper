import math

def isPalindrome(num):
    n = str(num)
    return (n == n[::-1])

def generatePalindromes(low,high):
    count = 0
    #print('range: '+ str(low)+' '+str(high))
    for i in range(low,high+1):
        if math.sqrt(i).is_integer():
            # print('Candidate: '+str(i))
            # print('isPalindrome: '+str(isPalindrome(int(math.sqrt(i)))))
            if(isPalindrome(i) and isPalindrome(int(math.sqrt(i)))):                
                count+=1

    return count

def readRange(f):
    line = f.readline()
    line.split()
    
    

if __name__ == "__main__":
    
    f = open('input.txt','r')
    numCases = int(f.readline())

    i = 1
    f2 = open('output.txt','w')
    while(i <= numCases):
    #while(i <= 1):
        line = f.readline()
        r = line.split()

        count = generatePalindromes(int(r[0]),int(r[1]))
        #print('Case #'+str(i)+": "+str(count)+"\n")
        f2.write('Case #'+str(i)+": "+str(count)+"\n")

        i+=1
        

    f.close()
    f2.close()
        
    
