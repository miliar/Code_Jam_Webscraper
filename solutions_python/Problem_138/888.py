#regular war, check Naomi's highest, see if Ken can go above, if no, 1 point for Naomi;
#next Naomi block, if Ken can go above, pop it out
#need to sort it first

#deceitful war: check Naomi's highest, see if Ken can go above, if no, 1 point;
#if yes, pop out Ken's piece, and pop out Naomi's lowest piece
#


def solve_case_regular(naomi_list, ken_list):
    #solve regular war
    naomi_list_copy = naomi_list[:]
    ken_list_copy = ken_list[:]
    i= number_pieces
    points = 0
    while i > 0:
        if naomi_list_copy[0]>ken_list_copy[0]:
            points +=1
            naomi_list_copy.pop(0)
            ken_list_copy.pop(-1)
            i -=1
        else:
            naomi_list_copy.pop(0)
            ken_list_copy.pop(0)
            i -=1
    return points

def solve_case_deceit(naomi_list, ken_list):
    #solve deceitful war
    naomi_list_copy = naomi_list[:]
    ken_list_copy = ken_list[:]
    i= number_pieces
    points = 0
    while i > 0:
        if naomi_list_copy[0]>ken_list_copy[0]:
            points +=1
            naomi_list_copy.pop(0)
            ken_list_copy.pop(0)
            i -=1
        else:
            naomi_list_copy.pop(-1)
            ken_list_copy.pop(0)
            i -=1
    return points
    

f = open("D-large.in")
fout = open("output.txt", "w")
T = int(f.readline().rstrip())

for ii in range(T):
    number_pieces = int(f.readline().rstrip())
    naomi_list = [float(x) for x in f.readline().rstrip().split(" ")]
    ken_list = [float(x) for x in f.readline().rstrip().split(" ")]

    answer_regular = solve_case_regular(sorted(naomi_list, reverse=True),sorted(ken_list, reverse=True))
    answer_deceit = solve_case_deceit(sorted(naomi_list, reverse=True),sorted(ken_list, reverse=True))

    print "Case #"+str(ii+1)+": "+str(answer_deceit)+" "+str(answer_regular)
    fout.write("Case #"+str(ii+1)+": "+str(answer_deceit)+" "+str(answer_regular)+"\n")

fout.close()
