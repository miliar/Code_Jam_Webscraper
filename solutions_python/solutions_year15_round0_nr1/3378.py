def main():
    name = input()
    lines = open(name+'.in').readlines()
    T = int(lines[0])
    result = ''
    for l in range(1,T+1):
        s = lines[l].split()
        s_max = int(s[0])
        s = list(map(int, s[1]))
        accumulated = 0
        required = 0
        for i in range(s_max+1):
            if accumulated < i and s[i] != 0:
                required += i - accumulated
                accumulated = i
            accumulated += s[i]
        case = 'Case #'+str(l)+': '+str(required)+'\n'
        result += case
    open(name+'.out', 'w').write(result)

if __name__ == '__main__':
    main()
