file = open("c:/CodeJam/2017/Qualifier/B-large.in")
line = file.readline()

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    # N = Max Value Counted to
    Nstring0 = file.readline()
    #print('Nstring0= '+Nstring0)
    Nstring = Nstring0[0:-1]
    N=int(Nstring)    
    Nstring = Nstring[::-1]
    #print('Nstring = '+ Nstring)
    
    #print('N='+str(N))
    Narray=[]
    tidynumber='notset'
    istidy=0
    tidyposition=0
    
    if (len(Nstring))==1:
        tidynumber=N

    else:
        for i in range(len(Nstring)-1):
            if len(Nstring)-1>= i+1:                
                if int(Nstring[i])>= int(Nstring[i+1]):
                    tidyposition+=1
                elif int(Nstring[i])< int(Nstring[i+1]):
                    #print('untidy!')
                    #print('Nstring[i]= '+Nstring[i]+' < '+'Nstring[i+1]= '+Nstring[i+1])
                    untidydigitsreversed= Nstring[0:i+1]
                    untidydigits= untidydigitsreversed[::-1]
                    subtractor= int(untidydigits)+1
                    N = N-subtractor
                    Nstring=str(N)
                    Nstring=Nstring[::-1]              
                    
        tidynumber=N
    
    print('Case #{}: {}'.format(testcase+1,str(tidynumber)))
           
file.close() 
        
        
    

    
    

