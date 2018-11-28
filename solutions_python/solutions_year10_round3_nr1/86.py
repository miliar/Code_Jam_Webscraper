# Problem A of Google Code Jam 2010 Round-1 Sub-3
def intersect(l0,r0,l1,r1):
    return (((l0>l1)and(r0<r1))or((l0<l1)and(r0>r1)))

def rope_intranet(s):
    n = len(s)
    cnt = 0
    i = 0
    while i<n:
        j = i+1
        while j<n:
            if intersect(s[i][0],s[i][1],s[j][0],s[j][1]):
                cnt = cnt+1
            j = j+1
        i = i+1
    return cnt

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        lines = raw_input()
        a = []
        for j in range(int(lines)):
            line = raw_input()
            line = line.split()
            a.append([int(line[0]),int(line[1])])
        print 'Case #%d: %d'%(i,rope_intranet(a))
