#!/usr/bin/python
#coding:utf8

def robots(A):
    blue   = []
    orange = []
    foo = None
    seq = []
    for i in A:
        if i == "O":
            foo = orange
            seq.append("O")
        elif i == "B":
            foo = blue
            seq.append("B")
        else:
            foo.append(int(i))
    steps = 0
    #print orange, blue
    #print seq
    pos_blue = pos_orange = 1
    while blue or orange:
        steps += 1
        apertou = False
        #print "round", steps
        if blue:
            if seq[0] == "B" and pos_blue == blue[0]:
                #print "B aperta butao", pos_blue
                apertou = True
                blue.pop(0)
            else:
                #print "b move from to", pos_blue, blue[0]
                pos_blue += cmp(blue[0], pos_blue)
        
        if orange:
            if seq[0] == "O" and pos_orange == orange[0]:
                #print "O aperta butao", pos_orange
                apertou = True
                orange.pop(0)
            else:    
                #print "o move from to", pos_orange, orange[0]
                pos_orange += cmp(orange[0],pos_orange)

        if apertou:
            seq.pop(0)
             
    return steps





if __name__ == '__main__':
    num = input()

    for i in range(num):
        foo = raw_input()
        print "Case #%s: %s"% (i+1, robots(foo.split()[1:]))
