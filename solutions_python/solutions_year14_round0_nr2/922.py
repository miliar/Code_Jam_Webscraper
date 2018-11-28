testcase_count = int(input())
for testcase_index in range(testcase_count):
    testcase_data = input().split()
    factory_cost = float(testcase_data[0])
    factory_production = float(testcase_data[1])
    target = float(testcase_data[2])

    production = 2
    total_time = 0

    while True:
        time_waiting = target / production
        time_buying = factory_cost / production + target / (production + factory_production)

        if time_waiting < time_buying:
            total_time += time_waiting
            break
        total_time += factory_cost / production
        production += factory_production

    print("Case #%d: %f" % (testcase_index + 1, total_time))
