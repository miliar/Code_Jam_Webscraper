file=open('c:/Users/pihulic/Desktop/CODEJAM/B-large.in')

## Number of Cases
T=int(file.next().rstrip('\n'))

for x in range(T):

    CFX=file.next().split()
    ## Price of Cookie Farm
    C=float(CFX[0])
    ## Incremental Cookie Production Rate
    F=float(CFX[1])
    ## Target Score
    X=float(CFX[2])


    ## Baseline Production
    Production=2.0
    ## Time to Purchase additional Farm
    TimeToNextFarm=C/Production
    ## Time to Target Score
    TimeToX=X/Production
    ## Running List of 
    TimesToX=[TimeToX]
    ## Checks if To See Which is Faster: Winning or Getting Additional Farm
    while TimeToNextFarm < TimeToX:
        ## Checks if Winning or Winning with Additional Farm is Faster
        if ((TimeToNextFarm+X/(Production+F))) <TimeToX:
            Production+=F
            TimeToX=X/Production+TimeToNextFarm
            TimeToNextFarm+=C/Production
            ##print(str(TimeToX))
            TimesToX.append(TimeToX)
        else:
            
            break
        
    print('Case #'+str(x+1)+': ' + str(TimesToX[-1]))


    
    
