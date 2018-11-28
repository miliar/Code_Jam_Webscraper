import sys


def intersects(w1, w2):
    if w1[0] < w2[0]:
        return (w1[1] > w2[1])
    else:
        return (w1[1] < w2[1])


if __name__ == '__main__':
    ### PROGRAM AAAAAAAAAAA
    #openfile = open('A.in', 'r')
    openfile = sys.stdin
    ET = int(openfile.readline()[:-1])
    for T in range(1, ET+1):
        # read test data
        N = int(openfile.readline()[:-1])
        wire = []
        pts = 0
        for j in range(N):
            AB = openfile.readline()[:-1]
            A, B = [int(s) for s in AB.split(' ')]
            wire.append((A, B))
        #for j in range(N):
        #    print wire[j]
        for j in range(N):
            for i in range(j+1, N):
                if intersects(wire[j], wire[i]):
                    pts += 1
        print 'Case #%s: %s' %(T, pts)
    openfile.close()
