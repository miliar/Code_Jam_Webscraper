#-*- encoding: utf8 -*-

import sys
import pdb

class ScoreDance(object):

    def __init__(self, tc_params):
        tc_p = map(int, tc_params.split())
        self.N = tc_p[0]
        self.S = tc_p[1]
        self.p = tc_p[2]
        self.ti = tc_p[3:]

        self.nb_token_S = int(self.S)
        
        self.mg = 0

        self.pr = {}
        for g_i in range(self.N):
            self.set_possible_results(g_i)

    def _normalize_score(self, score):
        return score if score >= 0 else 0

    def set_possible_results(self, g_i):
        """ Find all the possible results from @total_points
        and seperate those which are surprising.
        """
        total_points = self.ti[g_i]
        mid = total_points/3
        pr_n = []
        pr_s = []
        range_diff = range(-1, 2+1)
        for x in range_diff:
            for y in range_diff:
                for z in range_diff:
                    new_set = map(self._normalize_score, [mid+x, mid+y, mid+z])
                    if sum(new_set) == total_points:
                        new_set.sort()
                        if new_set[2] - new_set[0] <= 1:
                            pr_n.append(tuple(new_set))
                            #print "(%d|%d|%d) : %s" % (x, y, z, new_set)
                        elif new_set[2] - new_set[0] <= 2:
                            pr_s.append(tuple(new_set))
                            #print "(%d|%d|%d) : %s *" % (x, y, z, new_set)
        
        f_set_n = set(pr_n)
        f_set_s = set(pr_s)
        #print "Final Normal Set for (%d:%d) : %s" % (g_i, total_points, f_set_n)
        #print "Final Suprising Set for (%d:%d) : %s\n" % (g_i, total_points, f_set_s)
        #return len(f_set_n)+len(f_set_s)
        self.pr[g_i] = (pr_n[0], pr_s[0] if pr_s else (0,0,0))

    def get_best_result(self, g_i, with_surprise=False):
        #return self.pr[g_i][int(with_surprise)][2]
        if with_surprise:
            return max(self.pr[g_i][1]) #if self.pr[g_i]
        else:
            return max(self.pr[g_i][0])
    
    def compute_best_results(self):
        #print "[DEBUG:compute_best_results] N : %d" % self.N
        #print "[DEBUG:compute_best_results] S : %d" % self.S
        #print "[DEBUG:compute_best_results] p : %d" % self.p
        #print "[DEBUG:compute_best_results] nb_token_S : %d" % self.nb_token_S
        #print "[DEBUG:compute_best_results]: mg : %d" % self.mg
        # First round : only the normal results
        for g_i in range(self.N):
            if self.get_best_result(g_i, with_surprise=False) >= self.p:
                self.mg += 1
                self.pr.pop(g_i)
            #print "R1(%d): mg: %d , nb_token_S : %d" % (g_i, self.mg, self.nb_token_S)
        # Second round : only the surprising results for the remaining dancers
        for g_i in self.pr.keys():
            if self.get_best_result(g_i, with_surprise=True) >= self.p and self.nb_token_S > 0:
                self.mg += 1
                self.nb_token_S -= 1
            #print "R2(%d): mg: %d , nb_token_S : %d" % (g_i, self.mg, self.nb_token_S)
            if self.nb_token_S < 1:
                break
        return self.mg

def get_possible_results(total_points):
    """ Find all the possible results from @total_points
    and seperate those which are surprising.
    One can optimize ...
    """
    mid = total_points/3
    pr_n = []
    pr_s = []
    range_diff = range(-1, 2+1)
    for x in range_diff:
        for y in range_diff:
            for z in range_diff:
                if ((3 * mid) + x + y + z) == total_points:
                    new_set = [mid+x, mid+y, mid+z]
                    new_set.sort()
                    if new_set[2] - new_set[0] <= 1:
                        pr_n.append(tuple(new_set))
                        print "(%d|%d|%d) : %s" % (x, y, z, new_set)
                    elif new_set[2] - new_set[0] <= 2:
                        pr_s.append(tuple(new_set))
                        print "(%d|%d|%d) : %s *" % (x, y, z, new_set)
    
    f_set_n = set(pr_n)
    f_set_s = set(pr_s)
    print "Final Normal Set for %d : %s" % (total_points, f_set_n)
    print "Final Suprising Set for %d : %s\n" % (total_points, f_set_s)
    return len(f_set_n)+len(f_set_s)

def do_helper():
    for i in range(30):
        lpr = get_possible_results(i)
        if lpr != 2:
            print "#%d : %d" %(i, lpr)
            print "Waouh ... seems going wrong"

def do_it():
    all_tc = sys.stdin.readlines()
    for tc_n in range(1, int(all_tc[0]) + 1):
        dancegame = ScoreDance(all_tc[tc_n])
        max_score = dancegame.compute_best_results()
        print "Case #%d: %d" %(tc_n, max_score)

if __name__ == '__main__':
    do_it()
