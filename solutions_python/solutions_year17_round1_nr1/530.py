import sys

def main():
    global in_file
    input_file = str(sys.argv[1])
    output_file = str(sys.argv[2])

    in_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    n = int(in_file.readline())
    l = 1

    for line in in_file:
        t = line.rstrip('\n')
        #print(t)
        n = int(find_n(t))
        c = int(find_c(t))
        k = assemble_cake(x=n,y=c)
        #print(k)
        r = solve(x=k,y=n,z=c)
        #print(r)
        #print('Case #', str(l), ': ', '\n', sep='', end='')
        output_file.write('Case #' + str(l) + ': ' + '\n')
        p = 0
        while p < n:
            q = 0
            while q < c:
                #print(r[p][q], end='')
                output_file.write(r[p][q])
                q += 1
            #print('\n',end='')
            output_file.write('\n')
            p += 1
        l += 1
    in_file.close()
    output_file.close()

def find_n(x):
    a = ''
    for char in x:
        if char != ' ':
            a += char
        else:
            break
    return a

def find_c(x):
    a = ''
    found = False
    for char in x:
        if found == False:
            if char != ' ':
                continue
            else:
                found = True
        else:
            a += char
    return a

def assemble_cake(x,y):
    p = 0
    l = []
    while p < x:
        m = []
        t = in_file.readline()
        t = t.rstrip('\n')
        for char in t:
            m.append(char)
        l.append(m)
        p += 1
    return l

def solve(x,y,z):
    t = horizontal(a=x,b=y,c=z)
    s = vertical(a=t,b=y,c=z)
    return s

def horizontal(a,b,c):
    s = a[:]
    p = 0
    while p < b:
        q = 0
        #print(p,s[p],['?']*c)
        if not s[p] == ['?']*c:
            while q < c:
                t = '?' in s[p]
                while t == True:
                    #print(t,p,q)
                    if s[p][q] == '?':
                        if q == 0:
                            #print(s[p][q],s[p][q+1])
                            s[p][q] = s[p][q+1]
                        elif s[p][0:q] == ['?']*q:
                            s[p][q] = s[p][q+1]
                        else:
                            #print(s[p][q],s[p][q-1])
                            s[p][q] = s[p][q-1]
                    t = '?' in s[p]
                    q += 1
                    if t == True:
                        if not q < c:
                            q = 0
                    #print(s)
                    if t != True:
                        break
                if t != True:
                    break
        p += 1
    return s

def vertical(a,b,c):
    s = a[:]
    p = 0
    while p < b:
        t = ['?']*c in s
        while t == True:
            if s[p] == ['?']*c:
                if p == 0:
                    s[p] = s[p+1]
                elif s[0:p] == [['?']*c]*p:
                    s[p] = s[p+1]
                else:
                    s[p] = s[p-1]
            t = ['?']*c in s
            p += 1
            if t == True:
                if not p < b:
                    p = 0
            if t != True:
                break
        if t != True:
            break
    return s

main()
