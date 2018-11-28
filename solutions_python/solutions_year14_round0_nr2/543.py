#!/usr/bin/python

# Dan Seminara

import fileinput

def main():
    for i,line in enumerate(fileinput.input()):
        if i == 0:
            continue
        (c,f,x) = [float(j) for j in line.split(' ')]
        cookies = 0
        r = 2
        t = 0
        # find which is faster farm then win, or just win
        # if farm, buy farm and start again
        # else calc and done
        while True:
            time_from_current = (x-cookies)/r
            time_with_farm = (c-cookies)/r + (x)/(r+f)
            if time_with_farm < time_from_current:
                t += (c-cookies)/r
                r += f
                cookies = 0
            else:
                t += (x-cookies)/r
                break
        print('Case #%d: %.7f' % (i,t))
            

if __name__ == '__main__':
    main()