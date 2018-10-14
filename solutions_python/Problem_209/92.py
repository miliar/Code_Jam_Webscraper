from solution import Solution
from math import pi


def side_area(h, r):
    return h*pi*2*r


def surface_area(r):
    return pi*r*r


class AmpleSyrup(Solution):

    def parse_input(self):
        self.ks = []
        self.ns = []
        self.sizes_list = []
        with open(self.input_file) as f:
            t = int(f.readline().strip())
            for _ in range(t):
                n, k = [int(c) for c in f.readline().split()]
                sizes = []
                for _ in range(n):
                    sizes.append([int(c) for c in f.readline().split()])
                self.ks.append(k)
                self.ns.append(n)
                self.sizes_list.append(sizes)

    def calculate_small(self, k, sizes):
        hs = [s[1] for s in sizes[:-1]]
        hs.sort()
        hs = hs[::-1]
        side_areas = sum(hs[:k-1]) + sizes[-1][1]
        _surf_area = sizes[-1][0]
        return side_areas+_surf_area

    def calculate(self, k, sizes):
        sizes.sort(key=lambda x: x[0])
        sizes = [(surface_area(r), side_area(h, r)) for r, h in sizes]
        d = len(sizes)-k
        areas = [self.calculate_small(k, sizes)]
        for i in range(1, d+1):
            areas.append(self.calculate_small(k, sizes[:-i]))
        return max(areas)

    def run(self):
        self.results = [self.calculate(k, sizes) for k, sizes in zip(self.ks, self.sizes_list)]


AmpleSyrup("A-large (2)")
