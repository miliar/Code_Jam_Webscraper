

if __name__ == '__main__':
    T = int(raw_input().split()[0])

    for t in xrange(1,T+1):

        ##get inputs
        n = map(int,raw_input().split()[:1])[0]

        ws = []
        for i in range(0,n):
            ws.append(map(int, raw_input().split()))

        total=0

        for i in range(0,n):
            for j in range(i+1,n):
                if (ws[i][0] - ws[j][0]) * (ws[i][1] - ws[j][1]) <0:
                    total+=1
        
        


        print "Case #%d: %d" % (t,total)
