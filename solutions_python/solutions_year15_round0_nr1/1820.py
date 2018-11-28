f_in = 'A-large.in'
f_out = 'A-large.out'

f = open(f_in, 'r')
o = open(f_out, 'w')

T = int(f.readline())

def main():
    with f:
        data = f.readlines()

    total_standing = 0
    for case_num_minus1, line in enumerate(data):
        case = line.split()
        case[0] = int(case[0])      # Maximum shyness in audience
        case[1] = [int(i) for i in case[1]]     # Data: S_i of audience

        min_friend_needed = 0
        for Si, num_of_Si_audience in enumerate(case[1]):
            if (Si == 0) and (num_of_Si_audience > 0):
                """ Base case """
                total_standing = num_of_Si_audience
            elif (total_standing < Si):
                min_friend_needed += 1
                total_standing += (1+num_of_Si_audience)
            else:
                total_standing += num_of_Si_audience

        o.write("Case #{0}: {1}\n".format(str(case_num_minus1 + 1), str(min_friend_needed)))
        total_standing = 0  # Reset (loop logic bug?)

if __name__ == "__main__":
    main()
