import sys

def process(input, result_file):
    t = int(input[0])
    last = 1
    for i in range(1, t + 1):
        d, n = input[last].split(" ")
        d, n = int(d), int(n)
        horses = input[last+1:last+1+n]
        horses = [([int(number) for number in row.split(" ")]) for row in horses]
        last += n+1

        #print(horses)
        result = ""

        slowest_time = 0
        for horse in horses:
            distance = d-horse[0]
            arrival = distance/horse[1]
            slowest_time = max(slowest_time, arrival)

        result = d/slowest_time

        ## do work here

        result_string = "Case #{}: {}\n".format(i, result)
        print(result_string)
        result_file.write(result_string)

if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "testinput_A"

    result_file_name = file_name + "_result"
    with open(result_file_name, 'w') as result_file:
        with open(file_name) as input_file:
            content = input_file.readlines()
        process(content, result_file)