import math

def main():
    input1 = open('input1.txt', 'r')
    output1 = open('output1.txt', 'w')

    T = int(input1.readline())      #number of test cases
    
    for casenum in xrange(1, T + 1):
        line = input1.readline().strip(' ').split(' ')
        X = int(line[0])
        R = int(line[1])
        C = int(line[2])
        
        if(((R*C) % X) != 0):
            ans = 'R'
        else:
            if(X == 1):
                ans = 'G'
            elif(X == 2):
                ans = 'G'
            elif(X == 3):
                if(R*C == 3):
                    ans = 'R'
                else:
                    ans = 'G'
            elif(X == 4):
                if((R*C == 4) or (R*C == 8)):
                    ans = 'R'
                else:
                    ans = 'G'
        
        if(ans == 'R'):
            ans = 'RICHARD'
        else:
            ans = 'GABRIEL'
        outstr = 'Case #' + str(casenum) + ': '
        outstr += ans
        outstr += '\n'
        output1.write(outstr)
        
    input1.close()
    output1.close()
  
    
    
main()