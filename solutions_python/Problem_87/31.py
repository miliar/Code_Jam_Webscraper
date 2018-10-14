import sys

def airport_walkways(d, s, r, t, ws):
    d_wws = sum(i[1] - i[0] for i in ws)
    a = d - d_wws
    if a == 0: temp = []
    else: temp = [[0, a, 0]]
    ln = len(ws)
    wss = [i[2] for i in ws]
    for i in range(len(ws)):
        b = ws[wss.index(min(wss))]
        temp += [[a, b[1] - b[0] + a, min(wss)]]
        a += b[1] - b[0]
        wss[wss.index(min(wss))] = max(wss) + 1
    ws = [i*1 for i in temp]
    del temp, wss
    takent = 0
    for n, i in enumerate(ws):
        if ((r + i[2])*t) <= i[1] - i[0]:
            takent += t + (i[1] - i[0] - (r + i[2])*t) / (s + i[2])
            takent += sum((j[1] - j[0]) / (s + j[2]) for j in ws[n+1:])
            break
        else:
            a = (i[1] - i[0]) / (r + i[2])
            takent += a
            t -= a
    return str(round(takent, 8))

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    x = 0
    for i in range(1, int(Input[0]) + 1):
        (d, s, r, t, n) = [int(j) for j in Input[i+x].split(' ')]
        ws = [[int(k) for k in Input[i+j+x].split(' ')] for j in range(1, n+1)]
        x += n
        result = airport_walkways(d, s, r, t, ws)
        Output += "Case #" + str(i) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__": main(sys.argv[1])
