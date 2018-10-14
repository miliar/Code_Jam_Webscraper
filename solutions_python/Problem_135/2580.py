rf = open('A-small-attempt2.in', 'r')

line_counter = 0
T = None

answer_1 = None
answer_2 = None
answer_pair = []

arrangement_1 = []
arrangement_2 = []

read_next_4_in_a1_counter = 0
read_next_4_in_a2_counter = 0

case_num = 0

fw = open("p1_magic_trick_a2.txt", "w")

for l in rf:
    tokens = l.split()
    if len(tokens) > 0:
        line_counter += 1
        if line_counter == 0:
            T = int(tokens[0])
        elif (line_counter - 2) % 5 == 0:
            if (line_counter - 2) % 2 == 0:
                answer_pair = []
                arrangement_1 = []
                answer_1 = int(tokens[0])
                answer_pair.append(int(answer_1))
                read_next_4_in_a1 = []
                read_next_4_in_a1_counter = 4
            else:
                arrangement_2 = []
                answer_2 = int(tokens[0])
                answer_pair.append(int(answer_2))
                read_next_4_in_a2_counter = 4
        else:
            if read_next_4_in_a1_counter > 0:
                arrangement_1.append(tokens)
                read_next_4_in_a1_counter -= 1
            elif read_next_4_in_a2_counter > 0:
                arrangement_2.append(tokens)
                read_next_4_in_a2_counter -= 1

        if read_next_4_in_a1_counter==0 and read_next_4_in_a2_counter==0 and len(answer_pair)==2:
            case_num += 1

            i = set(arrangement_1[answer_pair[0]-1]).intersection(arrangement_2[answer_pair[1]-1])
            if len(i)==1:
                fw.write("Case #%d: %d\n" % (case_num, int(list(i)[0])))
            elif len(i)>1:
                fw.write("Case #%d: Bad magician!\n" % (case_num))
            else:
                fw.write("Case #%d: Volunteer cheated!\n" % (case_num))

