import math

def isPalindrome(x):
    if x == '':
        return True
    if x[0]==x[-1]:
        return isPalindrome(x[1:-1])
    else:
        return False
        
def findOcurs(x,y):
    numocurs = 0
    for i in xrange(x,y+1):
        sqi = math.sqrt(i)
        if not isPalindrome(str(i)):
            continue
        for j in xrange(1,int(sqi)+1):
            if j*j==i:
                if isPalindrome(str(j)):
                    numocurs+=1
                break
    return numocurs
    
if __name__ == '__main__':
    case = 1
    infile = open('C:\\Users\\Fly\\Downloads\\C-small-attempt0.in','r')
    outfile = open('C:\\Users\\Fly\\Downloads\\probC_out.txt','w')
    infile.readline()
    for line in infile:
        templine = line.split(' ')
        outfile.write('{0}{1}: {2}\n'.format('Case #',case,str(findOcurs(int(templine[0]),int(templine[1])))))
        case+=1
    infile.close()
    outfile.close()