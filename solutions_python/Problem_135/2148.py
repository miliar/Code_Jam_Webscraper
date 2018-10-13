def main():
    name = input()
    lines = open(name+'.in').readlines()
    T = int(lines[0])
    s = ''
    for i in range(T):
        ind = 1+10*i
        r1 = int(lines[ind]) - 1
        r2 = int(lines[ind+5]) - 1
        arrange1 = lines[ind+1:ind+5]
        arrange2 = lines[ind+6:ind+10]
        arrange1 = [list(map(int,s.split())) for s in arrange1]
        arrange2 = [list(map(int,s.split())) for s in arrange2]
        S1 = set(arrange1[r1])
        S2 = set(arrange2[r2])
        S = S1 & S2
        case = 'Case #'+str(i+1)+': '
        if len(S) == 1:
            case += str(list(S)[0])
        elif len(S) > 1:
            case += 'Bad magician!'
        else:
            case += 'Volunteer cheated!'
        case += '\n'
        s += case
    open(name+'.out', 'w').write(s)

if __name__ == '__main__':
    main()
