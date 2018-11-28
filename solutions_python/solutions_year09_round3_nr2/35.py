import math

INPUT_FILE = 'inputs/B-large.in'
OUTPUT_FILE = 'outputs/B-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline().strip())
for i in range(T):
    N = int(f_in.readline().strip())
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    for n in range(N):
        xi, yi, zi, vxi, vyi, vzi = [int(x) for x in f_in.readline().strip().split()]
        x.append(xi)
        y.append(yi)
        z.append(zi)
        vx.append(vxi)
        vy.append(vyi)
        vz.append(vzi)
    
    xSum = sum(x)
    ySum = sum(y)
    zSum = sum(z)
    vxSum = sum(vx)
    vySum = sum(vy)
    vzSum = sum(vz)
    
    t_min = 0;
    denom = (vxSum * vxSum + vySum * vySum + vzSum * vzSum)
    if denom != 0:
        t_min = - (xSum * vxSum + ySum * vySum + zSum * vzSum) / (vxSum * vxSum + vySum * vySum + vzSum * vzSum)
    if (t_min < 0):
        t_min = 0
    
    xAdd = 0
    yAdd = 0
    zAdd = 0
    
    for j in range(N):
        xAdd += x[j] + vx[j] * t_min
        yAdd += y[j] + vy[j] * t_min
        zAdd += z[j] + vz[j] * t_min
    
    L_min = math.sqrt((xAdd * xAdd + yAdd * yAdd + zAdd * zAdd)) / N
    print("Case #" + str(i + 1) + ": %.8F %.8F" % (L_min, t_min))
    f_out.write("Case #" + str(i + 1) + ": %.8F %.8F\n" % (L_min, t_min)) 

f_in.close()
f_out.close()
