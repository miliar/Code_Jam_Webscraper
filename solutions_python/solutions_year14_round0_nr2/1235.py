def calculate(farms, F):
    return (farms*F) + 2

with open("B-large.in","r") as fp:
    with open("ouput2.out","w") as out:
        cases = fp.readline()
        
        for c in range(0,int(cases)):
            farms = 0;
            
            line = fp.readline()
            C = float(line.split(" ")[0])
            F = float(line.split(" ")[1])
            X = float(line.split(" ")[2])
                    
            now = X / calculate(farms,F)
            buy_farm = (C / calculate(farms,F))
            after = buy_farm + (X / calculate(farms+1,F))
                        
            if(after < now):
                time = buy_farm
            else:
                time = now
                        
            while (after < now):
                farms = farms + 1;
                now = X / calculate(farms,F)
                buy_farm = (C / calculate(farms,F))
                after = buy_farm + (X / calculate(farms+1,F))
                if(after < now):
                    time = time + buy_farm
                else:
                    time = time + now
                 
            #print(time)
            out.write("Case #" + str(c+1) + ": " + str(time) + "\n")
            