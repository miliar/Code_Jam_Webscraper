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

import sys

def check(n):
    s = str(n)
    for j in range(1, len(s)):
        if ord(s[j]) < ord(s[j - 1]):
            return False
    return True

def solve_slow(n):
    for i in range(n, 0, -1):
        if check(i):
            return i
    return None # impossible

def solve(n):
    if check(n):
        return n
    
    s = str(n)
    best = -1
    for compref in range(len(s)):
        if compref != 0 and ord(s[compref - 1]) > ord(s[compref]):
            break
        minst = 0 if compref == 0 else int(s[compref - 1])
        mx = int(s[compref]) - 1
        
        if mx >= minst:
            best = max(best, int(s[:compref] + str(mx) + '9' * (len(s) - compref - 1)))
    return best


def self_check():
    for i in range(1, 1005):
        if solve(i) != solve_slow(i):
            print("!!!! Failed test", i, solve(i), solve_slow(i))
            sys.exit(1)
    
def main():
    t = int(input())
    for tc in range(t):
        n = int(input())
        print("Case #{}: {}".format(tc + 1, solve(n)))

self_check()
main()
