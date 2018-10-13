from codejam import *

@main
def RPI():
    T = read_int()
    for case in range(T):
        N = read_int()
        matches = []
        for i in range(N):
            matches.append(read_str())
        nwon = [s.count('1') for s in matches]
        debug(nwon=nwon)
        nlost = [s.count('0') for s in matches]
        debug(nlost=nlost)
        wp = [float(nwon[i]) / (nwon[i]+nlost[i]) for i in range(N)]
        debug(wp=wp)
        owp = []
        for i in range(N):
            o = 0
            n = 0
            for j in range(N):
                if j == i: continue
                if matches[j][i] == '.': continue
                nw = nwon[j]
                if matches[j][i] == '1': nw -= 1
                nl = nlost[j]
                if matches[j][i] == '0': nl -= 1
                if nw+nl > 0:
                    o += float(nw) / (nw+nl)
                    n += 1
            owp.append(o / n)
        debug(owp=owp)
        oowp = []
        for i in range(N):
            oo = 0
            n = 0
            for j in range(N):
                if j == i: continue
                if matches[j][i] == '.': continue
                oo += owp[j]
                n += 1
            oowp.append(oo / n)
        debug(oowp=oowp)
        rpi = [0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] for i in range(N)]
        printcase(case, '\n'.join(str(i) for i in rpi), sep='\n')
