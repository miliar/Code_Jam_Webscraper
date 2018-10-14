import os

def main():
    f = open('A-large.in', 'r')
    f2 = open('A-large.out', 'w')
    inp = f.readlines()
    t = int(inp[0].replace('\n', ''))
    del inp[0]
    
    forward = 0
    for i in range(t):
        d = ['/']    
        mkdir = 0
        oper = inp[forward].replace('\n', '').split(' ')
        n = int(oper[0])
        m = int(oper[1])
        for j in range(n):
            d.append(inp[forward+j+1].replace('\n', ''))
        for q in range(m):
            val = inp[forward+q+1+n].replace('\n', '')
            while val not in d:
                mkdir += 1
                d.append(val)
                val = os.path.dirname(val)
        result = 'Case #' + str(i+1) + ': ' + str(mkdir) + '\n'
        print result
        f2.write(result)
        
        forward = n+m+1+forward
    f.close()
    f2.close()


if __name__ == '__main__':
    main()
