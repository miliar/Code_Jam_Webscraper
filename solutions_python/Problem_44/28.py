import sys
from decimal import Decimal

def main():
    input = open(sys.argv[1])
    num_cases = int(input.readline())
    
    for i in range(num_cases):
        num_flies = int(input.readline())
        
        x0 = Decimal(0)
        xv = Decimal(0)
        y0 = Decimal(0)
        yv = Decimal(0)
        z0 = Decimal(0)
        zv = Decimal(0)
        
        for j in range(num_flies):
            fly = [int(t) for t in input.readline().split()]
            x0 += fly[0]
            y0 += fly[1]
            z0 += fly[2]
            xv += fly[3]
            yv += fly[4]
            zv += fly[5]
        
        x0 /= num_flies
        xv /= num_flies
        y0 /= num_flies
        yv /= num_flies
        z0 /= num_flies
        zv /= num_flies
        
        xvyvzv = xv**2 + yv**2 + zv**2
        if xvyvzv == 0:
            t = Decimal(0)
        else:
            t = -(x0*xv + y0*yv + z0*zv) / (xv**2 + yv**2 + zv**2)
        if t < 0: t = Decimal(0)
        
        d = ((xv*t + x0)**2 + (yv*t + y0)**2 + (zv*t + z0)**2).sqrt()
        
        print 'Case #%d: %.8f %.8f' % (i+1, d, t)
        
if __name__ == '__main__':
    main()
    