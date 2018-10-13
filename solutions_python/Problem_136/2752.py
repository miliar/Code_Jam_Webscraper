__author__ = 'prigor'

from cStringIO import StringIO
import sys

class Input(object):
    def __init__(self, C, F, X, base_production=2.0):
        self.total_cookies = 0
        self.C = float(C)
        self.F = float(F) # Number of farms
        self.X = float(X)
        self.base_production = base_production

    def calculate(self):
        total_time = 0

        if self.C >= self.X:
            total_time = self.X/self.base_production
            #print self.X
            return total_time

        else:
            max_farms = int(round(self.X/self.C))+1
            num_farms = 0
            cur_time = 0
            while num_farms < max_farms:
                # Obtain the production rate
                production = self.base_production + num_farms*self.F

                # Should we buy a farm? Look ahead ...
                projected_time_with_nofarm = self.X/production
                projected_time_with_farm = self.X/(self.base_production + (num_farms+1.)*self.F)

                # What is the time before we are able to purchase farm?
                # It's when we are able to afford it at price C
                cur_time = self.C/production

                # Project: make more self.C to purchase one more farm + projected rate afterward
                with_farm = cur_time + projected_time_with_farm

                # Debug
                #print self.X, total_cookies, remaining_cookies, production, num_farms, cur_time, projected_time_with_farm, with_farm, projected_time_with_nofarm

                if with_farm > projected_time_with_nofarm:
                    total_time += projected_time_with_nofarm
                    break
                else:
                    num_farms += 1
                    total_time += cur_time

        #print total_cookies
        return total_time

ifilename = sys.argv[1]
ifile = file(ifilename, 'r')

N_cases = int(ifile.readline())

for case in range(N_cases):
    data_lines = ifile.readline()
    if not data_lines.strip(): continue

    C, F, X = map(lambda x: float(x), data_lines.split())

    i = Input(C, F, X)
    print "Case #%s: %s" % (case+1, i.calculate())

    #if case + 1 == 1: break

