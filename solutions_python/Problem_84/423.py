#!/usr/bin/env python

def print_solution((w, h), img):
    for y in xrange(h):
        for x in xrange(w):
            c = img[y][x] == img[y+1][x] == img[y][x+1] == img[y+1][x+1] == '#'
            if c:
                img[y][x], img[y+1][x], img[y][x+1], img[y+1][x+1] = '/', '\\', '\\', '/'
    
    f = lambda a: ''.join(a[:w])
    img = [f(a) for a in img]
    if '#' in f(img):
        print 'Impossible'
    else:
        for a in img[:h]:
            print a

def main():
    T = int(raw_input())
    for x, i in enumerate(xrange(T)):
        h, w = map(int, raw_input().split(' '))
        img = []
        for j in xrange(h):
            img.append([i for i in raw_input()] + ['.'])
        img.append(['.']*(w+1))
        #print img
        print 'Case #{0}:'.format(x+1)
        print_solution((w, h), img)

if __name__ == '__main__':
    main()
