fin = open ('B-large.in','r')
fout = open('CJAM2OUT.txt','w')

T = int(fin.readline().strip())

for i in range(T):    
    C,F,X = list(map(float,fin.readline().strip().split()))
    rate = 2
    time = 0

    def check ():
        global rate, time
        wait = (X/rate)
        buy = (X/(rate+F)) + C/rate
        if wait < buy:
            time += wait
            return True
        else:
            #print (buy)
            time += C/rate
            rate += F
            return False

    soln = False

    while(soln==False):
        #print (rate)
        soln = check()

    print ('Case #', end = '', file = fout)
    print (i+1, end = '',file = fout)
    print (':','%.7f' % time,file = fout)

fout.close()
