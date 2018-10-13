__author__="Freezer"
__date__ ="$03.09.2009 12:11:51$"

if __name__ == "__main__":
    need = "welcome to code jam"
    needlen = len(need)
    def func(string, length, npos, spos):
        if npos == needlen:
            return 1
        c = need[npos];
        result = 0
        for i in range(spos, length):
            if string[i] == c:
                result += func(string, length, npos+1, i+1)
        return result

    fin  = open('d:\\c.in', 'r')
    fout = open('d:\\c.out', 'w')
    N = int(fin.readline())
    for i in range(1, N+1):
        line = fin.readline()
        fout.write('Case #%d: %04d\n' % (i, func(line, len(line), 0, 0)))
