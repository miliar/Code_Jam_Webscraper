fin = open("B-large.in","r")
fout = open("cookie_output","w")
inp = fin.readline
out = fout.write

t = int(inp())
for case in xrange(1,t+1):
    c,f,x = map(float,inp().split())
    buyFarm = True
    tp = 0.0
    speed = 2.0
    while buyFarm:
        if x-c > 0.0000001:
            tp += c/speed
            buy_time = (x/(speed+f)) + tp
            no_buy_time = ((x-c)/speed) + tp
            '''
            print tp
            print buy_time
            print no_buy_time
            print "****************"
            '''
            if  buy_time < no_buy_time:
                speed += f
            else:
                tp = no_buy_time
                buyFarm = False
        else:
            tp += x/speed
            buyFarm = False
    out("Case #"+str(case)+": "+'{0:.7f}'.format(tp)+"\n")
fin.close()
fout.close()
