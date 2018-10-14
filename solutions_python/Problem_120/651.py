## code by Jozik (Karolis Ramanauskas)
import time
import math

def result(pair):
    r = int(pair.split()[0])
    t = int(pair.split()[1])  
    return int(math.floor(  (-(2*r-1) + math.sqrt((2*r-1)**2+4.0*2*t) ) /4.0))

    
def main():     
    start_time = time.time()

##    f = open("sample.txt")
##    ff = open("out_sample.txt", "w")
##    f = open("test.txt")
##    ff = open("out_test.txt", "w")
    f = open("A-small-attempt0.in")
    ff = open("out_small.txt", "w")
##    f = open("A-large.in")
##    ff = open("out_large.txt", "w")

    N = int(f.readline())
    ins = []
    for i in range(N):
        ins.append(f.readline().replace("\n", ""))

    #temp to check if inputs are correctly read:
##    print N
##    print ins
##    print math.sqrt(10**18)
    


    #print output:
    c=1
    for i in ins:
        sol = str(result(i))
        print "Case #" + str(c) + ": " + sol
        ff.write("Case #" + str(c) + ": " + sol + "\n")
        c+=1

    print "time: " + str(round(time.time()-start_time,2)) + "s"
    f.close()
    ff.close()

main()
