import sys

def main(argv):    
    f = open('/home/saba/Documents/codejam/in2.txt', 'r')
    f.readline() #dont want number
    fo = open('/home/saba/Documents/codejam/out2.txt', 'w')
    num = 1
    for line in f:
        fo.write("Case #%d: " % num)
        totals = line.split(" ")
        for i in range(len(totals)):
            totals[i] = int(totals[i])
        n = totals[0]
        s = totals[1]
        sCount = 0
        pCount = 0
        p = totals[2]
        totals = totals[3:]
        for i in range(len(totals)):
            r = totals[i] % 3
            if(r == 0):
                score = totals[i]/3
                if(score >= p):
                    pCount += 1
                elif(score+1 == p and sCount < s and score != 0):
                    pCount += 1
                    sCount += 1
            elif(r == 1):
                maxScore = (totals[i] - 1)/3 + 1
                if (maxScore >= p):
                    pCount += 1
            elif(r == 2):
                score = (totals[i] - 2)/3 + 1
                if (score >= p):
                    pCount += 1
                elif(score+1 == p and sCount < s):
                    pCount += 1
                    sCount += 1
        fo.write("%d\n" % pCount)
        num += 1
    f.close()
    fo.close()
                
             

if __name__ == "__main__":
    main(sys.argv[1:])
