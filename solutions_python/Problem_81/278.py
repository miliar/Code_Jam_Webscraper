def solve_it(a):
    wp = []
    wp_tup = []
    owp = []
    oowp = []
    for aa in a:
        w = 0.0
        c = 0.0
        for aaa in aa:
            if aaa=='1':
                w = w + 1.0
                c = c + 1.0
            elif aaa=='0':
                c = c + 1.0
        if c!=0.0:
            wp.append(w/c) 
            wp_tup.append([w,c])
        else:
            wp.append(0.0)
            wp_tup.append([w,c])
#    print wp
#    print wp_tup
    t = len(a)
    for j in range(0,t):
        owp_r = 0.0
        cd = 0.0
        for k in range(0,t):
            if a[j][k]=='1':
                owp_r = owp_r + (wp_tup[k][0])/(wp_tup[k][1]-1.0)
                cd = cd + 1.0
            elif a[j][k]=='0':
                owp_r = owp_r + (wp_tup[k][0]-1.0)/(wp_tup[k][1]-1.0)
                cd = cd + 1.0
        owp.append(owp_r/cd)
#    print owp
    for j in range(0,t):
        owp_c = 0.0
        cd = 0.0
        for k in range(0,t):
            if a[j][k]=='1' or a[j][k]=='0':
                owp_c = owp_c + owp[k]
                cd = cd + 1.0
        oowp.append(owp_c/cd)
#    print oowp
    # Result
    for j in range(0,t):
        print "%0.12f" % (((0.25*wp[j])+(0.5*owp[j])+(0.25*oowp[j])),)
    return
f = open("A-large.in","r")
c = 0
i = True
s = 0
a = []
c_c = 0
for l in f:
    if c==0:
        c = c + 1
        continue
    try:
        s = int(l.strip("\n"))
        if c_c!=0:
  	        print "Case #%d:" % (c_c,)
	        solve_it(a)
        a = []
        c_c = c_c + 1
    except: 
        k = list(l.strip("\n"))
        a.append(k)
        continue
print "Case #%d:" % (c_c,)
solve_it(a)

f.close()
