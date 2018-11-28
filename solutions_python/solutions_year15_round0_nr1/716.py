#!/usr/bin/env python
# encoding: utf-8
__author__ = 'rui'

cases = []

class TestCase(object):
    def __init__(self, id, shyness, audience):
        self.id = id
        self.shyness = shyness
        self.audience = audience.strip()
    def get_ret(self):
        ret = 0
        current = 0
        cnt = 0
        # print self.audience, len(self.audience), self.shyness
        for c in self.audience:
            if cnt == 0:
                current += int(c)
            else:
                # print '\t',current, cnt
                if current < cnt:
                    ret += cnt - current
                    current += cnt - current
                current += int(c)
            cnt += 1
        # print ret
        return 'Case #%d: %d' % (self.id, ret)

if __name__ == '__main__':
    with open('A-large.in') as f:
        lines = f.readlines()
        size = int(lines[0])
        id = 1
        for line in lines[1:]:
            shyness, audience = line.split(' ')
            cases.append(TestCase(id, shyness, audience))
            id+=1
    f = open('A-large.out','w')
    for case in cases:
        f.write(case.get_ret() + '\n')