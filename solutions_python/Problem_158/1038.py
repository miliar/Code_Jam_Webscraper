


def main():
    with open('omino.txt','r') as file:
    
        tCases = int(file.readline())
        case = 1
    
        while tCases > 0:
            line = file.readline()
            board = line.split()
            
            x = int(board[0])
            r = int(board[1])
            c = int(board[2])
                              
                
            if (r*c)%x != 0:
                print 'Case #' + str(case) + ': RICHARD'
                case = case + 1
                tCases = tCases - 1
                
            elif x==1:
                print 'Case #' + str(case) + ': GABRIEL'
                case = case + 1
                tCases = tCases - 1   
            
            elif r == 1 or c == 1:
                if x == 2 and ( r ==2 or c == 2):
                    print 'Case #' + str(case) + ': GABRIEL'
                elif x == 2 and ( r == 4 or c == 4):
                    print 'Case #' + str(case) + ': GABRIEL'
                else:
                    print 'Case #' + str(case) + ': RICHARD'
                
                case = case + 1
                tCases = tCases - 1
            
            elif x == 4:
                if r ==2 and c ==2:
                    print 'Case #' + str(case) + ': RICHARD'
                    case = case + 1
                    tCases = tCases - 1
                elif r == 2 and c ==4:
                    print 'Case #' + str(case) + ': RICHARD'
                    case = case + 1
                    tCases = tCases - 1
                elif r ==4 and c==2:
                    print 'Case #' + str(case) + ': RICHARD'
                    case = case + 1
                    tCases = tCases - 1
                else:
                    print 'Case #' + str(case) + ': GABRIEL'
                    case = case + 1
                    tCases = tCases - 1
                            
            else:
                print 'Case #' + str(case) + ': GABRIEL'
                case = case + 1
                tCases = tCases - 1
        

main()