import sys

if __name__ == "__main__":          
    f = open ("C-small-attempt1.in")
    output = open ("output", "w")

    lines = f.readlines()

    lines = [s.strip() for s in lines]

    my_number = int(lines.pop(0))

    for i in range(my_number):
        my_list = lines[i].split()
        my_number_1 = int(my_list[0])
        my_number_2 = int(my_list[1])

        count = 0

        for j in range(my_number_1, my_number_2):
            my_string = str(j)

            for k in range(1, len(my_string)):
                my_number_3 = int(my_string[k:] + my_string[0:k])

                if my_number_3 > j and my_number_3 <= my_number_2:
                    count += 1
        
        my_string_3 = "Case #" + str(i+1) + ": " + str(count) + "\n"
        print str(my_number_1) + "," + str(my_number_2) + "::" + my_string_3
        output.write(my_string_3)
        
        
    
    
    
