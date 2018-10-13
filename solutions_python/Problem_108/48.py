f = open("A-small-attempt0.in", "r")
fout = open("out.txt", "w")

def out(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)
    print(*args, sep=sep, end=end, file=fout)

def process(T):
    N = int(f.readline().rstrip())
    dl = [f.readline().rstrip().split(' ') for i in range(N)]
    dl = [(int(i[0]), int(i[1])) for i in dl]
    D = int(f.readline().rstrip())
    maxCover = [0 for i in range(N)]
    maxCover[0] = dl[0][0] + dl[0][1]
    for i in range(1,len(dl)):
        fromIdx = i-1;
        checkIdx = i;
        while checkIdx<len(dl) and dl[checkIdx][0] < maxCover[fromIdx]:
            cover = dl[checkIdx][0]+ min(dl[checkIdx][1],dl[checkIdx][0]-dl[fromIdx][0])
            if cover > maxCover[checkIdx]:
                maxCover[checkIdx] = cover
                if maxCover[checkIdx] >= D:
                    out("Case #%d: YES" % T)
                    return
            checkIdx += 1

    out("Case #%d: NO" % T)

if __name__ == '__main__':
    for t in range(1, int(f.readline())+1):
        process(t)

f.close()
fout.close()