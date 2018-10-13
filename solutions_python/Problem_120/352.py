def f(r,t):
    return floor( ( 1-2*r + sqrt( 4*r^2-4*r+1+8*t ) )/4 )

def a():
    with open("input") as fin:
        with open("output","w") as out:
            fin.readline()
            i=1
            for line in fin:
                r,t=map(int,line.split())
                out.write("Case #"+str(i)+": "+str(f(r,t))+"\n")
                i+=1
      
