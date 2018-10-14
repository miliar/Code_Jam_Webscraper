import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for t in range(T):
    line = iFile.readline().strip().split()
    
    N = int(line[0])
    tgt_vol = float(line[1])
    tgt_tmp = float(line[2])

    sources = []

    for n in range(N):
        line = iFile.readline().strip().split()
        sources.append( (float(line[0]),float(line[1])) )

    if N == 1:
        if(tgt_tmp == sources[0][1]):
            answer = tgt_vol / sources[0][0]
        else:
            answer = "IMPOSSIBLE"
    else:
        if( (tgt_tmp > max(sources[0][1],sources[1][1])) or (tgt_tmp < min(sources[0][1],sources[1][1]))):
            answer = "IMPOSSIBLE"
        else:
            if(sources[0][1] == sources[1][1]):
                answer = tgt_vol / (sources[0][0]+sources[1][0])
            else:
                v1 = tgt_vol*(tgt_tmp-sources[1][1])/(sources[0][1]-sources[1][1])
                v2 = tgt_vol - v1
                answer = max(v1/sources[0][0],v2/sources[1][0])

    output = str(answer)
    
    print("Case #"+str(t+1)+": "+output)
