def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("B-large.out", "w")
        
    for tc in xrange(T):
        C, F, X = [float(x) for x in input_file.readline().replace('\n','').split(' ')]
        inc = 2.0
        totTime = 0.0
        if X <= C:
            totTime = X/inc
        else:
            while (C/inc + X/(inc+F)) < (X/inc):
                totTime = totTime + C/inc
                #print totTime, inc
                inc = inc+F                    
                
            totTime = totTime + X/inc
            #print totTime, inc
        
        output_file.write("Case #"+str(tc+1)+": " + str(totTime) + "\n")
        
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
