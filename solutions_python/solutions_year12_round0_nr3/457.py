import string

def solve(A, B):
    recycled = 0
    s=set()
    while A <= B:
        if (A in s):
            A+= 1
            continue
        i = 0
        num = 1
        s.add(A)
        a = str(A)
        while i < len(a)-1:
            i += 1
            if a[i] == 0:
                continue
            l = int(a[i:]+a[:i])
            if l > A and l <= B and l not in s:
                num += 1
                s.add(l)
        recycled += num * (num - 1) / 2

        A += 1

    return recycled

def main():
    inp = open('C-large.in', 'r')
    out = open('C-large.out', 'w')
    num_case = int(inp.readline())
    i = 1
    for line in inp:
        instance = map(int, line.split())
        A = instance[0]
        B = instance[1]
        out.write("Case #"+str(i)+": "+str(solve(A,B))+'\n')
        i+=1
    inp.close()
    out.close()

if __name__ == "__main__":
    main()
