T = int(raw_input())

def char(string, char, index):
        return string[:index] + char + string[index+1:]

for tc in range(0, T):
        N = raw_input()
#        print N
        lenN = len(N)

        #Loop from last digit to second digit
        for nc in range(lenN-1, 0, -1):

                if N[nc] < N[nc-1]:
                        N = char(N, '9', nc)
                        
                        #Fill nine
                        j = nc + 1
                        while j<lenN and N[j] != '9':
                                N =char(N, '9', j)
                                j = j + 1
                                
                        k = nc - 1
                        while k >= 0:
                                a=int(N[k])-1
                                #borrow from zero
                                if a<0:
                                        N = char(N, '9', k)
                                        k = k - 1
                                else:
                                        N = char(N, str(a), k)
                                        break
#                print N                     
        while N[0] == '0':
                N=N[1:]
                
        print 'Case #' + str(tc+1) + ': ' + N
