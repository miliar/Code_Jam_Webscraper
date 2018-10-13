#-*-coding:utf-8-*-


from __future__ import division


def time_with_k_farm(C, F, X, k, start_rate):
    """
    return the time cost for ending game with k farms
    """
    time = 0
    for i in xrange(0, k):
        time += C / (start_rate + i * F)

    time += X / (start_rate + k * F)

    return time




if __name__ == "__main__":
    data_file_path = "B-small-attempt0.in"

    test_num = 0
    with open(data_file_path) as file:
        lines = file.readlines()
        first_line = lines[0].strip()
        test_num = int(first_line)

        dict = {}
        test_index = 1
        for line in lines[1 : test_num + 1]:
            line = line.strip()
            paras = line.split(" ")
            test = {}
            test["C"] = float(paras[0])
            test["F"] = float(paras[1])
            test["X"] = float(paras[2])

            dict[test_index] = test
            test_index += 1

    # print dict

    with open("test2_output.txt", "w") as output_file:
        for test_index in xrange(1, test_num + 1):
            test = dict[test_index]
            C = test["C"]  # cost for a new farm
            F = test["F"]  # extra cookies per second
            X = test["X"]  # goal

            start_rate = 2
            current_total_farm_num = 0
            time_for_last_iteration = None

            while True:
                time = time_with_k_farm(C, F, X, current_total_farm_num, start_rate)

                if time_for_last_iteration and time > time_for_last_iteration:
                    break

                current_total_farm_num += 1
                time_for_last_iteration = time

            output_file.write("Case #" + str(test_index) + ": " + str(time_for_last_iteration) + "\n")



