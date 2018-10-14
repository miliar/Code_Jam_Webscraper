INPUT = {
    'config': ('int', 'linearray'),
    'points': ('int', ('linearray', lambda x: x['config'][0]))
}

TEST = ('''\
3
3 2
0 1
3 2
6 1
2 2
0 3
1 1
1 100
6000 4
''', '''\
Case #1: 1.0
Case #2: 2.5
Case #3: 150.0
''')

INPUT_ORDER = ['config', 'points']

def main(config, points):
    P, D = config
    
    # perform problem segmentation
    segments = []
    current_segment = []
    
    limit = points[0][0] + D
    for p, v in points:
        d = (v-1)*D/2.0
        print p,d
        if p - d > limit:
            # create new segment
            segments.append(current_segment)
            current_segment = []
        current_segment.append((p,v))       
        limit = p + d + D   # update limit
        print "NEW LIMIT:", limit
    segments.append(current_segment)
        
    def compute(points):
        a, b = zip(*points)
        # cumulatively sum b
        csum = [0]
        for k in b:
            csum.append(csum[-1] + k)
            
        del csum[0]
        
        points2 = zip(a,csum)
        P_min = a[0]
        
        # compute unadjusted distances
        i = 0
        limit = csum[0]
        p = a[0]
        dist_min = 0
        dist_max = 0
        for v in range(csum[-1]):
            if not v < limit:
                i = i + 1
                limit = csum[i]
                p = a[i]
            
            dist = v * D + P_min - p
            if dist > dist_max:
                dist_max = dist
            if dist < dist_min:
                dist_min = dist
            
        return float(dist_max - dist_min) / 2
        
    # compute for all
    dists = map(compute, segments)
    return str(max(dists))
    