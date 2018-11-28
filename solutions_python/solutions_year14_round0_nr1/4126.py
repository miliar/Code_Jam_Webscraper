
import sys



def main():
    infile = open(sys.argv[1], 'r')   
    outfile = open("out.file", 'w')
    cases = int(infile.readline())

    for case in range(0, cases):

        first_tip = int(infile.readline())
        guess = []
        final = []
        
        for row_number in range (1, 5):
            line = infile.readline().strip()  
            if row_number == first_tip:
                guess = line.split(' ')

        second_tip = int(infile.readline())
        #print guess
        for row_number in range (1, 5):
            line = infile.readline().strip().split(' ')
            if row_number == second_tip:
                for card in guess:
                    if card in line:
                        
                        final.append(card)
        
        if len(final) == 0:
            print "Case #"+str(case+1)+": Volunteer cheated!"
        
        elif len(final) > 1:
            print "Case #"+str(case+1)+": Bad magician!"

        else:
            print "Case #"+str(case+1)+": "+str(final[0])
       
    

main()
