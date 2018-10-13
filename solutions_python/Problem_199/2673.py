def flip(s_list, start, end):
    for idx in range(start, end):
        if s_list[idx] == '-':
            s_list[idx] = '+'
        else:
            s_list[idx] = '-'

def minunFlips(s, k):
    s_list = list(s)
    s_len = len(s_list)
    flips_num = 0
    for idx, p in enumerate(s_list):
        if p == '-':
            if s_len >= idx + k:
                flip(s_list, idx, idx + k)
                flips_num = flips_num + 1
            else:
                return "IMPOSSIBLE"
    return flips_num


def main(input_file, output_file):

    with open(input_file) as input:
        number_list = input.readlines()

    print "Got {0} input numbers".format(number_list[0])


    number_list.pop(0)

    with open (output_file, 'w') as output:
        for idx, val  in enumerate(number_list):
            val = val.strip()
            s, k = val.split(" ")
            print "*" * 20
            print "s {}, k {}".format(s, k)
            res = minunFlips(s, int(k))
            print "minumum flips: ", res
            output.write("Case #{0}: {1}\n".format(idx + 1, res))
    return


if __name__ == "__main__":
    input_file = "A-large.in"
    output_file = "A-large.out"
    main(input_file, output_file)