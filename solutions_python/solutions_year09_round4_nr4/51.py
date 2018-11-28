from math import sqrt

def min_r(plants):
    if len(plants) == 1:
        return plants[0][2]
    if len(plants) == 2:
        return max((plants[0][2], plants[1][2]))

    min_dist = float("inf")
    p1, p2, p3 = plants
    d1 = dist(p1, p2)/2, p3[2]
    d2 = dist(p2, p3)/2, p1[2]
    d3 = dist(p1, p3)/2, p2[2]
    a = min((d1, d2, d3))
    return max(a)
        

def dist(p1, p2):
    x1, y1, r1 = p1
    x2, y2, r2 = p2
    
    d = sqrt((x1-x2)**2 + (y1 - y2)**2) + r1 + r2
    return d


def main():
    C = int(raw_input())
    for i in range(1, C+1):
        plants = []
        N = int(raw_input())
        for j in range(N):
            plants.append(map(int, raw_input().split()))

        r = min_r(plants)
        print "Case #%d: %0.8f" % (i, r)

if __name__ == "__main__":
    main()
