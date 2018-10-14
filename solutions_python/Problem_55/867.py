data = open("data.txt","rU")
out = open("small.out","w")
cases = int(data.readline())

for i in range(cases):
    rides,size,no_groups = data.readline().split()
    #print rides,size,no_groups
    groups = data.readline().split(" ")
    groups = [int(k) for k in groups]
    #print "groups",groups
    #print
    money = 0
    for c in range(int(rides)):
        filling = True
        curr_size = int(size)
        temp = []
        while filling:
            if len(groups) > 0 and groups[0] <= curr_size:
                rider = groups.pop(0)
                curr_size -= rider
                temp.append(rider)
                money += rider
            else:
                filling = False
        groups = groups+temp
        #print groups
    out.write("Case #%s: %s \n" %(i+1,money))
    out.flush()
out.close()
