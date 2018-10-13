import sys

def main():
    f = open('D-small-attempt3.in', 'r')
    #f = open('rt.txt', 'r')
    pw = open('out.in', 'w')

    n = int(f.readline())

    case = 1
    
    for x in range(0, n):
        x, r, c = f.readline().strip().split()

        x,r,c = int(x), int(r), int(c)
        
        if x == 1:
            pw.write('Case #' + str(case) + ": GABRIEL")
            pw.write('\n')
        elif x == 2:
            row = 1
            col = 2

            if c % col == 0 or r % 2 == 0:
                pw.write('Case #' + str(case) + ": GABRIEL")
                pw.write('\n')
            else:
                pw.write('Case #' + str(case) + ": RICHARD")
                pw.write('\n')
        elif x == 3:
            gabwon = True
            
            for p in range(1,3):
                if p == 1:
                    if c % 3 != 0 and r % 3 != 0:
                        gabwon = False
                        break
                elif p==2:
                    row = 2
                    col = 1

                    if row > r:
                        gabwon = False
                        break
                    elif row == r:
                        if c == 1:
                            gabwon = False
                            break
                        else:
                            rem = (r*c) - 3
                            if rem % 3 != 0:
                                gabwonn = False
                                break
                    else:
                        if c == 1:
                            gabwon = False
                            break
                        if (r*c) % 3 != 0 :
                            gabwon = False
                            break
                        
            if gabwon:
                pw.write('Case #' + str(case) + ": GABRIEL")
                pw.write('\n')
            else:
                pw.write('Case #' + str(case) + ": RICHARD")
                pw.write('\n')

            
                    
        elif x == 4:
            gabwon = True
            
            for p in range(1, 5):
                if p == 1:
                    if c % 4 != 0 and r % 4 != 0:
                        gabwon = False
                        break
                elif p == 2:
                    row = 2
                    col = 2

                    if row > r or col > c:
                        gabwon = False
                        break
                    else:
                        if (r*c) % 4 != 0:
                            gabwon = False
                            break
                elif p == 3:
                    row = 3
                    
                    #first case
                    if row > r and row > c:
                        gabwon = False
                        break
                    elif row > r and row == c:
                        gabwon = False
                        break
                    elif row > r and row < c and c % 4 != 0:
                        gabwon = False
                        break
                    
                    if (r*c)%4 != 0:
                        gabwon = False
                        break
                    
                    #second case
                    if row > r:
                        gabwon = False
                        break
                    else:
                        if c == 2 or (r *c) % 4 != 0:
                            gabwon = False
                            break
                        
            if gabwon:
                pw.write('Case #' + str(case) + ": GABRIEL")
                pw.write('\n')
            else:
                pw.write('Case #' + str(case) + ": RICHARD")
                pw.write('\n')
                
                            
        case += 1
            

if __name__ == '__main__':
    main()
