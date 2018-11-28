# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:05:27 2014

@author: vajepeya
"""

# A - Magic Trick


def check_answer(ans1, gr1, ans2, gr2, cnt):

    result_string = ''
    
    row1 = set(gr1[ans1-1])
    row2 = set(gr2[ans2-1])
    result = row1.intersection(row2)

    if len(result) == 1:
        for x in result:
            a = x
        result_string = str(a)
    if len(result) == 0:
        result_string = 'Volunteer cheated!'
    if len(result) > 1:
        result_string = 'Bad magician!'
        
    out_string = 'Case #' + str(cnt) + ': ' + result_string + '\n'
    
    return out_string
    
    

def main():
    inpfile = 'A-small-attempt0.in'
    outfile = 'A-small-attempt0.out'
    
    finp = open(inpfile, 'r')
    fout = open(outfile, 'w')
    
    T = finp.readline()
    lines = finp.readlines()
    
    out_string = ''
    
    grid1 = []
    grid2 = []
    count = 0
    testcase_count = 1
    
    for line in lines:
    
        if count % 10 == 0:
            answer1 = int(line)
    
        elif count % 10 in (1,2,3,4):
            grid1.append([int(cell) for cell in line.split()])

        elif count % 10 == 5:
            answer2 = int(line)
            
        elif count % 10 in (6,7,8,9):
            grid2.append([int(cell) for cell in line.split()])

        # Increment counter
        count += 1
       
        # Reinitialize the grids after 1 attempt
        if count >= 10:
            out_string = check_answer(answer1, grid1, answer2, grid2, testcase_count)
            print out_string
            fout.write(out_string)
            grid1 = []
            grid2 = []
            count = 0
            testcase_count += 1    
    
    # Sanity check
#    if testcase_count == int(T)+1:
#        print 'OK...\n'
#    else:
#        #print T, linecount
#        print 'ERROR +++++++\n'
    
    finp.close()
    fout.close()
    

if __name__=="__main__":
    main()