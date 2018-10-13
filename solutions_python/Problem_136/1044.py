def cookieclicker(f):
    T = int(f.readline())
    testcase = 0
    while testcase < T:
        values = f.readline().split()
        C,F,X = float(values[0]), float(values[1]), float(values[2])
        cookie_earning = 2.0
        current_time = X / cookie_earning
        reach_time = 0.0
        
        while True:
            next_time = reach_time + (C / cookie_earning) + (X / (cookie_earning + F))
            if (current_time < next_time):
                break
            else:
                reach_time += C / cookie_earning
                cookie_earning += F
                current_time = next_time
        
        decision = "Case #" + str(testcase+1) + ": " + str(current_time)
        print decision
        
        output = open('largesetoutput','a')
        output.write(decision+"\n")
        output.close
        
        testcase += 1
    
    
      
    

f = open('B-large.in')
cookieclicker(f)