'''
Created on May 6, 2011

@author: iyen
'''

import heapq

def main():
    file = open('A-large.in')
    output = open('A-large.out', 'w')
    
    T = int(file.readline().strip())
    
    for t in range(1,T+1):
        case = file.readline().strip("\n").split(" ")
        num_buttons = int(case.pop(0))
        
        O_seq = []
        B_seq = []
        i = 0
        for b in range(1,num_buttons+1):
            if case[i] == "O":
                heapq.heappush(O_seq, (b, int(case[i+1])))
            elif case[i] == "B":
                heapq.heappush(B_seq, (b, int(case[i+1])))
            i += 2
                    
        O_curPos = 1
        B_curPos = 1
        
        try:
            (O_priority, O_goalPos) = heapq.heappop(O_seq)
        except IndexError:
            O_priority = 200
                    
        try:
            (B_priority, B_goalPos) = heapq.heappop(B_seq)
        except IndexError:
            B_priority = 200
        
        time = 0
        
        while True:
            #print("O:" + str(O_curPos) + "  B:" + str(B_curPos))
            O_diff = abs(O_goalPos - O_curPos)
            B_diff = abs(B_goalPos - B_curPos)
            
            if O_priority < B_priority:
                # move O
                O_curPos = O_goalPos
                # move B
                if O_diff >= B_diff-1:
                    B_curPos = B_goalPos
                else:
                    if B_goalPos > B_curPos:
                        B_curPos += O_diff + 1
                    else:
                        B_curPos -= O_diff + 1
                # increment time
                time += O_diff + 1
                # O pushes button
                #print("O :", O_curPos, "-->", time)
                
                # get next goal for O
                try:
                    (O_priority, O_goalPos) = heapq.heappop(O_seq)
                except IndexError:
                    O_priority = 200
            else:
                # move B
                B_curPos = B_goalPos
                # move O
                if B_diff >= O_diff-1:
                    O_curPos = O_goalPos
                else:
                    if O_goalPos > O_curPos:
                        O_curPos += B_diff + 1
                    else:
                        O_curPos -= B_diff + 1
                # increment time
                time += B_diff + 1
                # B pushes button
                #print("B :", B_curPos, "-->", time)
                
                # get next goal for B
                try:
                    (B_priority, B_goalPos) = heapq.heappop(B_seq)
                except IndexError:
                    B_priority = 200
            
            if O_priority == 200 and B_priority == 200:
                break
        
        #print("Case #"+str(t) + ": " + str(time) + "\n")
        output.write("Case #"+str(t) + ": " + str(time) + "\n")
                             
    
if __name__ == '__main__':
    main()