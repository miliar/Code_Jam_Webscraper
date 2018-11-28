infile = open('D:\study\codejam\codejam2014\B-large.in','r')
outfile = open('D:\study\codejam\codejam2014\B-large.out','w')
def main():
    T = int(infile.readline())
    for case in range(1,T+1):
        doCase(case)
    infile.close()
    outfile.close()

def doCase(case):
    c,f,x = [float(x) for x in infile.readline().split()]
    outfile.write('Case #'+str(case)+': '+str(check(c,f,x))+'\n')
    #print('case #'+str(case)+' '+str(check(c,f,x)))    

def check(c,f,x):
    rate = 2
    time1 = 0
    while x/(rate+f)+c/rate < x/rate:
        time1 += c/rate
        rate += f
    time = time1+x/rate
    return round(time,7)
