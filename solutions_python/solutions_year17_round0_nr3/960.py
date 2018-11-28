
def distance(e,occupied):
    rs = 0
    for i in occupied[e+1:]:
        if i == 0:
            rs += 1
        elif i == 1:
            break
    ls = 0
    for i in occupied[e-1::-1]:
        if i == 0:
            ls += 1
        elif i == 1:
            break
    return max(rs,ls),min(rs,ls)


def bathStall(N,k):
    occupied = [0 for _ in range(N+2)]
    occupied[0] = 1
    occupied[N+1] = 1
    stack = []
    stack.append((1,N))
    for i in range(k):
        init = stack[0][0]
        final = stack[0][1]
        stack.pop(0)
        mid = (final+init)/2
        if occupied[mid] == 0:
            occupied[mid] = 1
        else:
            continue
        if mid+1 <= final:
            stack.append((mid+1,final))
        if mid-1>= init:
            stack.append((init,mid-1))
        if i == k-1:
            return mid,occupied


if __name__ == '__main__':
    f = open("C-large.in",'r')
    out = open('t.txt','w')
    for i in range(int(f.readline())):
        line = f.readline().split(' ')
        num, occupied = bathStall(int(line[0]),int(line[1]))
        n = distance(num,occupied)
        out.write("Case #"+str(i+1)+": "+str(n[0])+" "+str(n[1])+"\n")
    out.close()
