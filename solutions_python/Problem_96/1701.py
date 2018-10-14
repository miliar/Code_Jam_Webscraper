import sys

maxMap = {30:(10,0),29:(10,0),28:(10,0),27:(10,1),26:(10,1),25:(9,0),
       24:(9,1),23:(9,1),22:(8,0),21:(8,1),20:(8,1),19:(7,0),18:(7,1),
       17:(7,1),16:(6,0),15:(6,1),14:(6,1),13:(5,0),12:(5,1),11:(5,1),
       10:(4,0),9:(4,1),8:(4,1),7:(3,0),6:(3,1),5:(3,1),4:(2,0),3:(2,1),
       2:(2,1),1:(1,0),0:(0,0)
       }

minMap = {30:(10,0),29:(10,0),28:(10,0),27:(9,0),26:(9,0),25:(9,0),
       24:(8,0),23:(8,0),22:(8,0),21:(7,0),20:(7,0),19:(7,0),18:(6,0),
       17:(6,0),16:(6,0),15:(5,0),14:(5,0),13:(5,0),12:(4,0),11:(4,0),
       10:(4,0),9:(3,0),8:(3,0),7:(3,0),6:(2,0),5:(2,0),4:(2,0),3:(1,0),
       2:(1,0),1:(1,0),0:(0,0)
       }    

def optimize(testCaseNumber,triplets,surprises,bestResult):
    remainingSurprises = surprises
    count = 0
    for i  in range(0,len(triplets)):
        triplet = triplets[i]
        result = ()
#        print "remaining: %d" % (remainingSurprises)
        result=minMap[triplet]
        if(bestResult <= result[0]):
            if(i==len(triplets)-1):
                result = maxMap[triplet]
            count +=1
            remainingSurprises -= result[1]
           # print "min branch count: %d"%count
        else:
            if(remainingSurprises > 0):
                result = maxMap[triplet]
                if(bestResult <= result[0]):
                    count +=1
                    remainingSurprises -= result[1]
                else:
                    result = minMap[triplet]
            else:
                result = minMap[triplet]
            #print "max branch count: %d"%count
        #print "result: (%d,%d)"% (result)
    print "Case #%d: %d"%(testCaseNumber,count)
 #       print "remaining: %d" % (remainingSurprises)    
        


def main(numTestCases,testCases):
    #print "Num TestCases: %d"%numTestCases
    for i in range(0, len(testCases)):
        testCase = testCases[i]
        numbers = testCase.split(' ')
        googlers=int(numbers[0])
        surprises=int(numbers[1])
        bestResult=int(numbers[2])
        triplets=map(int,numbers[3:])
        triplets.sort()
        #print "%d,%d,%d,%s"%(googlers,surprises,bestResult,triplets)
        optimize(i+1,triplets,surprises,bestResult)

if __name__ == '__main__':
    if(len(sys.argv)==2):
        f = open(sys.argv[1],'r').readlines();
        f = [i.replace('\n','') for i in f]
        numTestCases = int(f[0])
        testCases = f[1:]
        main(numTestCases,testCases)



    else:
        print "Usage: python "+sys.argv[0]+" filename"
