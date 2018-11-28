import sys

def get_numbers_rings(r,t):
    quantity = 0
    radius_min = r
    radius_max = radius_min + 1
    while t > 0:
        area_min = radius_min * radius_min
        area_max = radius_max * radius_max
        diference = area_max - area_min
        if diference <= t:
            quantity += 1
        t -= diference
        radius_min = radius_max + 1
        radius_max = radius_min + 1
    return quantity

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        quantity = int(f.readline())
        for execution in xrange(quantity):
            line = f.readline()
            line = line.split()
            r = int(line[0])
            t = int(line[1])
            print 'Case #%i: %s' %(execution+1,get_numbers_rings(r,t))
