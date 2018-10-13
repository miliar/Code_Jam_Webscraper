%%% Not pure Python : Sage Math

path = '/import/grecc/ducas/gcj/ex3/'

def solve(a,N,M):
    row_max = [max(v) for v in a]
    col_max = [max(v) for v in a.transpose()]

    for y in range(N):
        for x in range(M):
            if a[y,x] <> min([row_max[y],col_max[x]]):
                return "NO"

    return "YES"

def make_palin_odd(n):
    l = list(str(n))
    s = ""
    for x in l:
        s+= x
    l.reverse()
    for x in l[1:]:
        s+= x
    return ZZ(s)

def is_palin(n):
    l = list(str(n))
    ll = list(str(n))
    l.reverse()
    return (l==ll)

def int_of_list(l):
    s = ""
    for x in l:
        s+= x
    return ZZ(s)

def count_odd_sq_and_fair(rA,rB,A,B):
    lA = list(str(rA))
    n = len(lA)
    if (n%2)>0:
        start = int_of_list(lA[ :ceil(n/2)])
    else:
        start = int_of_list(['1'] + ['0' for i in range(floor(n/2))])
    x = start
    pal_x = make_palin_odd(x)
    c = 0
    while pal_x <= rB:
        r = pal_x*pal_x
        if is_palin(pal_x*pal_x):
            if (A <= r) and (r <= B):
                c+=1
        x+=1
        pal_x = make_palin_odd(x)
    return c
        

def solve(A,B):
    rA = floor(sqrt(A))
    rB = ceil(sqrt(B))
    c = count_even_sq_and_fair(rA,rB,A,B)
    c += count_odd_sq_and_fair(rA,rB,A,B)
    return c

def read_data_ex3(filen):
    f = open(path+filen,'r')
    l = f.read().split('\n')
    f.close()

    fout = file(path+filen+".out",'w')
    n = ZZ(l[0])
    line_index = 1
    for i in range(n):
        sizes = l[line_index].split(' ')
        A = ZZ(sizes[0])
        B = ZZ(sizes[1])
        line_index += 1
        print >> fout, "Case #"+str(i+1)+":", solve(A,B)


read_data_ex3("test")

