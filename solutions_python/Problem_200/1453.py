### Set the input and output file names
import time
import datetime
import string
import operator

filename = 'B-large'
input_filename = filename + '.in'
output_filename = filename + '.out.' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S') + '.txt'

def oneoneone(x,i):
    temp = ""
    for count in range(0,x):
        temp = str(i) + temp
    return(temp)

def tidy(x):
    temp = True
    x_string = str(x)
    max_X = int(x_string[:1])
    for count in range(1,len(x_string)):
        if int(x_string[count:count+1]) < max_X:
            temp = False
        else:
            max_X = int(x_string[count:count+1])
    return temp
    
def myMinus(x):
    x_string = str(x)
    n = 1
    while int(x_string[-n:][0:1]) == int(x_string[-1:]) and n <= len(x_string):
        n = n + 1
    if int(x_string[-1:]) > 0:
        return ( x_string[:len(x_string)-n+1] + oneoneone(n-1,int(x_string[-1:])-1))
    else:
        return ( str(int(x_string[:len(x_string)-n+1])-1) + oneoneone(n-1,9))

def countLastRepeats(x):
    x_string = str(x)
    n = 1
    while int(x_string[-n:][0:1]) == int(x_string[-1:]) and n <= len(x_string):
        n = n + 1
    return n - 1
        
### Open input file for reading
with open(input_filename) as f:
    lines = f.read().splitlines()

    ### Open output file for writing
    with open(output_filename, 'w') as output:

        ######################################################
        ### Initialise variables from first line of the file
        ######################################################   
        vars = lines[0].split(' ')
        cases = int(vars[0])                    # number of cases
        print(str(cases) + ' cases detected.')  # [soft validation]
        lineNum = 1                             # first case starts here
        caseNum = 0                             # for counting the num of cases
        caseSize_r = 1                          # number of rows in each case; default = 1
        caseSize_c = 1                          # number of columns in each case; default = 1
        
        #infoLines = True                        # Toggle according to question
        infoLines = False                       # Toggle according to question
        
        ### i.e. infoLines == True
        if infoLines:
            output.write('NA')
        ### i.e. infoLines == False
        else:   
            for caseNum in range(1, cases+1):
                
                ### Do the Work!
                ### TODO! 
                N = int(lines[lineNum])
                N_string = str(N)
                N_len = len(N_string)
                #print "n_string %s" % N_string
                #print "n_len %d" % N_len
                if N <= 9:
                    myAns = N
                    
                elif N < int(oneoneone(N_len,1)):
                    myAns = int(oneoneone(N_len - 1, 9))
                    
                else:
                #compare consecutive digits.  Whilst the second is equal or greater to the first, move on
                #if not then deduct 1 from the first digit, and make the rest of the chain "9"s
                #eg 32xx -> 2999.   40 -> 39999.   [8]02-> [7]99
                    myAns = N
                    
                    for count in range(1,N_len+1):
                        if not tidy(N_string[:count]):
                            a = countLastRepeats(N_string[:count-1])
                            #print("a " + str(a))
                            #print(str(int(N_string[:count-a])-1))
                            #print(str(oneoneone(N_len-count+a,9)))
                            myAns = int(str(int(N_string[:count-a])-1) + str(oneoneone(N_len-count+a,9)))
                            break
                    

                
                #len(lines[lineNum])
                lineNum += 1
                
                ### Output myAns
                print('Case #%d: %d\n' % (caseNum, myAns))
                output.write('Case #%d: %d\n' % (caseNum, myAns))

                

### END
