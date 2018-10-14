# -*- coding: utf-8 -*-
# Author: Fernando Gomez
# Mail: metaforaideas@gmail.com

import sys


class StandingOvation:
    path = ""
    shynessLevels = []
    friends = []

    def input(self):
        self.path = sys.argv[1]
        fileinput = open(self.path, 'r')
        T = int(fileinput.readline())
        for l in range(T):
            line = fileinput.readline()
            self.shynessLevels.append(line.replace('\n', '').split(' '))

    def solve(self):
        for shynessLevel in self.shynessLevels:
            stadingMembers = 0
            friends = 0
            maximumShynessLevel = shynessLevel[0]
            membersPerLevel = [int(sl) for sl in shynessLevel[1]]

            for level, members in enumerate(membersPerLevel):
                stadingMembers += members
                if stadingMembers + friends == maximumShynessLevel:
                    break
                elif stadingMembers + friends == level:
                    friends += 1

            self.friends.append(friends)

    def output(self):
        filename = self.path.split('.')
        filename.insert(-1, 'out')
        filename = '.'.join(filename)
        fileoutput = file(filename, 'w')

        for idx, friend in enumerate(self.friends):
            fileoutput.write('Case #%i: %i\n' % (idx + 1, friend))


def main():
    standingOvation = StandingOvation()
    standingOvation.input()
    standingOvation.solve()
    standingOvation.output()

if __name__ == '__main__':
    main()
