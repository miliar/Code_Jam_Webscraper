case = int(raw_input())
for t in range(1,case+1):
    x = raw_input().split()
    can = False
    if(0 < int(x[2]) < 100 or int(x[2]) == int(x[1])):
        for i in range(int(x[0])+1):
            for j in range(max(1,i),int(x[0])+1):
                if(float(i)*100/float(j) == int(x[1])):
                    can = True
    if(can):
        print 'Case #' + str(t) + ': Possible'
    else:
        print 'Case #' + str(t) + ': Broken'
