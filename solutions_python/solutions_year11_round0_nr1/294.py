'''
Created on 2010/05/08

@author: banana
'''

if __name__ == '__main__':
    pass

fp = open("A-large.in", "r")

lines = fp.readlines()

T = int(lines[0])

fpout = open("A-large.txt", "w")

for t in range(1, T+1):
    l = lines[t].split()[1:]
    listo = []
    listb = []
    for i in range(len(l)/2):
        if l[i*2] == "O":
            listo.append( (i, int(l[i*2 + 1])) )
        else:
            listb.append( (i, int(l[i*2 + 1])) )

    
    pos_o = 1
    if len(listo) == 0:
        next_pos_o = 1
        order_o = 999
    else:
        order_o = listo[0][0]
        next_pos_o = listo[0][1]
        listo.pop(0)

    pos_b = 1
    if len(listb) == 0:
        next_pos_b = 1
        order_b = 999
    else:
        order_b = listb[0][0]
        next_pos_b = listb[0][1]
        listb.pop(0)
    
    i = 0
    next_order_o = order_o
    next_order_b = order_b
    
    while order_o != 999 or order_b != 999:
        if pos_o == next_pos_o:
            if order_o < order_b:
                #push button!
                if len(listo) == 0:
                    next_order_o = 999
                else:
                    next_order_o = listo[0][0]
                    next_pos_o = listo[0][1]
                    listo.pop(0)
        else:
            # move
            if pos_o < next_pos_o:
                pos_o = pos_o + 1
            else:
                pos_o = pos_o - 1                

        if pos_b == next_pos_b:
            if order_b < order_o:
                #push button!
                if len(listb) == 0:
                    next_order_b = 999
                else:
                    next_order_b = listb[0][0]
                    next_pos_b = listb[0][1]
                    listb.pop(0)
        else:
            # move
            if pos_b < next_pos_b:
                pos_b = pos_b + 1
            else:
                pos_b = pos_b - 1 
        
        i = i + 1
#        print "O:", pos_o, " B:", pos_b
        if next_order_o != order_o:
            order_o = next_order_o
        if next_order_b != order_b:
            order_b = next_order_b                
        
    fpout.write("Case #%d: %d\n"%(t, i))    
        
        
fpout.close()