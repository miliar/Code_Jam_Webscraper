#Problem A. Bot Trust
#url: http://code.google.com/codejam/contest/dashboard?c=975485

def read_type(foo): return foo(raw_input())
def read_array(foo): return [foo(x) for x in raw_input().split()]

def bot_log(log_size, pushlog):
    time=0
    posO, posB = 1, 1
    orange=[]
    blue=[]
    for x in pushlog:
        (col, num)=x
        if col =='O': orange.append(int(num))
        else: blue.append(int(num))

    #print orange, blue
    o = 0
    b = 0
   
    for x in pushlog:
        (col, strnum)=x
        num = int(strnum)

        i=0
        while 1: #i < 1000:
#            print orange[o], posO, blue[b], posB, time, num, i, x
            i += 1
            time += 1

            flagO, flagB = False, False

            if orange:
                if posO != orange[o]:
                    if posO < orange[o]: posO += 1
#                    elif posO > orange[o]: posO -= 1
                    else: posO -= 1
                else:
                    flagO = True

            if blue:
                if posB != blue[b]:
                    if posB < blue[b]: posB += 1
                    else: posB -= 1
                else:
                    flagB = True

            if flagO and col == 'O' and posO == num:
                    break

            if flagB and col == 'B' and posB == num:
                    break        

        if col == 'O' and o < len(orange)-1: o += 1
        if col == 'B' and b < len(blue)-1  : b += 1

    return time

##print bot_log(4, [['O', '2'], ['B', '1'], ['B', '2'],['O', '4']])
##print bot_log(3, [['O', '5'],['O', '8'],['B','100']])
##print bot_log(2, [['B','2'],['B','1']])

cases = read_type(int)
for c in range(cases):
    entry = read_array(str)
    log_size  = int(entry[0])
    i=1
    inp=[]
    while i < 2*log_size:
        col, num = entry[i], entry[i+1]
        i += 2
        inp.append((col,num))
    print 'Case #%d: %d' % (c+1, bot_log(log_size, inp))
    
    
    
