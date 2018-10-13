#!/usr/bin/python
import sys,os


def solve(farmPrice, farmRate, goal):
    """Returns a string result to one case of a problem"""
    cookies = 0.0
    cps = 2.0
    time = 0.0
    if(goal <= farmPrice):
        return "%.7f" % (goal / cps)


    while(shouldBuyAnotherFarm(goal, cps, farmPrice, farmRate)):
        time += workTime(farmPrice,cps)
        cookies = 0 # bought a farm
        cps += farmRate # add farm production rate
    time += workTime(goal - cookies, cps)
    return "%.7f" % time


def workTime(goal, cps):
    return goal / cps # return how long it would take to produce

def shouldBuyAnotherFarm(goal, cps, farmPrice,farmRate):
    return workTime(goal, cps + farmRate) < workTime(goal - farmPrice, cps)

#Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        
        cases = int(f_in.readline().strip())
        for case in range(1,cases+1):
            #Get input data
            inC, inF, inX = [float(x) for x in f_in.readline().strip().split()]
            #Solve and output
            print("Case #{}: {}".format(case, solve(inC, inF, inX)))
    
if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '"+str(sys.argv[1])+"' does not exist!"
    else:
        print "No file supplied! Run program this way: '"+str(sys.argv[0])+" something.in'"
        
