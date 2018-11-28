with open('A-large.in','r') as input:
    
    def isHappy(pancakes):
        """Check if a the range of pancakes is happy
            returns: Boolean
        """
        pancakesAreHappy = True
        
        for pancake in pancakes:
            if pancake == "-":
                pancakesAreHappy = False
                break
        return pancakesAreHappy

    file = input.read().split("\n")

    #Number of cases T
    T = int(file[0])

    #Storing results as a list for easier output
    results_list = list()

    current_line = 1

    for case in range(1,T+1):

        line = file[current_line].split(" ")

        pancake_row = list(line[0])
        flipper = int(line[1])
        first_pancake_index = 0
        last_pancake_index = first_pancake_index + flipper
        num_flips = 0

        #if len(pancake_row) == flipper:
        #    if not isHappy(pancake_row):
        #        num_flips = "IMPOSSIBLE"
        #else:

        while last_pancake_index <= len(pancake_row):
            #current_range = pancake_row[first_pancake_index:last_pancake_index+1]

            if pancake_row[first_pancake_index] == "-":
                #flipped_range = flip(current_range)
                for index in range(first_pancake_index,last_pancake_index):
                    if pancake_row[index] == "+":
                        pancake_row[index] = "-"
                    else:
                        pancake_row[index] = "+"
                    
                num_flips+=1

               
            first_pancake_index +=1
            last_pancake_index +=1

        #Last pancake range
        #first_pancake_index +=1
        #last_pancake_index +=1

        if not isHappy(pancake_row[first_pancake_index:last_pancake_index]):
            num_flips = "IMPOSSIBLE"


        results_list.append((str(case),str(num_flips)))

        current_line+=1

with open('A-large.out','w') as output:
    for case in results_list:
        output.write("Case #" + case[0] + ": " + case[1] + "\n")