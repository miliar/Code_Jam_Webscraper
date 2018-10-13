import numpy as np
from heapq import *


class Solution(object):
    base_folder = "/home/knut/Downloads/"
    out_folder = "results/"

    def __init__(self, name, test=False):
        self.test = test
        suffix = ".test" if test else ""
        self.input_file = self.base_folder + name + suffix + ".in"
        self.output_file = self.out_folder + name + suffix +  ".out"
        print("Reading")
        self.parse_input()
        print("Running")
        self.run()
        print("Writing")
        self.write_output()

    def run(self):
        pass

    def format_output(self):
        self.output_lines = ["Case #%s: %s" % (i+1, n)
                             for i, n in enumerate(self.results)]

    def parse_input(self):
        with open(self.input_file) as f:
            f.readline()
            self.inputs = [self.parse_line(line) for line in f.readlines()]

    def parse_line(self):
        pass

    def write_output(self):
        print("Writing to %s" % self.output_file)
        self.format_output()
        if self.test:
            return self.write_test()
        with open(self.output_file, "w") as f:
            f.write("\n".join(self.output_lines))

    def write_test(self):
        for line in self.output_lines:
            print(line)


class Stalls(object):
    def __init__(self, k, n):
        self.k = k
        self.ds = []
        heappush(self.ds, 0)
        self.populate(n)

    def update_stalls(self):
        d = self.k-heappop(self.ds)-1
        self.a = d/2
        self.b = d-self.a
        heappush(self.ds, self.k-self.a)
        heappush(self.ds, self.k-self.b)

    def populate(self, m):
        for _ in xrange(m):
            self.update_stalls()

    def __str__(self):
        return str(self.b) + " " + str(self.a)


class Stalls2(object):
    def __init__(self, k, m):
        k = k+2
        self.k = k
        self.left_distances = np.arange(self.k)
        self.right_distances = np.arange(self.k-1, -1, -1)
        self.mins = np.minimum(self.left_distances, self.right_distances)
        self.maxs = np.maximum(self.left_distances, self.right_distances)
        self.vals = self.mins*self.k+self.maxs
        self.populate(m)

    def find_place(self):
        i = np.argmax(self.vals)
        self.max_d = self.maxs[i]-1
        self.min_d = self.mins[i]-1
        return i

    def update_stalls(self):
        i = self.find_place()
        left = 0
        right = self.k
        for j in xrange(i+1):
            if self.right_distances[i-j] == 0:
                left = i-j
                break
            self.right_distances[i-j] = j
        for j in xrange(self.k-i):
            if self.left_distances[i+j] == 0:
                right = i+j
                break
            self.left_distances[i+j] = j

        a = self.left_distances[left:right]
        b = self.right_distances[left:right]
        self.maxs[left:right] = np.maximum(a, b)
        self.mins[left:right] = np.minimum(a, b)
        self.vals[left:right] = self.mins[left:right] * self.k+self.maxs[left:right]

    def populate(self, num_persons):
        for _ in range(num_persons):
            self.update_stalls()

    def __str__(self):
        return str(self.max_d) + " " + str(self.min_d)


class SimpleStalls(object):
    def __init__(self, k, m):
        n_divs = int(np.floor(np.log2(m))+1)
        n_parts = 2**n_divs
        self.a = (k-n_parts+1)/(n_parts)
        k_rest = m-(2**(n_divs-1)-1)
        n_rest = (k-n_parts+1) % n_parts

        if n_rest >= k_rest:
            self.b = self.a+1
        else:
            self.b = self.a
        if n_rest-n_parts/2 >= k_rest:
            self.a = self.a+1

    def __str__(self):
        return str(self.b) + " " + str(self.a)


class BathroomStalls(Solution):
    def parse_line(self, line):
        return [int(c) for c in line.split()]

    def run(self):
        #self.results = []
        #i = 0
        #n = len(self.inputs)
        #for k, m in self.inputs:
        #    print i, n, k, m
        #    self.results.append(str(Stalls(k, m)))
        #    i += 1

        self.results = [str(SimpleStalls(k, m)) for k, m in self.inputs]

import time
t = time.time()
BathroomStalls("C-small-2-attempt1")
print(time.time()-t)

