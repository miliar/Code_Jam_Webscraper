# https://code.google.com/codejam/contest/6224486/dashboard

if __name__ == "__main__":
    filein = open('2015QA.in', 'r')
    fileout = open('2015QA.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t+1))
        [S_max, S_str] = filein.readline().split()
        s = list(map(int, list(S_str)))
        ans = 0
        current_people = 0
        current_level = 0
        for si in s:
            if current_people < current_level:
                ans += current_level - current_people
                current_people = current_level
            current_people += si
            current_level += 1
        fileout.write('%d\n' % (ans))

    filein.close()
    fileout.close()
