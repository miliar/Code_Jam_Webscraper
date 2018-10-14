
from sets import Set

input_file = open('A-small-attempt0.in','r')
input_data = ''.join(input_file.readlines())
input_file.close()

lines = input_data.split('\n')
no_of_test_cases = int(lines[0])
f=open("out.txt",'w')
for i in range (no_of_test_cases):
    j=i*10+1
    first_sol = int(lines[j])
    first_sol_row = Set(lines[j+first_sol].split(' '))
    #print first_sol_row
    j=j+5
    second_sol = int(lines[j])
    second_sol_row = Set(lines[j+second_sol].split(' '))
    #print second_sol_row
    intersection = first_sol_row & second_sol_row
    #print intersection

    if len(intersection) == 1:
        f.write("Case #%d: %s\n"%(i+1,intersection.pop()))
        #print "Case #%d: %s"%(i+1,intersection.pop())
    elif len(intersection) == 0:
        f.write("Case #%d: Volunteer cheated!\n"%(i+1))
        #print "Case #%d: Volunteer cheated!"%(i+1)
    else:
        f.write("Case #%d: Bad magician!\n"%(i+1))
        #print "Case #%d: Bad magician!"%(i+1)
f.close()


