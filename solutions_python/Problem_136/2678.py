f = open('asdf', 'w')

def minsecs(cnum ,C,F,X):
    cps = 2.0
    time = 0.0

    while(True):
        ttg = X / cps
        ttnf = C / cps
        ttgnf = X / (cps+F)
        if(ttnf + ttgnf < ttg):
            time+=ttnf
            cps+=F
        else:
            time+=ttg
            break

    f.write("Case #"+str(cnum)+": "+str(time)+"\n")

for t in range(int(raw_input())):
    i = []
    i += map(float,raw_input().rsplit())
    minsecs(t+1,i[0],i[1],i[2])

