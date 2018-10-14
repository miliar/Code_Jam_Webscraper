#!/usr/bin/env python
# -*- coding: utf-8 -*-


class War(object):
    def __init__(self, N, Naomi_masses, Ken_masses):
        self.N = N
        self.Naomi_masses = sorted(Naomi_masses)
        self.Ken_masses = sorted(Ken_masses)
        self.Naomi_remain = [e for e in self.Naomi_masses]
        self.Ken_remain = [e for e in self.Ken_masses]
        self.Naomi_real_score = 0
        self.Naomi_deceitful_score = 0

    def p(self):
        print 'N: %d' % self.N
        print 'Naomi_masses: %s' % self.Naomi_masses
        print 'Ken_masses: %s' % self.Ken_masses

    def Ken_choose(self, k):
        for i, e in enumerate(self.Ken_remain):
            if e > k:
                return i
        return -1

    def real_war(self):
        for e in self.Naomi_remain:
            i = self.Ken_choose(e)
            if i == -1:
                self.Naomi_real_score += len(self.Ken_remain)
                break
            else:
                del self.Ken_remain[i]
        self.Ken_remain = [e for e in self.Ken_masses]
        return None

    # def deceitful_war(self):
    #     for e in self.Naomi_remain:
    #         if e > self.Ken_remain[-1]:
    #             self.Naomi_deceitful_score += len(self.Ken_remain)
    #             break
    #         else:
    #             self.Ken_remain.pop()
    #     self.Ken_remain = [e for e in self.Ken_masses]
    #     return None

    def deceitful_war(self):
        i = 0
        j = len(self.Naomi_remain) - 1
        k = len(self.Ken_remain) - 1
        while k >= 0:
            if self.Naomi_remain[i] < self.Ken_remain[0]:
                i += 1
                k -= 1
            elif self.Naomi_remain[j] > self.Ken_remain[k]:
                self.Naomi_deceitful_score += 1
                j -= 1
                k -= 1
            else:
                i += 1
                k -= 1
        return None

    def run(self, f_out, i):
        self.deceitful_war()
        self.real_war()
        f_out.write('Case #%d: %d %d\n'% (i, self.Naomi_deceitful_score, self.Naomi_real_score))
        print self.Naomi_deceitful_score, ' ', self.Naomi_real_score


def execute(in_path, out_path):
    f_in = open(in_path)
    f_out = open(out_path, 'wb')
    T = int(f_in.readline().strip())
    print T
    for i in range(T):
        N = int(f_in.readline().strip())
        line = f_in.readline().strip()
        Naomi_masses = [float(e) for e in line.split()]
        line = f_in.readline().strip()
        Ken_masses = [float(e) for e in line.split()]
        war = War(N, Naomi_masses, Ken_masses)
        # war.p()
        war.run(f_out, i + 1)



    f_in.close()
    f_out.close()



def main():
    # execute('sample.in', 'sample.out')
    # execute('small.in', 'small.out')
    execute('large.in', 'large.out')


if __name__ == '__main__':
    main()