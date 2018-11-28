import sys
import time

start_time = time.time()

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stdout = sys.__stdout__


def check_if_ascending(num_arr):
    for i in range(len(num_arr) - 1):
        if num_arr[i] > num_arr[i + 1]:
            return i
    return -1


def main():

    for testcases in range(int(input())):
        ans = ''

        num = str(input())
        if len(num) == 1:
            ans = num
        else:
            number_arr = []
            for i in num:
                number_arr.append(int(i))
            while check_if_ascending(number_arr) != -1:
                pos = check_if_ascending(number_arr)
                number_arr[pos] -= 1
                for i in range(pos + 1, len(number_arr)):
                    number_arr[i] = 9

            for i in number_arr:
                ans += str(i)
            ans = str(int(ans))
        sys.stdout = open("output.txt", "a")
        print("Case #" + str(testcases + 1) + ": " + ans)
        sys.stdout = sys.__stdout__
        print("Case #" + str(testcases + 1) + ": Done")

if __name__ == '__main__':
    main()


sys.stdout = sys.__stdout__
print("Execution time : ", time.time() - start_time)
