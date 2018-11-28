import sys

def last_tidy_int(num):
    return int(last_tidy_str(str(num)))

def last_tidy_str(num_str):
    if len(num_str) < 2:
        return num_str
    temp = last_tidy_str(num_str[1:])
    if num_str[0] <= temp[0]:
        return num_str[0] + temp
    else:
        return str(int(num_str[0]) - 1) + '9'*(len(temp))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    target = open('b-small-output.txt', 'w')
    for i in range(n):
        target.write("case #{}: {}\n".format(i+1, last_tidy_int(int(sys.stdin.readline()))))
