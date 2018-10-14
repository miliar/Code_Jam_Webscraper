import sys, math
import fileinput
input_file=sys.argv[1]

line_count=0

fo = open("result.txt", "wb")

for line in fileinput.input(input_file):
    if line_count > 0:
        word_count = 0
        select = 0 
        fo.write( "Case #" + str(line_count) + ": ")
        rline=line.rstrip('\n\r')
        thisline = rline.split(" ");
        for word in thisline:
            word_count = word_count +1
            if word_count == 1:
                number_of_googlers = int(word)
            elif word_count == 2:
                surprising_case = int(word)
            elif word_count == 3:
                max_num = int(word)
            else:
                i = int(word)

                first_tab = 0
                second_tab = 0

                if i == 0:
                    print i
                    if max_num == 0:
                        first_tab=1

                else:

                    x=i/3.0
                    print x
                    if i % 3 == 0:
                        if x >= max_num:
                            first_tab=1
                            second_tab=0

                    x=(i-1)/3.0
                    print x
                    if (i-1) % 3 == 0:
                        if first_tab == 0:
                            if x >= max_num or x+1 >= max_num :
                                first_tab=1
                                second_tab=0

                    x=(i-2)/3.0


                    print x

                    if (i-2) % 3 == 0:
                        if first_tab == 0:
                            if x >= max_num or x+1 >= max_num:
                                first_tab=1
                                second_tab=0
                            elif x+2 == max_num:
                                if first_tab == 0:
                                    if surprising_case > 0:
                                        print "used surprising"
                                        surprising_case=surprising_case-1
                                        second_tab=1

                    x=(i-3)/3.0

                    print x

                    if first_tab == 0:
                        if (i-3) % 3 == 0:
                            if x >= max_num or x+1 >= max_num or x+2 >= max_num :
                                if surprising_case > 0:
                                    print "used surprising"
                                    surprising_case=surprising_case-1
                                    second_tab=1

                    x=(i-4)/3.0

                    print x

                    if first_tab == 0:
                        if (i-4) % 3 == 0:
                            if x >= max_num or x+2 >= max_num:
                                if surprising_case > 0:
                                    print "used surprising"
                                    surprising_case=surprising_case-1
                                    second_tab=1

                if first_tab == 1:
                    print "here"
                    select = select +1
                elif second_tab == 1:
                    print "here"
                    select = select +1

                print "--"
        print "----------------------------------------------"
        print select
        fo.write(str(select))
        fo.write("\n")

    line_count = line_count+1
fo.close()
