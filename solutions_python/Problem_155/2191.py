__author__ = 'dlohani'

input_file = open("input/A-large.in", "r")
output_file = open("output/A-large.out", "w")
T = int(input_file.readline())
for i in range(T):
    inp = input_file.readline()
    inp = inp.split()
    max_shyness = int(inp[0])
    no_of_audience = inp[1]
    ans = 0
    digit_sum = int(no_of_audience[0])
    for j in range(1, len(no_of_audience)):
        int_no_of_audience = int(no_of_audience[j])
        if j > digit_sum:
            ans += j - digit_sum
            digit_sum += int_no_of_audience + (j - digit_sum)
        else:
            digit_sum += int_no_of_audience
        if digit_sum >= max_shyness:
            break
    output_file.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")
output_file.close()
input_file.close()
