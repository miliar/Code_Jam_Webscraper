## code by Jozik (Karolis Ramanauskas)
import time
import math

def result(i):
    x, y = [int(a) for a in i.split()]
    res = ''
    if x > 0:
        res += 'WE'*x
    else:
        res += 'EW'*abs(x)
    if y > 0:
        res += 'SN'*y
    else:
        res += 'NS'*abs(y)
    return res

def main():     
    start_time = time.time()

##    f = open("sample.txt")
##    ff = open("out_sample.txt", "w")
##    f = open("test.txt")
##    ff = open("out_test.txt", "w")
    f = open("B-small-attempt0.in")
    ff = open("out_small.txt", "w")
##    f = open("B-large.in")
##    ff = open("out_large.txt", "w")

    N = int(f.readline())
    ins = []
    for i in range(N):
        ins.append(f.readline().replace("\n", ""))

    #temp to check if inputs are correctly read:
    print N
    print ins


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
