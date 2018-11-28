import re
import logging

LOG = logging.getLogger(__name__)


class Ovationer(object):

    tc_reg = re.compile(r'(\d+)\s+(\d+)\s*$')

    def __init__(self, fin):
        self.fin = fin
        self.t = int(fin.readline().strip())
        LOG.debug("T = %d", self.t)

    def execute_test_cases(self):
        for i in range(self.t):
            test_args = self.get_next_test()
            res = self.add_ovation(*test_args)
            print('Case #%d: %d' % (i+1, res[2]))

    def get_next_test(self):
        tc_line = self.fin.readline().strip()
        if not tc_line or tc_line == '':
            return None
        matchobj = self.tc_reg.match(tc_line)
        if matchobj is not None:
            s_max = int(matchobj.group(1))
            p = matchobj.group(2)
            LOG.debug('s_max = %d, p = %s', s_max, p)
            return (s_max, p)
        return None

    def ovation(self, s_max, p, r=0, n_prev=0, p_tot=0):
        LOG.debug('ovation: %d, %s, %d, %d', s_max, p, r, n_prev)

        if r >= 0 and r <= s_max:
            pr = int(p[r])
            LOG.debug('pr = %d', pr)
            if r == 0:
                return self.ovation(s_max, p, r+1, pr, p_tot+pr)
            else:
                if n_prev >= r:
                    return self.ovation(s_max, p, r+1, n_prev + pr, p_tot+pr)
                else:
                    return self.ovation(s_max, p, r+1, n_prev, p_tot+pr)
        elif r == s_max + 1:
            LOG.info('n_standing = %d', n_prev)
            LOG.info('n_total = %d', p_tot)
            return (n_prev, p_tot)
        else:
            raise ValueError('r must be >=0 and <= s_max')

    def add_ovation(self, s_max, p, r=0, n_prev=0, p_new=0, p_tot=0):
        LOG.debug('add_ovation: %d, %s, %d, %d, %d, %d', s_max, p, r, n_prev, p_new, p_tot)
        while r <= s_max + 1:
            if r >= 0 and r <= s_max:
                pr = int(p[r])
                LOG.debug('pr = %d', pr)

                if r == 0:
                    ''' First round
                    '''
                    LOG.debug('First round')
                    r += 1
                    n_prev = pr
                    p_tot += pr
                    #return self.add_ovation(s_max, p, r+1, pr, p_new, p_tot + pr)
                else:
                    ''' The usual case
                    '''
                    LOG.debug('The usual case')
                    # Will anybody stand up in this round?
                    shortfall = r - n_prev
                    LOG.debug('shortfall = %d', shortfall)
                    if shortfall > 0:
                        n_prev += shortfall
                        p_new += shortfall
                    r += 1
                    n_prev += pr
                    p_tot += pr
                    #return self.add_ovation(s_max, p, r+1, n_prev + pr, p_new, p_tot + pr)
            elif r == s_max + 1:
                ''' Return the result.
                '''
                LOG.info('Return the result')
                LOG.info('n_standing  = %d', n_prev)
                LOG.info('n_totalorig = %d', p_tot)
                LOG.info('n_added     = %d', p_new)
                return (n_prev, p_tot, p_new)
            else:
                raise ValueError('r must be >=0 and <= s_max')

if __name__=='__main__':
    import sys
    fin = open(sys.argv[1], 'r')
    try:
        ov = Ovationer(fin)
        ov.execute_test_cases()
    finally:
        fin.close()
