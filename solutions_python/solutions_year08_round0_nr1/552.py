from re import *
import sets

class Case(object):
    def __init__(self, idx, number_of_engines):
        self.index = idx
        self.num_engines = number_of_engines
        self.switches = 0
        self.num_requests = 0
        self.requests_processed = 0
        self.engines = set()
        self.queries = set()
    def add_engine(self, engine):
        self.engines.add(engine)
        if len(self.engines) == self.num_engines:
            return 'get_num_requests'
        else:
            return 'get_engines'
    def add_query(self, query):
        self.queries.add(query)
        self.requests_processed += 1
        if len(self.queries) == self.num_engines:
            self.switches += 1
            self.queries.clear()
            self.queries.add(query)
        if self.requests_processed == self.num_requests:
            return 'new_case'
        else:
            return 'get_requests'
    def to_s(self):
        print("Case #%d: %d" % (self.index, self.switches))


state = 'num_cases'
idx   = 1
cases = []
f = open('p1_input.txt')
for line in f:
    if line.strip() == '': continue
    if state == 'num_cases':
        cases = [None] * int(line.strip())
        state = 'new_case'
    elif state == 'new_case':
        current_case = Case(idx, int(line.strip()))
        cases[idx - 1] = current_case
        idx += 1
        state = 'get_engines'
    elif state == 'get_engines':
        state = current_case.add_engine(line.strip())
    elif state == 'get_num_requests':
        current_case.num_requests = int(line.strip())
        if current_case.num_requests == 0:
            state = 'new_case'
        else: state = 'get_requests'
    elif state == 'get_requests':
        state = current_case.add_query(line.strip())
    
f.close()

for c in cases:
    c.to_s()
