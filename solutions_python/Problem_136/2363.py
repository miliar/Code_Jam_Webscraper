
N = 0 #total test cases

with open("output.txt", 'w') as output:
        
    with open("B-large.in") as inp:
        N = inp.readline()
        N = int(N)

        for i in range(0, N):
            val = inp.readline()
            C, F, X = val.split(" ")
            C = float(C)
            F = float(F)
            X = float(X)
            
            cookieGen = 2
            minTime = X / cookieGen
            farmCost = 0.0
            
            while 1:
                farmCost = farmCost + (C/cookieGen)
                cookieGen = cookieGen + F

                targetCost = (X / cookieGen) + farmCost

                if targetCost < minTime:
                    minTime = targetCost
                else:
                    output.write("Case #"+str(i+1)+": "+str(minTime)+"\n")
                    break;
