f=open('A-small-attempt0.in','r')
out=open('output.txt', 'w+')
c=0
u=1
lis=[]
for line in f:
    #print line
    ct = 0
    if c==0:
        tc = int(line)
        c=c+1
        continue
    else:
        inp = line
        #print inp
        k = int(inp.split(" ")[1])
        s = list(inp.split(" ")[0])
        global count
        def flip(lis, f, count = 0):
            try:
                i = lis.index("-")
                temp = lis[i:]
                #print temp
                if len(temp) < f:
                    return "IMPOSSIBLE"
                else:
                    for j in range(f):
                        if temp[j] == "-": 
                            temp[j] = "+"
                        else: 
                            temp[j] = "-"

                count +=1
                #print count
                if len(temp) != 0 :
                    return flip(temp, f, count)
                else:
                    return count
            except:
                return count
        x = flip(s, k)
        x = str(x)
        x = x + "\n"
        j = "Case #{}: {}".format(u, x)
        out.write(j)
        u+=1
        lis.append(j)

f.close()
out.close()



'''def test(x = [1,2,3,4,5]):
	print x.pop(0)
	print x
	if len(x) == 0:
		return 0
	else: 
		return test(x)'''

#test(x = [1,2,3,4,5])

