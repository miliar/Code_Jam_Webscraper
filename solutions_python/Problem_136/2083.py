def main():
    name = input()
    lines = open(name+'.in').readlines()
    T = int(lines[0])
    s = ''
    for i in range(1, T+1):
        C, F, X = map(float, lines[i].split())
        rate, time = [2], [0]
        while time[-1] == 0 or time[-1] + X/rate[-1] < time[-2] + X/rate[-2]:
            time.append(time[-1] + C/rate[-1])
            rate.append(rate[-1] + F)
        total = time[-2] + X/rate[-2]
        case = 'Case #'+str(i)+': '
        case += str(round(total, 7)) + '\n'
        s += case
    open(name+'.out', 'w').write(s)

if __name__ == '__main__':
    main()
