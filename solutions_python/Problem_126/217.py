import sys

def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        name, n = in_stream.readline().split()
        n = int(n)
        l = len(name)
        m = 0
        for i in range(l):
            for j in range(i + 1, l + 1):
                k = i
                while k < j:
                    if name[k] not in ['a', 'e', 'i', 'o', 'u']:
                        k2 = k + 1
                        while k2 < j and name[k2] not in ['a', 'e', 'i', 'o', 'u']:
                            k2 += 1
                        if k2 - k >= n:
                            m += 1
                            break
                        k = k2 - 1
                    k += 1
        out_stream.write("Case #%d: %d\n" % (tc + 1, m))
    #        i = 0
        #   while i < l:
            #   if name[i] not in ['a', 'e', 'i', 'o', 'u']:
                #   j = i + 1
                        #while j < l and name[j] not in ['a', 'e', 'i', 'o', 'u']:
                        #                    j += 1
#                if j - i >= n:


if __name__ == '__main__':
#    main(sys.stdin, sys.stdout)
    main(open("A-small-attempt0.in", "r"), open("a-small-out.txt", "w"))