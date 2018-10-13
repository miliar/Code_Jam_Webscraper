def main():
    T = input()
    for i in range(1,T+1):
        N = input()
        naomis = list(map(float, raw_input().split(" ")))
        kens = list(map(float, raw_input().split(" ")))

        naomis.sort()
        kens.sort()

        naomis.reverse()
        kens.reverse()

        war = 0
        dwar = 0

        jn = jk = 0

        while jn < N and jk < N:
            while jk < N and jn < N and naomis[jn] < kens[jk]:
                jk += 1
            if jk < N:
                dwar += 1
                jn += 1
                jk += 1

        while len(naomis) > 0:
            idx = -1
            pos = 0
            while pos < len(naomis) and kens[pos] > naomis[0]:
                idx = pos
                pos += 1
            naomis.pop(0)
            if idx == -1:
                war += 1
                kens.pop()
            else:
                kens.pop(idx)

        print "Case #%d: %d %d" % (i, dwar, war)

main()
