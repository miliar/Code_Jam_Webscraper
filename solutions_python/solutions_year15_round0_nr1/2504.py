__author__ = 'valentinarho'

if __name__ == '__main__':

    nomefile = "A-large"

    # open file input
    input = open(nomefile+'.in','r')
    out = open(nomefile+'.out','w')

    # number of test case
    T = int(input.readline())

    for i in range(1, T+1): #da 1 a t
        case = input.readline()
        case_split = case.split(' ')
        max_shy = int(case_split[0])
        shy_numbers = case_split[1]
        shy_array = list(shy_numbers)
        to_invite = 0

        num_standing = int(shy_array[0])
        for min in range(1, max_shy+1):
            while num_standing + to_invite < min:
                to_invite = to_invite+1

            num_standing = num_standing + int(shy_array[min])

        out.write("Case #"+str(i)+": "+str(to_invite)+"\n")

    out.close()
    input.close()