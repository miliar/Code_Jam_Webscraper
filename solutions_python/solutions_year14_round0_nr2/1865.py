with open("test.txt", "r") as file:
    with open("out.txt", "w") as outFile:
        t = int(file.readline())
        for i in range(1, t+1):
            g = file.readline().rstrip().split(" ")
            C = float(g[0])
            F = float(g[1])
            X = float(g[2])
            if (X <= C):
                outFile.write("Case #" + str(i) + ": " + str(X / 2) +"\n")
            else:
                cookiesPerSecond = 2.0
                time = 0
                exitLoop = True
                while (exitLoop):
                    #Calculate time to next farm
                    timeToF = C / cookiesPerSecond
                    time += timeToF

                    #Decide, if we want to purchase the farm or not, greedy
                    if ((X - C) / cookiesPerSecond < (X / (cookiesPerSecond + F))):
                        time += (X - C) / cookiesPerSecond
                        exitLoop = False
                    else:
                        cookiesPerSecond = cookiesPerSecond + F
                outFile.write("Case #" + str(i) + ": " + str(time) +"\n")


            
