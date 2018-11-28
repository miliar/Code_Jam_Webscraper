__author__ = 'Haewon'

from math import log2, pow

# def bin_reverse(x):
#     rev = 0
#     while x:
#         rev <<= 1
#         rev += x & 1
#         x >>= 1
#     return rev


def bathroomStall(n, k):
    l = int(log2(k+1))
    num_pieces = int(pow(2, l))
    rem_k = k - num_pieces + 1

    if rem_k == 0:
        num_pieces /= 2
        rem_stalls = n - num_pieces + 1
        size_piece = int(rem_stalls/num_pieces)
        return [int(size_piece/2), int((size_piece-1)/2)]

    rem_stalls = n - num_pieces + 1
    size_piece = int(rem_stalls/num_pieces)
    num_ex_size_piece =  rem_stalls % num_pieces

    # ex_size_loc = []
    # bin_number = num_pieces-1
    # for i in range(num_ex_size_piece):
    #     rev_bin_number = bin_reverse(bin_number)
    #     ex_size_loc.append(rev_bin_number)
    #     bin_number -= 1

    if rem_k <= num_ex_size_piece:
        size_piece += 1

    return [int(size_piece/2), int((size_piece-1)/2)]


def main():
    #input read
    input_file = open("input_c_small2.in", 'rt')
    num_cases = int(input_file.readline())

    #output write
    output_file = open("output_c_small2.txt", 'w')

    for i in range(num_cases):
        line = input_file.readline()
        p=[]
        line = line.split()
        n = int(line[0])
        k = int(line[1])
        result = bathroomStall(n, k)
        output = "Case #%d: %d %d\n" %(i+1, result[0], result[1])
        output_file.write(output)
        print(i+1)
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()