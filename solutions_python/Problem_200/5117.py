f = open("input.txt", "r")

num_test_cases = int(f.readline())
print num_test_cases

list1 = []


for test_cases in range(0, num_test_cases):
    list1.append(int(f.readline()))
print list1


def last_tidy_num(n):
    if n < 10:
        return n

    else:
        for number in range(n, 0, -1):
            segment = [int(digits) for digits in str(number)]
            if sorted(segment) == segment:
                return number


result = []
fout = open("output.txt", "w")
for i in range(0, num_test_cases):

    fout.write("Case #" + str(i+1) + ": " + str(last_tidy_num(list1[i])) + '\n')

# print(last_tidy_num(1111111110))
