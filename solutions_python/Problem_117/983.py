### This not pure python : this use "sage math"

path = '/import/grecc/ducas/gcj/ex2/'

def solve(a,N,M):
    row_max = [max(v) for v in a]
    col_max = [max(v) for v in a.transpose()]

    for y in range(N):
        for x in range(M):
            if a[y,x] <> min([row_max[y],col_max[x]]):
                return "NO"

    return "YES"


def read_data_ex1(filen):
    f = open(path+filen,'r')
    l = f.read().split('\n')
    f.close()

    fout = file(path+filen+".out",'w')
    n = ZZ(l[0])
    line_index = 1
    for i in range(n):
        sizes = l[line_index].split(' ')
        N = ZZ(sizes[0])
        M = ZZ(sizes[1])
        line_index += 1
        mat1 = []
        for k in range(N):
            mat1 += [l[line_index].split(' ')]
            line_index +=1
        mat = matrix(ZZ,mat1)
        print >> fout, "Case #"+str(i+1)+":", solve(mat,N,M)
    return


read_data_ex1("B-large.in")
