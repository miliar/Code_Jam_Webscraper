import sys

def main():
    fin = open(sys.argv[1])

    cases = int(fin.readline().strip())
    for case in range(cases):
        line = fin.readline().strip().split()
        
        farm_cost = float(line[0])
        farm_rate = float(line[1])
        target = float(line[2])
        
        rate = 2.0
        time = 0
        
        if farm_cost >= target:
            time = target / rate
        else:
            while 1:
                time += farm_cost / rate
                
                time_with_farm = target / (rate + farm_rate)
                time_without_farm = (target - farm_cost) / rate
                
                if time_without_farm <= time_with_farm:
                    time += time_without_farm
                    break
                else:
                    rate += farm_rate
        
        print "Case #%d: %.7f" % (case + 1, time)
        

if __name__ == "__main__":
    main()
