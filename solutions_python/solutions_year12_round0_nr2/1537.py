I,O = open('input.txt','rU'),open('output.txt','w')
W,R = O.write,I.readline
I = open('input.txt','rU')
R = I.readline

tests = int(R())

for loop in range(tests):
    data = map(int,R().split())
    n = data[0] # number of Googlers
    s = data[1] # number of surprising triplets of scores
    p = data[2] # pass requirement
    scores = [data[i] for i in range(3,n+3)]
    greater = 0
    for score in scores:
        average = score//3
        remainder = score%3
        if average>=p:
            greater += 1
            print "1"
        elif remainder and average+1>=p:
            greater += 1
            print "2"
        elif s:
            if score>=2 and not remainder and average+1>=p:
                greater += 1
                s -= 1
                print "3"
            elif score>=2 and remainder==2 and average+2>=p:
                greater += 1
                s -= 1
                print "4"
        else:
            print "-"
    W('Case #%d: %s\n'%(loop+1,greater))

I.close()
O.close()