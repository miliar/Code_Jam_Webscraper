#-------------------------------------------------------------------------------
# Name:        Magic Trick
# Purpose:
#
# Author:      udonko
#
# Created:     12/04/2014
# Copyright:   (c) udonko 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# python3.3.2

import sys
import collections


MagicStatus = collections.namedtuple("MagicStatus",['answer','matrix'])

class OneTest:
    def __init__(self, magicStatus1, magicStatus2):
        self.status1 = magicStatus1
        self.status2 = magicStatus2
        self.result = None
        self.resolve()
    def resolve(self):
        firstrow = self.status1.matrix[ self.status1.answer - 1 ]
        secondrow = self.status2.matrix[ self.status2.answer - 1 ]
        result_set = set(firstrow) & set(secondrow)
        if len(result_set) == 1:
            self.result = str(result_set.pop())
        elif len(result_set) > 1:
            self.result = "Bad magician!"
        else:
            self.result = "Volunteer cheated!"
    def getAnswer(self):
        return self.result

class Resolve:
    def __init__(self, filename):
        with open(filename, "r") as infile:
            tmp = infile.readline();
            self.t =int(tmp)
            def readStatus():
                tmp = infile.readline();
                answer = int(tmp)
                mat = []
                for j in range(4):
                    tmp = infile.readline();
                    row = tuple(map(int,tmp.split()))
                    mat.append(row)
                status = MagicStatus(answer,mat)
                return status
            with open(filename+"out.txt","w") as outfile:
                for i in range(self.t):

                    onetest =  OneTest(readStatus(),readStatus())
                    tmp = "Case #{0}: {1}".format(i+1 , onetest.getAnswer() + "\n")
                    outfile.write(tmp)


def main():
    reso = Resolve("A-small-attempt1.in")

if __name__ == '__main__':
    main()
