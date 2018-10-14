import sys

if __name__ == "__main__":
    input = sys.stdin.read()
    input = input.split('\n')

    #print input

    T = int(input[0].strip())
    #print T
        
    casenum = 1
    for item in input[1:-1]:
        orders = item.split(' ')
        n = int(orders[0])
        orange_pos = 1
        blue_pos = 1
        orange = []
        blue = []
        overall = []
        for i in range(n):
            if orders[1+2*i] == "O":
                orange += [int(orders[1+2*i+1])]
            else: 
                blue += [int(orders[1+2*i+1])]
            overall += (orders[1+2*i], int(orders[1+2*i+1]))
        #print orange
        #print blue
        #print overall
        counter = 0
        while (len(overall) > 0):
            #print orange_pos
            #print blue_pos
            ormove = False
            blmove = False
            if overall[0] == 'O' and orange_pos == overall[1]:
                ormove = True
                orange = orange[1:]
                overall = overall[2:]
            elif overall[0] == 'B' and blue_pos == overall[1]:
                blmove = True
                blue = blue[1:]
                overall = overall[2:]
            if not ormove and len(orange) > 0:
                if orange[0] > orange_pos:
                    #print orange[0]
                    orange_pos += 1
                elif orange[0] < orange_pos:
                    orange_pos += -1
            if not blmove and len(blue) > 0:
                if blue[0] > blue_pos:
                    #print blue[0]
                    blue_pos += 1
                elif blue[0] < blue_pos:
                    blue_pos += -1
            counter += 1
        print "Case #%i: %i" % (casenum, counter)
        casenum += 1
