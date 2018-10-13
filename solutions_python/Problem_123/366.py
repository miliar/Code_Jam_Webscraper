## code by Jozik (Karolis Ramanauskas)
import time
import math

def result(armin_size, motes):
    count = 0
    min_count = len(motes)
    motes=[int(a) for a in motes.split()]
    motes.sort()
    while motes<>[]:
        # eat all small shit:
        ate = False
        for i in motes:
            if i<armin_size:
                armin_size+=i
                ate = True
                motes.remove(i)
##                print "a", armin_size, motes
        min_count = min(min_count, count+len(motes))
        if ate == False: # didn't eat anything
            if armin_size > 1:
                motes.append(armin_size-1)
            else:
                motes.remove(max(motes))
            count += 1
##            print "b", armin_size, motes
##    print armin_size, motes, count
    return min_count
        
    

def main():     
    start_time = time.time()

##    f = open("sample.txt")
##    ff = open("out_sample.txt", "w")
##    f = open("test.txt")
##    ff = open("out_test.txt", "w")
##    f = open("A-small-attempt2.in")
##    ff = open("out_small.txt", "w")
    f = open("A-large.in")
    ff = open("out_large.txt", "w")

    T = int(f.readline())
    ins = []
    armin_size = []
    for i in range(T):
        in1 = f.readline().replace("\n", "")
        armin_size.append(int(in1.split()[0]))
        ins.append(f.readline().replace("\n", ""))

    #temp to check if inputs are correctly read:
##    print T
##    print armin_size
##    print ins


    #print output:
    c=1
    for i in range(len(ins)):
        sol = str(result(armin_size[i], ins[i]))
##        print armin_size[i], ins[i]
        print "Case #" + str(c) + ": " + sol
        ff.write("Case #" + str(c) + ": " + sol + "\n")
        c+=1

    print "time: " + str(round(time.time()-start_time,2)) + "s"
    f.close()
    ff.close()

main()
