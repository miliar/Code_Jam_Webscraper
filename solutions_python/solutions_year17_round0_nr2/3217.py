import sys

def main():
    input_file = str(sys.argv[1])
    output_file = str(sys.argv[2])

    in_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    n = int(in_file.readline())
    l = 1
    for line in in_file:
        t = line.rstrip('\n')
        #print(t)
        r = largest_num(t)
        #print(r)
        output_file.write('Case #' + str(l) + ': ' + str(r) + '\n')
        l += 1
    in_file.close()
    output_file.close()

def largest_num(x):
    n = False
    k = int(x)
    s = str(k)
    m = 0
    while n == False:
        #print('s,n,m',s,n,m)
        if len(s) == 1:
            p = k
            n = True
            #print('1',p)
            break
        elif len(s) == 2:
            #print('s',s)
            if s[0] < s[1]:
                p = k
                n = True
                #print('2+',p)
                break
            elif s[0] == s[1]:
                p = k
                n = True
                break
            else:
                k -= 1
                s = str(k)
                m = 0
                #print('2-')
                continue
        else:
            if s[0] < s[1]:
                s = s[1:]
                m = 0
                #print('++')
                continue
            elif s[0] == s[1]:
                s = s[1:]
                m += 1
                continue
            else:
                if m == 0:
                    k -= 1
                else:
                    k = int(str(k)[0:m]) * 10 ** (len(str(k))-m) + (int(str(k)[m])-1) * 10 ** (len(str(k))-m-1) + 9
                s = str(k)
                m = 0
                #print('--')
                continue
    return p

main()
