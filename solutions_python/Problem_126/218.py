## code by Jozik (Karolis Ramanauskas)
import time
import math

def result(i):
    word, num = i.split()
    num = int(num)
    vow = 'aeiou'
    cons = 'qwrtypsdfghjklzxcvbnm'
    starts = [] # where num cons starts
    for j in range(len(word)-num+1):
        count = 0
        for k in range(num):
            if word[k+j] in cons:
                count += 1
            if count == num:
                starts.append(j)

    res = 0
    for s in range(len(starts)):
        if s == len(starts)-1: # einam iki galo
            res += 1 + starts[s] + (len(word) - num - starts[s]) + starts[s]*(len(word) - num - starts[s])
        else: # einam iki sekancio starto
            res += 1 + starts[s] + (starts[s+1] - num - starts[s] + (num-1)) + starts[s]*(starts[s+1] - num - starts[s] + (num-1))
            
    return res
    
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
