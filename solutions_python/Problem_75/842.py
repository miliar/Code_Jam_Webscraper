f = open("B-large.in",'r')
fw = open('b-large.txt','w')

#f = open('test.txt','r')
#fw = open('tst.txt','w')

N = int(f.readline())


for case in range(1,N+1):
    
    c = {}
    o = {}
    
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
           
        
        #compose list based on 
        if e1 > e2:
            if c.has_key(e2):
                c_item = c[e2]
                c_item[e1] = er
                c[e2]=c_item
            else:
                c_item = {}
                c_item[e1] = er
                c[e2]=c_item
                  
        else:
            if c.has_key(e1):
                c_item = c[e1]
                c_item[e2] = er
                c[e1]=c_item
            else:
                c_item = {}
                c_item[e2] = er
                c[e1]=c_item

    opps = int(ls[combos+1])
  
    for opp in range(combos+2,combos+2+opps):
        e1 = ls[opp][0]
        er = ls[opp][1]

        #compose list based on 
        if o.has_key(er):
            o_item = o[er]
            o_item.append(e1)
            o[er]=o_item
        else:
            o_item = []
            o_item.append(e1)
            o[er]=o_item
  
        if o.has_key(e1):
            o_item = o[e1]
            o_item.append(er)
            o[e1]=o_item
        else:
            o_item = []
            o_item.append(er)
            o[e1]=o_item
    
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
     
        #check for and handle constructive combinations
        if cl > ll:

            if c.has_key(ll):
                c_item = c[ll]
                if c_item.has_key(cl):
                    outstr = outstr[:len(outstr)-1] + c_item[cl]
                    const_happened = 1
        else:
            if c.has_key(cl):
                c_item = c[cl]
                if c_item.has_key(ll):
                    outstr = outstr[:len(outstr)-1] + c_item[ll]
                    const_happened = 1
        
        #check for and handle destructive combinations        
        found_dest = 0
        if const_happened == 0:
            if o.has_key(cl):
                rmost = 0
                for dlet in o[cl]:
                    if dlet in outstr:
                        found_dest = 1
                        dlet_loc = outstr.rfind(dlet)
                        if dlet_loc > rmost:
                            rmost = dlet_loc

            if found_dest == 1:
                dest_happened =1
                #outstr = outstr[:rmost]
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

