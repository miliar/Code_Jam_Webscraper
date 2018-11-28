# Google Code Jam 2014, Problem A - Magic Trick
# Steven Stevanus stevenstevanus@gmail.com

def magictrick():
    try:
        f_input = open('A-small-attempt0.in','r')
        f_output = open('A-small-attempt0.ou','w')
        case = int(f_input.readline().strip('\n'))
        for i in range(1,case+1):
            row1 = int(f_input.readline().strip('\n'))
            Card_row1 = set()
            Card_row2 = set()
            for j in range(1,5):
                if j==row1:
                    Card_row1 = set([k for k in f_input.readline().strip('\n').split(' ')])
                else:
                    f_input.readline()
                    
            row2 = int(f_input.readline().strip('\n'))
            for j in range(1,5):
                if j == row2:
                    Card_row2 = set([k for k in f_input.readline().strip('\n').split(' ')])
                else:
                    f_input.readline()
            result = Card_row1&Card_row2
            if len(result) == 1:
                r = [k for k in result]
                f_output.write("Case #"+str(i)+": "+r[0]+'\n')
            elif len(result) == 0:
                #print ("Volunteer cheated!")
                f_output.write("Case #"+str(i)+": Volunteer cheated!"+'\n')
            else:
                #print ("Bad magician!")
                f_output.write("Case #"+str(i)+": Bad magician!"+'\n')

    except:
        print ("Error Reading File")
    
    f_input.close()
    f_output.close()

if __name__ == '__main__':
    magictrick()
                    
    
