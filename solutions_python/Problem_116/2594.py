#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  a.py
#  
#  Copyright 2013 Matyas Kocsis <matyilona@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def read_in():
    z = [f.readline().strip() for i in range(4)]
    return(z)

f = open('A-large.in','r')
now = []
was_dot = False
x_won = False
y_won = False

def check_row(i):
    global now, was_dot, x_won, y_won
    y = sorted(list(now[i]))
    check(y)

def check_col(i):
    global now, was_dot, x_won, y_won
    y = sorted([now[j][i] for j in range(4)])
    check(y)

def check_dia():
    y = sorted([now[j][j] for j in range(4)])
    check(y)
    y = sorted([now[j][3-j] for j in range(4)])
    check(y)

def check(y):
    global now, was_dot, x_won, y_won
    y = ''.join(y)
    #~ print(y)
    if (y=="TXXX") or (y=="XXXX"):
        x_won = True
        #~ print("Xwon")
    elif (y == "OOOT") or (y == "OOOO"):
        y_won = True
        #~ print("Ywon")
    elif y[0] == ".":
        was_dot = True
        #~ print("ThereIsDot", was_dot)


def main():
    global now, was_dot, x_won, y_won
    n = int(f.readline().strip())
    g = open('al.out','w')
    for j in range(n):
        now = read_in()
        for i in range(4):
            check_row(i)
            check_col(i)
        check_dia()
        end="undef"
        if x_won:
            end = "X won"
        elif y_won:
            end = "O won"
        elif was_dot:
            end = "Game has not completed"
        else:
            end = "Draw"
        #~ print(was_dot)
        g.write('Case #'+str(j+1)+': '+end+'\n')
        x_won = y_won = was_dot = False
        f.readline()
    g.close()
    return 0

if __name__ == '__main__':
    main()

