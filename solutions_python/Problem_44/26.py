import math

def find_center(flies):
    center_coords = [0, 0, 0, 0, 0, 0]
    for fly in flies:
        for i in range(len(center_coords)):
            center_coords[i] += fly[i]

    for i, coord in enumerate(center_coords):
        center_coords[i] = coord/float(len(flies))

    return center_coords


def cross_len(v1, v2):
    a1, a2, a3 = v1
    b1, b2, b3 = v2

    total = 0
    total += (a2*b3 - a3*b2)**2
    total += (a3*b1 - a1*b3)**2
    total += (a1*b2 - a2*b1)**2
    return math.sqrt(total)

def dot_prod(v1, v2):
    prod = 0
    for i, val in enumerate(v1):
        prod += val * v2[i]
    return prod

def minus(v1, v2):
    res = []
    for i, val in enumerate(v1):
        res.append(val - v2[i])
    return res


def vec_len(v):
    ans = 0
    for coord in v:
        ans += coord ** 2

    return math.sqrt(ans)

def is_zero(vec):
    for i in vec:
        if i != 0:
            return False
    return True

def min_dist(center):
    if is_zero(center[3:]):
        return vec_len(center[:3])
    x1 = center[:3]
    x2 = x1[:]
    for i, val in enumerate(center[3:]):
        x2[i] += val
    
    num = cross_len(minus((0, 0, 0), x1),
                    minus((0, 0, 0), x2))
    tmp = minus(x2, x1)
    den = vec_len(minus(x2, x1))
    return abs(num/den)


def min_time(center):
    if is_zero(center[3:]):
        return 0
    x1 = center[:3]
    x2 = x1[:]
    for i, val in enumerate(center[3:]):
        x2[i] += val

    v1 = x1
    v2 = minus(x2, x1)
    num = - dot_prod(v1, v2)
    den = vec_len(v2) ** 2
    if num/den != abs(num/den):
        return None
    return abs(num / den)

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        flies = []
        for j in range(N):
            flies.append(map(int, raw_input().split()))
            
        center = find_center(flies)
        dmin = min_dist(center)
        tmin = min_time(center)
        if tmin is None:
            tmin = 0
            dmin = vec_len(center[:3])
        print "Case #%d: %0.8f %0.8f" % (i, dmin, tmin)

if __name__ == "__main__":
    main()


