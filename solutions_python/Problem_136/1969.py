with open("B-large.in", "rt") as in_file:
    with open("out.txt", "wt") as out_file:
        runs = in_file.readline()
        runs = int(runs)
        for run in range(1,(runs+1)):
            inputString=in_file.readline()
            farmCost,farmRate,winCount=[float(i) for i in inputString.split(' ')]
            time=0
            currentRate=2
            while 1==1:
                winTime=time+(winCount)/currentRate
                farmTime=time+(farmCost)/currentRate
                newWinTime=farmTime+(winCount)/(currentRate+farmRate)
                if newWinTime<winTime:
                    time=farmTime
                    currentRate=currentRate+farmRate
                else:
                    
                    break
            out_file.write("Case #"+str(run)+": "+str(winTime)+"\n")
            print("Case #"+str(run)+": "+str(winTime))
