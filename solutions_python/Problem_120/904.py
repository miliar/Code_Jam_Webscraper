f = open('G:/Study/Programming/Code Jam/2013/Round1A/A-small-attempt0.in', 'r')
#f = open('G:/Study/Programming/Code Jam/2013/Round1A/trial.txt', 'r')
g = open('G:/Study/Programming/Code Jam/2013/Round1A/output1_large.txt', 'w')
#g = open('G:/Study/Programming/Code Jam/2013/Round1A/output_trial.txt', 'w')
no_test_cases = int(f.readline())
for test_case in range(1,no_test_cases+1):
    Initial_Rad, Total_Paint = f.readline().split()
    Initial_Rad, Total_Paint = int(Initial_Rad), int(Total_Paint)
    R, T = Initial_Rad, Total_Paint
    Answer = ((2*R-1)+((2*R-1)**2 + 8*T)**0.5)/4
    Answer2 = ((2*R-1)-((2*R-1)**2 + 8*T)**0.5)/4
    real_ans = Answer2
    if abs(int(Answer)) < abs(int(Answer2)):
        real_ans = Answer
    what_to_print = 'Case #'+str(test_case)+': '
    what_to_print += str(abs(int(real_ans))) + chr(10)
    g.write(what_to_print)