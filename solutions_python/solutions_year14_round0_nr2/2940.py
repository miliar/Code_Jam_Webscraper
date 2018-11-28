import sys

def cookie(c,f,x):
#    print "c={},f={},x={}".format(c,f,x)
    income = 2.0
#    nfarms = 0
    time = 0

    while x/income > c/(income) + x/(income + f):
        time = time + c/income
#        nfarms = nfarms + 1
        income = income + f
#        print "nfarms = {}, income = {}, time = {}".format(nfarms,income, time)
#        print ">> cond: {} > {} + {}".format(x/income,c/(income),x/(income + f))
        
    time = time + x/income
    return time

def main():
    with open(sys.argv[1]) as infile:
        ntests = int(infile.readline())
        for i in range(1,ntests+1):
            c,f,x = map(float,infile.readline().split())
            time = cookie(c,f,x)
            print "Case #{}: {:.7f}".format(i,time)

main()
