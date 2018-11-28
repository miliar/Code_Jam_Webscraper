

def worker(num):
    for i in reversed(range(num + 1)):
        num_list = list(str(i))
        num_list = list(map(int, num_list))

        if sorted(num_list) == num_list:
            return int(''.join(map(str, num_list)))


if __name__ == '__main__':

    # test = int(input())
    #
    # t = 1
    # while t <= test:
    #     in_value = input()
    #     print("Case #{}: {}".format(t, worker(in_value)))
    #     t += 1

    with open('/Users/lobanod/PycharmProjects/GoogleJam/Qualification/output.txt', 'w') as output:

        with open('/Users/lobanod/PycharmProjects/GoogleJam/Qualification/test.txt', 'r') as file:
            test = int(file.readline())
            t = 1
            for f in file.readlines():
                print("Case #{}: {}".format(t, worker(int(f))))
                t += 1
