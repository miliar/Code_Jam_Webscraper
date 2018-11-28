with open('outputB.txt','w') as o:
    with open('B-small-attempt0.in','r') as f:
        lines = f.readlines()
        T = int(lines[0])
        for Tnum in range(1,T+1):
            values = lines[Tnum].split()
            C=float(values[0])
            F=float(values[1])
            X=float(values[2])

            besttime = X
            time = X/2
            numFarms = 0
            while time < besttime:
                besttime = time
                numFarms += 1
                rate = 2
                time = 0

                for farm in range(0,numFarms):
                    time += C/rate
                    rate += F

                time += X/rate

            o.write('Case #' + str(Tnum) + ': ' + '{0:.7f}\n'.format(besttime))


            
        
