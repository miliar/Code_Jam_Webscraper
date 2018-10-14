import time
import numpy as np
import math
import random
from collections import deque

# CONFIG
config = 'assgn5_matrix.txt'
fname = 'ght_small.txt'
qname = 'ght_query.txt'

dist_count = 0

def distance(p1, p2):
    global dist_count
    dist_count += 1
    return np.sqrt(np.sum(np.power(p2.x - p1.x, 2)))

def mahalanobis(p1, p2):
    global dist_count
    dist_count += 1
    tmp = np.array(p2.x - p1.x)
    temp = np.dot(tmp, conf)
    return np.dot(temp, tmp.transpose())

class Point(object):
    def __init__(self, x, idx=None, name=None):
        self.x = np.array(x)
        self.idx = idx
        self.name = name
    def __repr__(self):
        return "x=%s, idx=%s, name=%s" % (self.x, self.idx, self.name)

class GHTree(object):
    def __init__(self, points, dist=None):
        self.left = None
        self.right = None
        self.left_pivot = None
        self.right_pivot = None
        self.dist = dist if dist is not None else distance

        random_elements = random.sample(points, int(math.sqrt(len(points))))
        if len(random_elements) < 1:
            return
        elif len(random_elements) == 1:
            self.left_pivot = random_elements[0]
        
        minn = -np.inf
        for i, p in enumerate(random_elements):
            for j, q in enumerate(random_elements):
                if j == i:
                    continue
                temp = distance(p, q)
                if temp > minn:
                    minn = temp
                    self.left_pivot = p
                    self.right_pivot = q

        if self.left_pivot is not None:
            points.remove(self.left_pivot)
        if self.right_pivot is not None:
            points.remove(self.right_pivot)

        leftNode = []
        rightNode = []
        if len(points) > 0:
            for i, p in enumerate(points):
                dist_left_pivot = distance(self.left_pivot, p)
                if self.right_pivot is None:
                    break
                dist_right_pivot = distance(self.right_pivot, p)
                if dist_right_pivot < dist_left_pivot:
                    rightNode.append(p)
                else:
                    leftNode.append(p)

        if len(leftNode) > 0:
            self.left = GHTree(points=leftNode, dist=self.dist)
        if len(rightNode) > 0:
            self.right = GHTree(points=rightNode, dist=self.dist)

    def isLeaf(self):
        return (self.left is None) and (self.right is None)

class PriorityQueue(object):
    def __init__(self, size=None):
        self.queue = []
        self.size = size
    def push(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort()
        if self.size is not None and self.size < len(self.queue):
            self.queue.pop()

def kNNSearch(ghtree, q, k):
    result = PriorityQueue(k)
    visited = deque([ghtree])

    while len(visited) > 0:
        node = visited.popleft()
        if node is None:
            continue

        if node.left_pivot is not None:
            d = ghtree.dist(q, node.left_pivot)
            result.push(d, node.left_pivot)
        if node.right_pivot is not None:
            d = ghtree.dist(q, node.right_pivot)
            result.push(d, node.right_pivot)

        if node.isLeaf():
            continue

        r = ghtree.dist(node.left_pivot, node.right_pivot)
        d_l = ghtree.dist(node.left_pivot, q)
        d_r = ghtree.dist(node.right_pivot, q)
        if abs(d_l - d_r) <= 2*r:
            visited.append(node.right)
            visited.append(node.left)
        else:
            if (d_l < d_r):
                visited.append(node.left)
            else:
                visited.append(node.right)

    return result.queue

def rangeSearch(ghtree, q, tau):
    result = []
    visited = deque([ghtree])

    while len(visited) > 0:
        node = visited.popleft()
        if node is None:
            continue

        if node.left_pivot is not None:
            d = ghtree.dist(q, node.left_pivot)
            if d < tau:
                result.append((d, node.left_pivot))
        if node.right_pivot is not None:
            d = ghtree.dist(q, node.right_pivot)
            if d < tau:
                result.append((d, node.right_pivot))

        if node.isLeaf():
            continue

        r = ghtree.dist(node.left_pivot, node.right_pivot)
        d_l = ghtree.dist(node.left_pivot, q)
        d_r = ghtree.dist(node.right_pivot, q)
        if abs(d_l - d_r) <= 2*r:
            visited.append(node.right)
            visited.append(node.left)
        else:
            if (d_l < d_r):
                visited.append(node.left)
            else:
                visited.append(node.right)

    return result

with open(config) as c:
    cfg = c.read().splitlines()
conf = [map(float, con.split()) for con in cfg]
conf = np.array(conf)


knn_query_dist_count = []
range_query_dist_count = []
range_query_time = []
knn_query_time = []

if __name__ == '__main__':
    with open(fname) as f:
        contents = f.read().splitlines()
    
    values = [content.split() for content in contents]

    points = [Point([float(val[0]), float(val[1])], val[2], val[3]) for val in values]

    ghtree = GHTree(points)

    with open(qname) as q:
        queries = q.read().splitlines()
    queries = [qq.split() for qq in queries]

    for query in queries:
        print query
        if int(query[0]) == 2:  # range search
            pt = Point([float(query[1]),float(query[2])])
            tmp = dist_count
            start = time.time()
            result = rangeSearch(ghtree, pt, float(query[3]))
            end = time.time()
            range_query_dist_count.append(dist_count - tmp)
            range_query_time.append(end - start)

        elif int(query[0]) == 3:    # knn search
            pt = Point([float(query[1]),float(query[2])])
            tmp = dist_count
            start = time.time()            
            result = kNNSearch(ghtree, pt, int(query[3]))
            end = time.time()
            knn_query_dist_count.append(dist_count - tmp)
            knn_query_time.append(end - start)
        
        if len(result) > 0:
            for d, n in result:
                print "\t", n
        print "\n\n"

    np.array(range_query_dist_count)
    np.array(knn_query_dist_count)
    np.array(range_query_time)
    np.array(knn_query_time)

    print "TIME STATS\n"
    print "Range Search"
    print "Min: %f" % min(range_query_time)
    print "Max: %f" % max(range_query_time)
    print "Mean: %f" % np.mean(range_query_time, axis=0)
    print "Deviation: %f\n" % np.std(range_query_time, axis=0)

    print "KNN Search"
    print "Min: %f" % min(knn_query_time)
    print "Max: %f" % max(knn_query_time)
    print "Mean: %f" % np.mean(knn_query_time, axis=0)
    print "Deviation: %f\n" % np.std(knn_query_time, axis=0)

    print "DISTANCE STATS\n"
    print "Range Search"
    print "Min: %f" % min(range_query_dist_count)
    print "Max: %f" % max(range_query_dist_count)
    print "Mean: %f" % np.mean(range_query_dist_count, axis=0)
    print "Deviation: %f\n" % np.std(range_query_dist_count, axis=0)

    print "KNN Search"
    print "Min: %f" % min(knn_query_dist_count)
    print "Max: %f" % max(knn_query_dist_count)
    print "Mean: %f" % np.mean(knn_query_dist_count, axis=0)
    print "Deviation: %f\n" % np.std(knn_query_dist_count, axis=0)
