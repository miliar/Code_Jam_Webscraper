import sys

class Star:
    def __init__(self, index, position, distance, t):
        self.position = position
        self.distance = distance
        self.index = index
        self.booster = False
        if self.position >= 0.5 * t:
            self.boostable = self.distance
        elif self.position + self.distance >= 0.5 * t:
            self.boostable = self.position + self.distance - 0.5 * t
        else:
            self.boostable = 0
    
    def travel_time(self):
        if self.booster:
            return int(self.boostable / 1 + (self.distance - self.boostable) / 0.5)
        else:
            return int(self.distance / 0.5)
    
    def nextPos(self):
        return self.position + self.distance
    def __repr__(self):
        return 'Star{}:{}:{}:{}:{}'.format(self.index, self.position, self.distance, self.booster, self.boostable)
    
    def __cmp__(self, other):
        return cmp(self.boostable, other.boostable)
    
def build(sorted_stars, L, t):
    l = L
    for star in sorted_stars:
        if l > 0:
            star.booster = True
            l -= 1

def calculate(stars):
    return sum([star.travel_time() for star in stars])


def solve(f):
    f = open(f)
    w = open('out.txt', 'w')
    # Read the number of cases
    T = int(f.readline())
    for _t in range(T):
        line = map(int, f.readline().split())
        L, t, N, C = line[:4]
        a = line[4:]
#        print L, t, N, C, a
        stars = []
        for i in range(N + 1):
            pos = 0
            dis = a[i % C]
            if i != 0: pos = stars[i - 1].nextPos()
            if i == N:dis = 0
            stars.append(Star(i, pos, dis, t))
#        print 'Stars:{}'.format(stars)
        rank = sorted(stars, reverse=True)
#        print 'Sorted:{}'.format(rank)
        build(rank, L, t)
#        print stars, stars[0].travel_time()
#        print calculate(stars)
        
        
        
        #Print output to file
        output = 'Case #{}: {}\n'.format(_t + 1, calculate(stars))
        print output
        w.write(output)
    
    f.close()
    w.close()




        
if __name__ == '__main__':
    solve('b-small-attempt0.in')

    
