import sys

def cal_time(dist,hourse):
    return (dist-hourse[0])/hourse[1]

with open(sys.argv[1]) as f:
    num = int(f.readline())
    for x in range(0,num):
        this_line  = f.readline().split(' ')
        dist = float(this_line[0])
        hourse_num = int(this_line[1])
        #print dist, hourse_num
        hourses = []
        for y in range(0, hourse_num):
            hourse = f.readline().split(' ')
            hourses.append([float(hourse[0]),float(hourse[1])])
        #print hourses
        result = []
        for hourse in hourses:
            result.append( cal_time(dist, hourse))
        time = max(result)
        print 'Case #{0}: {1:.6f}'.format(x+1,dist/time)
