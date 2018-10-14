'''
Created on Apr 15, 2017

@author: qiuyx
'''

def solve(R, C, cake):
    startrow = 0
    for i in xrange(R):
        if len(set(cake[i])) != 1 or (len(set(cake[i])) == 1 and '?' not in set(cake[i])):
            startrow = i
            break
        
    for i in xrange(startrow, R):
        direction = 'r'
        if (len(set(cake[i])) == 1 and '?' in set(cake[i])):
            direction = 'c'

        if direction == 'r':
            for j in xrange(C):
                last = 0
                if cake[i][j] != '?':
                    for k in xrange(j):
                        cake[i][k] = cake[i][j] if cake[i][k] == '?' else cake[i][k]
                    last = j
    
                if j == C - 1 and cake[i][j] == '?':
                    for k in xrange(last, C):
                        cake[i][k] = cake[i][last]
        elif direction == 'c':
            for j in xrange(C):
                cake[i][j] = cake[i-1][j]
    
    for i in xrange(startrow):
        for j in xrange(C):
            cake[i][j] = cake[startrow][j]
    
    
if __name__ == '__main__':
    # read file:
    
    file_in = open('H:/ZJam/A-small-attempt1.in')
    file_out = open('H:/ZJam/A-small-output.out', 'w')
    T = int(file_in.readline()[:-1])
    for i in xrange(T):
        line = (file_in.readline())[:-1].split(' ')
        R, C = line
        cake = []
        for j in xrange(int(R)):
            cake.append(list((file_in.readline())[:-1]))

        solve(int(R), int(C), cake)
        
        
        result = 'Case #' + str(i+1) + ':\n'
        for j in xrange(int(R)):
            result += ''.join(cake[j]) + '\n' if j<int(R)-1 else ''.join(cake[j])
            
        file_out.write(str(result)+'\n')
        print result
 

    file_out.close()
    file_in.close()