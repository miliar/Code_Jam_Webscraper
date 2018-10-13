file = open("c:/CodeJam/problemA/A-large.in")
line = file.next()

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    Case = file.next().split()
    ## Max Shyness:  0 <= Smax <= 1000
    Smax=int(Case[0])
    ## Number of People with each level of shyness:  length= 1+Smax
    Sindex = Case[1]

    ## Number of People Standing
    Scurrent=0
    ## Number of additional people needed
    Sextra=0
    for i in range(Smax+1):
        Si=int(Sindex[i])

        if Scurrent+Sextra >= i:
            Sextra+=0
            Scurrent+=Si
            ##print('Sextra={}  Scurrent={}'.format(Sextra,Scurrent))
        else:
            Sextra+= i-(Scurrent+Sextra)
            Scurrent+=Si

    
    print('Case #{}: {}'.format(testcase+1,Sextra))
           
        
        
        
    

    
    

