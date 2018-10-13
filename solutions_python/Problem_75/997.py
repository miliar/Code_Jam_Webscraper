f = open("B-large.in",'r')
fw = open('b-large_out.txt','w')

N = int(f.readline())

for case in range(1,N+1):
    
    combinations = {}
    oppose = {}
    
    l = f.readline()
    
    ls = l.split()
    
    combos = int(ls[0])
    c_index = []
    o_index = []
    print('Case %i.' % case)    
    for combo in range(1,combos+1):
        e1 = ls[combo][0]
        e2 = ls[combo][1]
        er = ls[combo][2]
           
        if e1 > e2:
            if combinations.has_key(e2):
                c_item = combinations[e2]
                c_item[e1] = er
                combinations[e2]=c_item
            else:
                c_item = {}
                c_item[e1] = er
                combinations[e2]=c_item
                  
        else:
            if combinations.has_key(e1):
                c_item = combinations[e1]
                c_item[e2] = er
                combinations[e1]=c_item
            else:
                c_item = {}
                c_item[e2] = er
                combinations[e1]=c_item

    opps = int(ls[combos+1])
  
    for opp in range(combos+2,combos+2+opps):
        e1 = ls[opp][0]
        er = ls[opp][1]

        if oppose.has_key(er):
            o_item = oppose[er]
            o_item.append(e1)
            oppose[er]=o_item
        else:
            o_item = []
            o_item.append(e1)
            oppose[er]=o_item
  
        if oppose.has_key(e1):
            o_item = oppose[e1]
            o_item.append(er)
            oppose[e1]=o_item
        else:
            o_item = []
            o_item.append(er)
            oppose[e1]=o_item
    
    st = ls[combos+3+opps]
    outstr = ''
    l_index = {}

    for cursor in range(0,len(st)):
        cl = st[cursor]
      
        if len(outstr) == 0:
            outstr = cl
            continue
            
        ll = outstr[len(outstr)-1]
        const_happened = 0
        dest_happened = 0
     
        if cl > ll:

            if combinations.has_key(ll):
                c_item = combinations[ll]
                if c_item.has_key(cl):
                    outstr = outstr[:len(outstr)-1] + c_item[cl]
                    const_happened = 1
        else:
            if combinations.has_key(cl):
                c_item = combinations[cl]
                if c_item.has_key(ll):
                    outstr = outstr[:len(outstr)-1] + c_item[ll]
                    const_happened = 1
                
        found_dest = 0
        if const_happened == 0:
            if oppose.has_key(cl):
                rmost = 0
                for dlet in oppose[cl]:
                    if dlet in outstr:
                        found_dest = 1
                        dlet_loc = outstr.rfind(dlet)
                        if dlet_loc > rmost:
                            rmost = dlet_loc

            if found_dest == 1:
                dest_happened =1
                outstr = ''
        if const_happened == 0 and dest_happened == 0:
            outstr = outstr + cl
    
    print outstr
    fw.write('Case #%i: [' % case)    
    
    f_str = ''
    
    for o_let in outstr:
        f_str = f_str + o_let + ', '
        
    f_str = f_str[:len(f_str)-2]
    
    fw.write(f_str+']\n')
    








f.close()
fw.close()

