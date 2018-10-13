#!/usr/bin/env python
import sys
import re

p = re.compile(r'(\(.*?\))')

def tokenize(w):
    r = []
    for token in p.split(w):
        if token.isalnum():
            r.extend(token)
        else:
            r.append(token[1:-1])
    return filter(None, r)


def out(X, K):
    print "Case #%s: %s" % (X, K)

class Dataset(object):

    _index = {}

    def run(self, fname):
        self.parse(fname)
        self.index()
        for i, case in enumerate(self.cases):
            out(i+1, self.matches(case))

    def index(self):
        for w in self.vocab:
            for i, c in enumerate(w):
                self._index.setdefault(i, {}).setdefault(c, set()).update([w])

    def get_index(self, k, v):
        try:
            return self._index[k][v]
        except KeyError:
            return None

    def search(self, querydict):
        sets = []
        for k, v in querydict.items():
            t = set()
            if len(v)==1:
                t = self.get_index(k, v)
            else:
                ss = filter(None, (self.get_index(k, c) for c in v))
                if ss:
                    t = reduce(lambda a,b:a|b, ss)
            if t is not None:
                sets.append(t)
        if sets:
            sets = reduce(lambda a,b:a&b, sets)
        return sets or []

    def matches(self, case):
        d = {}
        for i, token in enumerate(tokenize(case)):
            d[i] = token
        s = self.search(d)
        return len(s)

    def parse(self, fname):
        f = open(fname)
        self.vocab = []
        self.cases = []
        L, D, N = map(int, f.readline().split())
        for i in range(D):
            self.vocab.append(f.readline().strip())
        self.cases.extend(x.strip() for x in f.readlines())

if __name__=="__main__":
    d = Dataset()
    d.run(sys.argv[1])
