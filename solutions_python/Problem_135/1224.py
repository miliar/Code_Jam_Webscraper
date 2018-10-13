'''
Created on 12 Apr 2014

@author: Nigel.Fernandez
'''

def main():
    fread = open('A-small-attempt0.in', 'r')
    fwrite = open('A_magic_trick_output_nigel_fernandez.dat', 'w')
    
    c_num = int(fread.readline())
    
    for i in range(c_num):
        ans1 = int(fread.readline())
        board1 = []
        for _ in range(4):
            board1.append(fread.readline().split())
        ans2 = int(fread.readline())
        board2 = []
        for _ in range(4):
            board2.append(fread.readline().split())
        
        row1 = set(board1[ans1 - 1])
        row2 = set(board2[ans2 - 1])
        verdict = len(row1.intersection(row2))
        
        if (verdict == 0):
            fwrite.write('Case #' + str(i + 1) + ': Volunteer cheated!\n')
        elif (verdict == 1):
            fwrite.write('Case #' + str(i + 1) + ': ' + str(row1.intersection(row2).pop()) + '\n')
        else:
            fwrite.write('Case #' + str(i + 1) + ': Bad magician!\n')
    
    fread.close()
    fwrite.close()
    
if __name__ == '__main__':
    main()