## code by Jozik (Karolis Ramanauskas)
import time
import math

def result(inpp):
    inpp = [int(i) for i in inpp.split()]
    res = ''
    for i in inpp:
        inp = i
##        print inp
        while inp > 1:
            if inp%5 == 0:# and '5' not in res:
                res += '5'
                inp /= 5
            elif inp%4 == 0:# and '4' not in res:
                res += '4'
                inp /= 4
            elif inp%3 == 0:# and '3' not in res:
                res += '3'
                inp /= 3
            elif inp%2 == 0:# and '2' not in res:
                res += '2'
                inp /= 2
        if len(res)>3:
            return res[:3]
    return res+(3-len(res))*'2'
            
            
    print inp

def main():     
    start_time = time.time()

##    f = open("sample.txt")
##    ff = open("out_sample.txt", "w")
##    f = open("test.txt")
##    ff = open("out_test.txt", "w")
    f = open("C-small-1-attempt0.in")
    ff = open("out_small.txt", "w")
##    f = open("A-large.in")
##    ff = open("out_large.txt", "w")

    T = int(f.readline())
    params = f.readline().replace("\n", "")
    R = int(params.split()[0])
    N = int(params.split()[1])
    M = int(params.split()[2])
    K = int(params.split()[3])
    ins = []
    for i in range(R):
        ins.append(f.readline().replace("\n", ""))

    #temp to check if inputs are correctly read:
    print T
    print R, N, M, K
    print params
    print ins


    #print output:
    c=1
    print "Case #1:"
    ff.write("Case #1:" + "\n")
    
    for i in ins:
        sol = str(result(i))
        print sol
        ff.write(sol + "\n")
        c+=1

    print "time: " + str(round(time.time()-start_time,2)) + "s"
    f.close()
    ff.close()

main()
