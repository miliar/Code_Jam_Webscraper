from pprint import pprint

def p2d(tab):
    for e in tab:
        print(e)

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)
    
    for test in range(N):
        total = 0
        line = fin.readline().replace("\n", "")
        l = line.split(" ")
        
        pprint(l)
        c = 0
        
        com = {}
        opp = {}
        bas = ""
        elm = []
        
        i = 0
        while True:
            for j in xrange(int(l[i])):
                if c == 0:
                    tmp = l[i+j+1]
                    com[tmp[:-1]] = tmp[-1:]
                    com[tmp[:-1][1] + tmp[:-1][0]] = tmp[-1:]
                elif c == 1:
                    tmp = l[i+j+1]
                    opp[tmp[:-1]] = tmp[-1:]
                    opp[tmp[-1:]] = tmp[:-1]
                else:
                    #elm = [x for x in l[i+1]]
                    #elm.reverse()
                    #elm = "".join(elm)
                    bas = l[i+1]
                    break
            i += int(l[i]) + 1
            c += 1
            if len(bas) > 0:
                break
          
        #pprint(com)
        #pprint(opp)
        #pprint(bas)
        #print 
        
        i = 0
        while True:
            elm += bas[i]
            #print "ELM: ", elm
            proceed = True
            
            while proceed:
                if len(elm) >= 2:
                    clast = com.get("".join(elm[-2:]), None)
                    #print "CLAST: ", clast
                    if clast is not None:
                        elm.pop()
                        elm.pop()
                        elm.append(clast)                                        
                        print elm 
                    else:
                        ops = opp.get(elm[len(elm)-1], None)
                        if ops is not None and ops in elm:
                            elm = []
                        proceed = False
                else: 
                    proceed = False                                          
                        
            bas = bas[1:]
            if len(bas) == 0:
                break
        
        print elm

        total = str([x for x in elm]).replace("'", "")

        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)
