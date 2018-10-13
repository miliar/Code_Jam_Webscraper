#!/usr/bin/python

import sys

class Button:
    def __init__(self, c, n):
        self.c = c
        self.n     = n
        self.final = 0
        self.move = 0

def botTrust(buttons):
    #construct button_array
    arr = buttons.split()
    num = int(arr[0]) * 2
    i = 1
    button_array = []
    while i < num:
        color = arr[i]
        number = int(arr[i + 1])
        button_array.append( Button(color, number) )
        i = i + 2
    
    final = {}
    last_btn = None
    last_same_color_btn = {'B': None, 'O': None}
    for b in button_array:
        if not last_btn:
            b.move = abs(b.n - 1)
            b.final = 1 + b.move
        elif last_btn.c == b.c:
            b.move = abs(b.n - last_btn.n)
            b.final = 1 + b.move + last_btn.final
        else:
            if not last_same_color_btn[b.c]:
                b.move = abs(b.n - 1)
                last_final = 0
                
            else:
                b.move = abs(last_same_color_btn[b.c].n - b.n)
                last_final = last_same_color_btn[b.c].final
            b.final = 1 + max(b.move + last_final, 
                              last_btn.final)
        last_same_color_btn[b.c] = b
        last_btn = b
    #dbg
    #for b in button_array:
    #    print "%s%d, M: %d, F: %d" % (b.c, b.n, b.move, b.final)
    return button_array[len(button_array) - 1].final

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        line = f.readline().strip()
        result = botTrust(line)
        print "Case #%d: %s" % (i + 1, result)
        
if __name__ == "__main__":
    sys.exit(main())
