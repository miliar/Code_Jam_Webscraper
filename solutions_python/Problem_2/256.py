import sys

def do(foo):
    f = open(foo)
    o = open(sys.argv[2],'w')
    cases = int(f.next().strip())
    for case in range(cases):
        t = int(f.next().strip())
        na,nb = [int(x) for x in f.next().strip().split()]
        a_arr, a_dept, b_arr, b_dept = [],[],[],[]
        for case_ab in range(na):
            s1,s2 = [x for x in f.next().strip().split()]
            a_dept.append(int(''.join(s1.split(':'))))
            i1,i2 = [int(x) for x in s2.split(':')]
            i2 += t
            while i2 > 59:
                i2 -= 60
                i1 += 1
            b_arr.append(i1*100+i2)
            
        for case_ba in range(nb):
            s1,s2 = [x for x in f.next().strip().split()]
            b_dept.append(int(''.join(s1.split(':'))))
            i1,i2 = [int(x) for x in s2.split(':')]
            i2 += t
            while i2 > 59:
                i2 -= 60
                i1 += 1
            a_arr.append(i1*100+i2)
            
        a,b = [],[]
        for i in a_arr:
            a.append([i, -1])
        for i in a_dept:
            a.append([i, 1])
        for i in b_arr:
            b.append([i, -1])
        for i in b_dept:
            b.append([i, 1])
        a.sort(); b.sort()   
        a_max,b_max,a_mom,b_mom = 0,0,0,0
        for i in a:
            a_mom += i[1]
            if a_mom>a_max:
                a_max = a_mom
        for i in b:
            b_mom += i[1]
            if b_mom>b_max:
                b_max = b_mom
        
        o.write('Case #'+str(case+1)+': '+str(a_max)+' '+str(b_max)+'\n')


if __name__ == '__main__':
    do(sys.argv[1])
