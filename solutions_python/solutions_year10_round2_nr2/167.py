'''
Created on 2010-05-22

@author: lawford
'''

import operator

def alg2(k,b,t,points,speeds):
    print("===")
    print("b="+str(b))
    chicks = zip(points, speeds)
    print(chicks)
    times = []
    sorted_chicks = sorted(chicks, key=operator.itemgetter(0),reverse=True)
    print(sorted_chicks)
    
    for chick in sorted_chicks:
        x0 = chick[0]
        v = chick[1]
        
        t= (b-chick[0])*1.0/chick[1]
        
        for i in range(0,len(times)):
            hit_time = (x0 - sorted_chicks[i][0])*1.0 / (sorted_chicks[i][1]-v)
            if (hit_time >= 0) and (hit_time <= t):
                t = times[i]
        times.append( t )

    print(times)
    
    return [0]


def alg(k,b,tmax,points,speeds):
    print("===")
    print("b="+str(b)+", t="+str(tmax))
    chicks = zip(points, speeds)
    print(chicks)
    times = []
    sorted_chicks = sorted(chicks, key=operator.itemgetter(0),reverse=True)
    print(sorted_chicks)
    
    swaps = 0
    in_count = 0
    for chick in sorted_chicks:
        if (in_count == k):
            break
        print(times)
        
        x0 = chick[0]
        v = chick[1]
        
        t= (b-x0)*1.0/v
        if (len(times)) and (t < times[-1]):
            if t <= tmax and times[-1] <= tmax:
                t = times[-1]
            else:
                if t <= tmax:
                    for i in range(0,len(times)):
                        if (times[len(times)-i-1] > tmax):
                            swaps = swaps+1                    
        
        if (t <= tmax):
            in_count = in_count+1
        if (len(times) == 0) or (t > tmax):
            times.append( t )

    print(times)
    print(str(in_count)+" of "+str(k))
    if (in_count < k):
        return ["IMPOSSIBLE"]
    
    return [swaps]


if __name__ == '__main__':
    fname = "B"
#    f = open(fname+".in.txt", "r")
    f = open("/raid/downloads/firefox/B-large(2).in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

    piece1 = f.readline()
    while piece1 != '':
        print(piece1)
        [n,k,b,t] = map(int, piece1.split(" "))
        piece2 = f.readline()
        points = map(int, piece2.split(" "))
        piece3 = f.readline()
        speeds = map(int, piece3.split(" "))
        result = alg(k,b,t,points, speeds)
        print(result)
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str,result))+"\n")
        piece1 = f.readline()
        cnt = cnt+1
    fout.close()
    f.close()
