__author__ = 'chamathsilva'


def finder(data_string):
    no_of_invite_friends = 0
    shyness_level = 0

    persons = list(data_string)

    for i in range (len(persons)):
        if i <= shyness_level:
            shyness_level += int(persons[i])

        else:
            no_of_invite_friends += i - shyness_level
            shyness_level = i
            shyness_level += int(persons[i])


    return no_of_invite_friends



def get_input():
    out_string = ""
    input_file =  open('A-large.in', 'r')
    N = int(input_file.readline())

    for i in range (N):
        temp = input_file.readline().split()
        out_string += str("Case #") + str(i+1) +str(": ")  + str(finder(temp[1])) + str("\n")
    output_file  = open('output_file.out','w')
    output_file.write(out_string)




if __name__ == "__main__":
    get_input()
