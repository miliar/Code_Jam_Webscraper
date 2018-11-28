f = open('output.txt','w')
t = int(raw_input())
for kk in range(0,t):
    n = int(raw_input())
    st1 = raw_input()
    st2 = raw_input()
    l1 = len(st1)
    l2 = len(st2)
    ind1 = 0
    ind2 = 0
    ans = 0
    flag = 0
    while ind1 < l1 or ind2 < l2:
        if ind1 < l1 and ind2 < l2 and st1[ind1] == st2[ind2]:
	    ind1+=1
	    ind2+=1
            continue
	elif ind1 < l1 and ind2 > 0 and st1[ind1] == st2[ind2-1]:
	    ans += 1
	    ind1 += 1
            continue
	elif ind1 > 0 and ind2 < l2 and st1[ind1-1] == st2[ind2]:
	       ans += 1
	       ind2 += 1
	       continue
        else:
	    print "Fegla Won"
	    f.write("Case #"+str(kk+1)+": Fegla Won\n")
	    flag = 1
	    break
    if flag == 0:
	f.write("Case #"+str(kk+1)+": "+str(ans)+"\n")
        print ans        
f.close()
    
