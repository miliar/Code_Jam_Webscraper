def solve(C, F, X, base_rate):
    rate=base_rate
    if X<C:
        return X/rate
    else:
        t=0
        stop=False
        while not stop:
            t+=C/rate
            if X/(rate+F)<(X-C)/rate:
                rate+=F
            else:
                t+=(X-C)/rate
                stop=True
        return t
    

#Main
f=open("B-large.in",'r')
lines=f.readlines()
f.close()

N=eval(lines[0])

results=[]

for i in range(1, N+1):
    tmp=list(map(eval, lines[i].split()))
    result="Case #" + str(i) + ": "
    result+="{:.7f}".format(solve(tmp[0], tmp[1], tmp[2], 2.0))
    print(result)
    result+="\n"
    results.append(result)

f=open("o.in",'w')
f.writelines(results)
f.close()
    
