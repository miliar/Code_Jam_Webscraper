N = int(input())

def expand(pie,r,c,R,C):
    x = pie[r][c]
    # expand horizontally
    last = c+1
    first = c
    for ic in range(c+1,C):
        if pie[r][ic] == '?':
            pie[r][ic] = x
            last = ic+1
        else:
            break
    for ic in range(c-1,-1,-1):
        if pie[r][ic] == '?':
            pie[r][ic] = x
            first = ic
        else:
            break
    # expand vertically
    for ir in range(r+1,R):
        if pie[ir][first:last] == list('?'*(last-first)):
            pie[ir][first:last] = list(x*(last-first))
        else:
            break
    for ir in range(r-1,-1,-1):
        if pie[ir][first:last] == list('?'*(last-first)):
            pie[ir][first:last] = list(x*(last-first))
        else:
            break

for c in range(N):
    R,C = map(int,input().split())
    pie = []*R
    for ir in range(R):
        pie.append(list(input()))
    letters = set()
    for ir in range(R):
        for ic in range(C):
            if pie[ir][ic] != '?' and pie[ir][ic] not in letters:
                letters.add(pie[ir][ic])
                expand(pie,ir,ic,R,C)
    print('Case #',c+1,':',sep='')
    for r in pie:
        print(*r,sep='')
    
