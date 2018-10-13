import sys

def main():
    input_file = str(sys.argv[1])
    output_file = str(sys.argv[2])

    in_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    n = int(in_file.readline())
    #n = n.rstrip('\n')
    #print(n)
    #print()
    l = 1

    for line in in_file:
        t = line.rstrip('\n')
        u = sign_to_number(t)
        v = int(find_k(t))
        #print(u, v)
        w = ''
        b = 0
        while b < v:
            w += '1'
            b += 1
        w = int(w,2)
        #print(u, w)
        r = solve(x=u, y=w, z=v)
        #print(r)
        output_file.write('Case #' + str(l) + ': ' + str(r) + '\n')
        l += 1
    in_file.close()
    output_file.close()

def sign_to_number(x):
    a = ''
    for char in x:
        if char != ' ':
            if char == '-':
                a += '0'
            else:
                a += '1'
            continue
        else:
            break
    return a

def find_k(x):
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

def solve(x, y, z):
    s = 0
    i = ''
    k = 0
    for cha in x:
        i += cha
    while k < len(i):
        char = i[0]
        #print(i,s,char)
        if char == '1':
            i = i[1:]
            continue
        elif len(i) < z:
            s = 'IMPOSSIBLE'
            break
        else:
            c = i[0:z]
            f = i[z:]
            d = int(c,2)
            e = d^y
            if e == 0:
                g = '00'
            elif e == 1:
                g = '01'
            else:
                g = '{0:b}'.format(e)
            s += 1
            i = g + f
            #print(c,f,d,e,g)
            continue
        k += 1
    return s

main()
