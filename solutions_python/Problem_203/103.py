q = int(input())
for case in range(1,q+1):
    h,w = [int(x) for x in input().split()]
    mat = [[0]*w for _ in range(h)]
    for y in range(h):
        for x,c in enumerate([ord(x) for x in input()]):
            mat[y][x]=c
    seen = set()
    seen.add(ord('?'))
    for y in range(h):
        for x in range(w):
            if mat[y][x] not in seen:
                seen.add(mat[y][x])
                a=x-1
                while a>=0 and mat[y][a]==ord('?'):
                    a -= 1
                a+=1
                b = x+1
                while b<w and mat[y][b]==ord('?'):
                    b += 1
                b-=1
                
                def check_mat(interval,y):
                    for x in range(interval[0],interval[1]+1):
                        if mat[y][x] != ord('?'):
                            return False
                    return True

                d = y+1
                while d<h and check_mat((a,b),d):
                    d+=1
                d-=1
                c = y-1
                while c>=0 and check_mat((a,b),c):
                    c-=1
                c+=1
                for yi in range(c,d+1):
                    for xi in range(a,b+1):
                        mat[yi][xi] = mat[y][x]
    print("Case #%d:" %(case))
    for y in range(h):
        print(*[chr(i) for i in mat[y]],sep="")
        


