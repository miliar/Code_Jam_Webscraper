

def run():
    import string
    fp = open('c:\\B-large.in','r')
    cases = string.atoi(fp.readline())
    c = 1
    while (cases > 0):
        time = string.atoi(fp.readline())
        na, nb = map(string.atoi,fp.readline().split(' '))
        la = na
        lb = nb
        a = []
        b = []
        
        while (la > 0):
            start,end = fp.readline()[:-1].split(' ')
            start = string.atoi(start[0:2]) * 60 + string.atoi(start[3:5])
            end = string.atoi(end[0:2]) * 60 + string.atoi(end[3:5])+time
            a.append([start, 'd'])
            b.append([end,'a'])           
            la = la - 1

        while (lb > 0):
            start,end = fp.readline()[:-1].split(' ')
            start = string.atoi(start[0:2]) * 60 + string.atoi(start[3:5])
            end = string.atoi(end[0:2]) * 60 + string.atoi(end[3:5])+time
            b.append([start, 'd'])
            a.append([end,'a'])            
            lb = lb - 1
            
        a.sort()
        b.sort()

        left = 0
        right = 0
        #print a,b
        sl,sr = 0,0
        
        while (len(a) > 0 or len(b) > 0):
            if (len(a) > 0 and len(b) > 0):
                if (a[0][0] < b[0][0] or (a[0][0] == b[0][0] and a[0][1] == 'a')):
                    if a[0][1] == 'a':
                        left = left + 1
                        a.remove(a[0])
                    else:
                        left = left - 1
                        a.remove(a[0])
                else:
                    if b[0][1] == 'a':
                        right = right + 1
                        b.remove(b[0])
                    else:
                        right = right - 1
                        b.remove(b[0])
            elif (len(a) > 0):
                if a[0][1] == 'a':
                    left  = left + 1
                    a.remove(a[0])
                else:
                    left = left - 1
                    a.remove(a[0])
            else:
                if b[0][1] == 'a':
                    right = right + 1
                    b.remove(b[0])
                else:
                    right = right - 1
                    b.remove(b[0])
#            print left,right
            if (sl < -left):
                sl = -left
            if (sr < -right):
                sr = -right
                   
        
        
        print "Case #%d: %d %d" % (c,sl,sr)
        
        cases = cases - 1
        c = c+1 

        
run()        