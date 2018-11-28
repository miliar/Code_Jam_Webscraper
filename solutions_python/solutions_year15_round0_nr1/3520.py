#!/usr/bin/env python

"""
  Author:  Yeison Cardona --<yeison.eng@gmail.com>
  Purpose: Qualification Code Jam
  Created: 10/04/15
"""

import sys
filename = sys.argv[1]
filename_out = sys.argv[1].replace(".in", ".out")


########################################################################
# Problem A.
class StandingOvation:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        data_set = self.read_file()

        output = []
        index = 1
        file_out = open(filename_out, "w")
        for group in data_set:
            value = self.get_inviteds(*group)
            file_out.write("Case #%s: %d\n"%(index, value))
            index += 1
        file_out.close()

    #----------------------------------------------------------------------
    def read_file(self):
        """Parse file input."""

        file = open(filename)
        lines = file.readlines()
        file.close()

        T = int(lines[0])
        audience = lines[1:T+1]

        data_set = []
        for shyness in audience:
            max_, shy_ = shyness.split()
            data_set.append((int(max_), list(enumerate(shy_))))
            pass

        return data_set

    #----------------------------------------------------------------------
    def get_inviteds(self, T, i):
        """"""
        clapping = 0
        clapping_extra = 0
        for n in i:
            if int(n[1]) > 0: must_clapping = n[0]
            else: must_clapping = 0
            if clapping < must_clapping:
                clapping_extra += (must_clapping - clapping)
                clapping += clapping_extra
            clapping += int(n[1])

        return clapping_extra


if __name__ == '__main__':
    StandingOvation()
