def main():
    filename = "A-large.in.txt"

    input_file = open(filename, "r")
    output_file = open("snapper.out.txt", "w")

    num_of_testcases = int(input_file.readline())

    line_counter = 0
    while True:
        line = input_file.readline()
        line_counter += 1
        if line == "":
            break
        else:
            n, k = [int(x) for x in line.split()]
            
            bit_mask = 2**n - 1
            k_masked = bit_mask & k
            
            if k_masked == bit_mask:
                output_file.write("Case #" + str(line_counter) + ": ON\n")
            else:
                output_file.write("Case #" + str(line_counter) + ": OFF\n")

    input_file.close();

if __name__ == '__main__':
    main()