#! /usr/bin/python2.6
# coding: utf-8

# 'it cannot cover white tiles, and it cannot go outside the picture'

# backtrack

def putable(img, r, c, i, j):
    if i+1 >= r:
        return False
    if img[i+0][j:j+2] != ['#', '#']:
        return False
    if img[i+1][j:j+2] != ['#', '#']:
        return False
    return True

def bluetiles(img):
    return sum(row.count('#') for row in img)

def putbase(img, r, c, i, j, c1, c2):
    img[i+0][j+0] = c1
    img[i+0][j+1] = c2
    img[i+1][j+0] = c2
    img[i+1][j+1] = c1

def put(img, r, c, i, j):
    putbase(img, r, c, i, j, '/', '\\')

def unput(img, r, c, i, j):
    putbase(img, r, c, i, j, '#', '#')

def show(img):
    print '\n'.join(''.join(row) for row in img)

def gonext(img, r, c, i, j):
    jj = 0 if j+2 >= c else j+2
    ii = i+1 if j+2 >= c else i
    if ii >= r:
        return img if bluetiles(img) == 0 else None
    res = check(img, r, c, ii, jj)
    return res

def check(img, r, c, si=0, sj=0):
    if bluetiles(img) == 0:
        return img
    
    for i in xrange(si, r):
        for j in xrange(sj if i==si else 0, c):
            if not putable(img, r, c, i, j):
                #print 'not putable',i,j
                continue
            put(img, r, c, i, j)
            #print 'put at',i,j; show(img)
            if gonext(img, r, c, i, j):
                return img
            #print 'unput at',i,j; show(img)
            unput(img, r, c, i, j)
            if gonext(img, r, c, i, j):
                return img
        

ntcase = int(raw_input())
for tcase in range(1, ntcase + 1):
    r,c = map(int, raw_input().split())
    img = [[ch for ch in raw_input()] for row in range(r)]
    result = check(img, r, c)
    print 'Case #%d:' % tcase
    if result is None:
        print 'Impossible'
    else:
        print '\n'.join(''.join(row) for row in img)
