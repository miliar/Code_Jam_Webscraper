#!/usr/bin/env python

def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def list_char_input():
    return list(raw_input())

def table_int_input(h):
    return [list_int_input() for i in range(h)]

def table_char_input(h):
    return [list_char_input() for i in range(h)]

def train_loop():
    #word = raw_input()
    #word2 = raw_input()
    
    a = 10
    while a != 0:
        a = a - 1
        print a,
        if a>5:
            print "Big Num"
        elif a%2==0:
            print "Even"
        else:
            print "Shit"
    #print word + " " + word2
    
def train_list():
    cats = ["one","two","three",\
            "four","five"]
    #cats.append("append")
    #del cats[0]
    
    #print cats[0]
    #print cats[-1]
    
    for cat in cats[1:3]:
        print cat,
    print ""
    
    cats[0:2] = [cats[0]+" "+cats[1]]
    
    cats.insert(2,"2.5")
    cats.extend(["last","lasttt"])
    
    for cat in cats:
        print cat

def train_dic():
    ages = {}
    ages['eig'] = 34
    ages['x'] = 2
    
    print ages['x']
    
class Pair:
    def __int__(self,x,y):
        self.x = x
        self.y = y

def train_class():
    pList = []
    pList.append((1,10))
    pList.append((6,60))
    pList.append((2,20))
    pList.append((5,50))
    
    pList = sorted(pList, key = lambda p:p[0])
    
    for p in pList:
        print p[1]

def train_math():
    x = 5
    y = 2.0
    print x/y
    print x//y
    print x**y

def solve():
    R = int_input()
    C = int_input()
    
    table = table_char_input()
    
    

def solve(c):
    [R,C] = list_int_input()
    
    table = table_char_input(R)
    
    print 'Case #%d:' % (c),
    
    for i in range(R-1):
        for j in range(C-1):
            if table[i][j]=='#' and table[i+1][j]=='#' and table[i][j+1]=='#' and table[i+1][j+1]=='#':
                table[i][j]='/'
                table[i][j+1]='\\'
                table[i+1][j]='\\'
                table[i+1][j+1]='/'
    print ""
    for i in range(R):
        for j in range(C):
            if table[i][j]=='#':
                print "Impossible"
                return
    for i in range(R):
        print ''.join(table[i])

def main():
    for i in range(int_input()):
        solve(i+1)
    

main()