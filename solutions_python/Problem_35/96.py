import time

in_file = "B-large.in"
out_file = "B-large.out"

CONST_LABELS = "abcdefghijklmnopqrstuvwxyz"
LABEL_COUNT = 0

def start():
    f_in = file(in_file, "r")
    f_out = file(out_file, "w")    
    T = int(f_in.readline().strip())

    for i in xrange(T):
        global LABEL_COUNT
        LABEL_COUNT = 0
        altitudes = []
        labels = []
        parts = f_in.readline().strip().split(" ")
        H = int(parts[0])
        W = int(parts[1])
        for j in xrange(H):
            parts = f_in.readline().strip().split(" ")
            a = []
            l = []
            for k in xrange(W):
                a.append(int(parts[k]))
                l.append("#")
            altitudes.append(a)
            labels.append(l)

        generateLabels(altitudes, labels, H, W)
        f_out.write("Case #" + str(i+1) + ":\n")
        msg = ""
        for x in xrange(H):
            for y in xrange(W):
                msg = msg + labels[x][y] + " "
            msg = msg + "\n"
        f_out.write(msg)

    f_in.close()
    f_out.close()

def generateLabels(altitudes, labels, H, W):
    for i in xrange(H):
        for j in xrange(W):        
            if labels[i][j] == "#":
                updateLabels(altitudes, labels, H, W, i, j, [], [])
            
def updateLabels(altitudes, labels, H, W, i, j, xs, ys):
            alt = altitudes[i][j]
            mnm = alt
            new_i = -1
            new_j = -1
            if i-1>=0:
                n = altitudes[i-1][j]
                if n < mnm:
                    mnm = n
                    new_i = i-1
                    new_j = j

            if j-1>=0:
                w = altitudes[i][j-1]
                if w < mnm:
                    mnm = w
                    new_i = i
                    new_j = j-1

            if j+1<W:
                e = altitudes[i][j+1]
                if e < mnm:
                    mnm = e
                    new_i = i
                    new_j = j+1

            if i+1<H:
                s = altitudes[i+1][j]
                if s < mnm:
                    mnm = s
                    new_i = i+1
                    new_j = j

            l = None
            if new_i == -1:
                global CONST_LABELS
                global LABEL_COUNT
                l = CONST_LABELS[LABEL_COUNT]
                LABEL_COUNT = LABEL_COUNT+1
            else:                
                l = labels[new_i][new_j]
            if l != "#":
                for k in xrange(len(xs)):
                    labels[xs[k]][ys[k]] = l
                labels[i][j] = l                    
                return
            else:
                xs.append(i)
                ys.append(j)
                updateLabels(altitudes, labels, H, W, new_i, new_j, xs, ys)
        
start()   
           
