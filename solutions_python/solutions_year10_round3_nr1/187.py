def process(points):
    count = 0 
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                if p1[0] < p2[0] and p1[1] > p2[1]:
                    count += 1
    return count
            
    
if __name__ == '__main__':
    file = 'A-large.in'
    f = open(file,'r')
    num_case = int(f.readline().strip())
    for i in range(num_case):
        N = int(f.readline().strip())
        points = []
        for j in range(N):
            a = f.readline().strip()
            points.append([int(x) for x in a.split()])
        ans = process(points)
        print "Case #%d: %d" % (i+1, ans )