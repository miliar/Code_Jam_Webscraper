tc = input()
for i in range(0,tc):
    inp = raw_input()
    inp_list = inp.split()
    si_str = inp_list[1]
    si_list = list(si_str)
    si_list = map(int,si_list)
    total = 0
    add_ppl = 0
    for x in range(0,(int(inp_list[0])+1)):
        if(x>total and si_list[x]):
            add_ppl += (x-total)
            total = x+si_list[x]
        else:
            total += si_list[x]
    print "Case #"+str(i+1)+": "+ str(add_ppl)