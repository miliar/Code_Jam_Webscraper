import multiprocessing
import sys
import math
import bisect


class RangeSearch(object):
    def __init__(self, i, (start, end)):
        self.i = i
        self.start = start
        self.end = end
        self.startsearch = int(math.ceil(math.sqrt(start)))  # >=
        self.endsearch = int(math.ceil(math.sqrt(end)))  # <=
        self.result = 0

    def __str__(self):
        return "Range Search %d %d-%d: %d" % (self.i, self.start, self.end, self.result)


class SearchRange(object):
    def __init__(self, start, end):
        self.searches = []
        self.start = start
        self.end = end
        self.start_ranges = []
        self.end_ranges = []
        self.processed = 0

    def process(self):
        if self.processed == 0:
            del self.start_ranges[:]
            del self.end_ranges[:]
            self.searches.sort(key=lambda x: x.startsearch)
            self.start_ranges += sorted([(x.startsearch, i) for i, x in enumerate(self.searches)])
            self.end_ranges += sorted([(x.endsearch, i) for i, x in enumerate(self.searches)])
            self.processed = 1

    def run(self):
        self.processed = 0
        self.process()
        self.start = self.start_ranges[0][0]
        self.end = max([x[0] for x in self.end_ranges])

        #print "FROM %d TO %d" % (self.start, self.end)
        #print [str(x) for x in self.searches]

        start_vals = [x[0] for x in self.start_ranges]
        end_vals = [x[0] for x in self.end_ranges]

        for i in range(self.start, self.end+1):
            if str(i) == str(i)[::-1]:
                qd = i*i
                if str(qd) == str(qd)[::-1]:
                    left = bisect.bisect_right(start_vals, i)
                    #if left == len(start_vals):
                    #    left -= 1
                    right = bisect.bisect_left(end_vals, i)
                    if right:
                        right -= 1

                    #print start_vals[-1], start_vals, end_vals
                    #print i, qd, left, right, self.start_ranges[:left], self.end_ranges[right:]

                    for idx in set([x[1] for x in self.start_ranges[:left]]).intersection(set([x[1] for x in self.end_ranges[right:]])):
                        if qd >= self.searches[idx].start and qd <= self.searches[idx].end:
                            #print "Incrementing", str(self.searches[idx])
                            self.searches[idx].result += 1

    def __str__(self):
        return "Search %d-%d, %d" % (self.start, self.end, len(self.searches))

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        else:
            return self.end < other.end

    def __gt__(self, other):
        if self.start != other.start:
            return self.start > other.start
        else:
            return self.end > other.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __le__(self, other):
        if self.start != other.start:
            return self.start <= other.start
        else:
            return self.end <= other.end

    def __ge__(self, other):
        if self.start != other.start:
            return self.start >= other.start
        else:
            return self.end >= other.end

    def __ne__(self, other):
        return self.start != other.start or self.end != other.end


def reader(f):
    return f.readlines()


def writer(f, data):
    f.write(data)


def chunks(l, n, k=0):
    for i in xrange(0, len(l), n):
        yield l[i:i+(n-k)]


def split(data):
    ranges = []
    for i, line in enumerate(data):
        rs = RangeSearch(i+1, [int(x) for x in line.split(" ")])
        sr = SearchRange(rs.startsearch, rs.endsearch)
        sr.searches.append(rs)
        bisect.insort(ranges, sr)

    n = len(ranges)/16
    #for r in ranges:
    #    print r.start, r.end

    #pack ranges
    i = 1
    while i < len(ranges):
        #print ranges[i-1], ranges[i]
        if ranges[i-1].end >= ranges[i].start:
            #print " UNITE"
            if len(ranges[i-1].searches) < n or (ranges[i-1].end >= ranges[i].end):
                ranges[i-1].end = max(ranges[i-1].end, ranges[i].end)
                ranges[i-1].searches += ranges[i].searches
                del(ranges[i])
            else:
                ranges[i].process()
                k = bisect.bisect_right(ranges[i].end_ranges, ranges[i-1].end)
                if k == len(ranges[i].end_ranges):
                    #should not happen as ranges[i-1].end >= ranges[i].start
                    #print " SKIP %d" % k
                    i += 1
                    continue
                cut_idx = ranges[i].end_ranges[k][1]
                ranges[i-1].searches += ranges[i].searches[:cut_idx]
                #print " Transferred %d from idx %d" % (len(ranges[i].searches[:cut_idx]), k)
                ranges[i].searches = ranges[i].searches[cut_idx:]
                #print " Moved start from %d to %d" % (ranges[i].start, ranges[i-1].end+1)
                ranges[i].start = ranges[i-1].end + 1
                if len(ranges[i].searches) == 0:
                    del(ranges[i])
                    continue
                ranges[i].processed = 0
                ranges[i-1].processed = 0
                srt = sorted(ranges)
                if ranges != srt:
                    ranges = srt
                else:
                    i += 1
        else:
            #print " SKIP"
            i += 1

    return ranges


def transform((queue, no, workset)):
    workset.run()

    for s in workset.searches:
        queue.put("Case #%d: %d" % (s.i, s.result))

    return len(workset.searches)

if __name__ == "__main__":
    #read
    data = reader(sys.stdin)

    #extract something
    num_jobs = int(data[0].strip())

    #split
    worksets = [x for x in split(data[1:])]

    #sys.exit(0)

    #transform
    manager = multiprocessing.Manager()
    pool = multiprocessing.Pool()
    queue = manager.Queue()
    n = map(transform, ((queue, i+1, workset) for i, workset in enumerate(worksets)))

    r = []
    while not queue.empty():
        r.append(queue.get())

    #write
    for x in sorted(r, key=lambda s: int(s[s.find("#")+1:s.find(":")])):
        writer(sys.stdout, x+"\n")
