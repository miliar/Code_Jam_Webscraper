import math
def main():
    f = open("./B-large.in")
    g = open("./output","w")
    
    numcases = int(f.readline())
    for casenumber in range(numcases):
        N = int(f.readline())
        x = []
        y = []
        z = []
        vx = []
        vy = []
        vz = []
        
        for i in range(N):
            s = f.readline()
            t = s.partition(" ")
            x.append(int(t[0]))
            s = t[2]
            t = s.partition(" ")
            y.append(int(t[0]))
            s = t[2]
            t = s.partition(" ")
            z.append(int(t[0]))
            s = t[2]
            
            t = s.partition(" ")
            vx.append(int(t[0]))
            s = t[2]
            t = s.partition(" ")
            vy.append(int(t[0]))
            s = t[2]
            
            vz.append(int(s))
            
        vxm, xm = sum(vx),sum(x)
        vym, ym = sum(vy),sum(y)
        vzm, zm = sum(vz),sum(z)
        
        if (vxm != 0 or vym !=0 or vzm !=0): 
            t = -((vxm*xm + vym*ym + vzm*zm)*1.0)/(vxm*vxm + vym*vym + vzm*vzm)
            if(t < 0):
                t = 0
        else:
            t = 0
        a = (vxm*t+xm)*(vxm*t+xm)
        b  = (vym*t+ym)*(vym*t+ym)
        c = (vzm*t+zm)*(vzm*t+zm)
        d = (math.sqrt(a+b+c))/N
       
            
        
        s = "Case #" + str(casenumber+1) + ": " + str(d) + " " +str(t)+"\n"
        g.write(s)
