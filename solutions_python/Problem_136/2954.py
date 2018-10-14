#-*-coding:utf-8-*-


from __future__ import division


def time_with_k_farm(C, F, X, k, start_rate, time_for_k_1_farms):
    """
    return (the time cost for buying k farms, the time after buying k farms)
    """
    time1 = time_for_k_1_farms + C / (start_rate + (k - 1) * F)

    time2 = X / (start_rate + k * F)

    return time1, time2




if __name__ == "__main__":
    data_file_path = "B-large.in"

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

    with open("test2_output_large.txt", "w") as output_file:
        for test_index in xrange(1, test_num + 1):
            test = dict[test_index]
            C = test["C"]  # cost for a new farm
            F = test["F"]  # extra cookies per second
            X = test["X"]  # goal

            start_rate = 2
            current_total_farm_num = 0
            time_for_last_iteration = X / start_rate # start with no farms
            time_for_k_1_farms = 0
            while True:
                current_total_farm_num += 1
                time1, time2 = time_with_k_farm(C, F, X, current_total_farm_num, start_rate, time_for_k_1_farms)


                if time1 + time2 > time_for_last_iteration:
                    break

                time_for_k_1_farms = time1
                time_for_last_iteration = time1 + time2

            output_file.write("Case #" + str(test_index) + ": " + str(time_for_last_iteration) + "\n")



