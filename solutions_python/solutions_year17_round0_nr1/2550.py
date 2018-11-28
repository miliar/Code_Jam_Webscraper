#!/usr/bin/python3
# Copyright (C) 2017 Sayutin Dmitry.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 3
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <http://www.gnu.org/licenses/>.

def main():
    t = int(input())
    for tc in range(t):
        line, k = input().split()
        k = int(k)
        line = [(ch == '+') for ch in line]
        
        fail = False
        ans  = 0
        for i in range(len(line)):
            if line[i] == False:
                if i + k > len(line):
                    fail = True
                    break
                else:
                    for j in range(k):
                        line[i + j] = not line[i + j]
                    ans += 1
        
        out = "IMPOSSIBLE" if fail else str(ans)
        print("Case #{}: {}".format(tc + 1, out))


main()
