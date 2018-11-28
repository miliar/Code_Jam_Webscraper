def main(input_address):
    input_file = open(input_address, "r")
    solve(input_file, open("D:\\output.txt","w"))

def solve(input_file, output_file):
    cases_number = int(input_file.readline())
    for k in range(cases_number):
        first_answer = int(input_file.readline())
        for i in range(first_answer-1):
            input_file.readline()
        row1 = input_file.readline().split()

        for i in range(4 - first_answer):
            input_file.readline()
        
        second_answer = int(input_file.readline())
        for i in range(second_answer-1):
            input_file.readline()
        row2 = input_file.readline().split()

        for i in range(4 - second_answer):
            input_file.readline()

        for i in range(4):
            row1[i] = int(row1[i])
            row2[i] = int(row2[i])

        rep = repetitions(row1,row2)

        if rep[0] == 1:
            answer = rep[1]
        elif rep[0] == 0:
            answer = "Volunteer cheated!"
        else:
            answer = "Bad magician!"
            
        output_file.write("Case #" +
                          str(k+1) + ": " + answer + "\n")
    input_file.close()
    output_file.close()



        
        
def repetitions(list1, list2):

    #takes two lists, returns the number of repeated numbers as a singleton.
        #If it is 1, return a list where the first value is 1, the second
        #is a string of the number that was repeated.

    num = 0
    for i in list1:
        for j in list2:
            if i==j:
                repeated = j
                num += 1
                break
    if num != 1:
        return [num]
    else:
        return [num, str(repeated)]
          


main("D:\\A-small-attempt0.in")
