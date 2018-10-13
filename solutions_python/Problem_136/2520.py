import glob
import os.path
def procfile(fin,fout):
    T=int(fin.readline())
    
    solutions="\n".join(["Case #%d: %.7f"%(i+1, procproblem([float(x) for x in fin.readline().split()])) for i in range(T)])
    fout.write(solutions)
    fout.close()

def procproblem(data):
    C,F,X = data
    rate=2.0
    cookies=0.0
    #C farm cost, F farm rate, X cookies needed
    #C/F = farm payback time
    #(C-cookies)/rate = time to next farm
    #X-cookies cookies left
    #(X)/rate finish time if nop
    #(X)/rate < C/F will farm pay itself back in time?
    
    #optimal_farms=n   X/(2+Fn) - C/F  solve for lim
    optimal_farms = int((X/C) - (2/F))
    #print optimal_farms
    optimal_farms = optimal_farms if optimal_farms >= 0 else 0
    #note: you can't buy partial farms

    seconds=0.0
    
    for i in range((optimal_farms)):
        seconds += C / (F*i+ 2.0)
        #print C / (F*i+ 2.0)

    seconds += X / (F * optimal_farms + 2.0)

    return seconds

for x in glob.glob("*.in"):
    if os.path.isfile(x+".out"):
        print(x + ".out already exists")
        continue
    print(x)
    try:
        fin,fout=file(x),file(x+".out","w+")
        procfile(fin,fout)
    finally:
        fin.close()
        fout.close()