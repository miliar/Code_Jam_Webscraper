def main():
    num_test_cases = int(raw_input())
    for test_case in range(num_test_cases):
        C, F, X = map(float, raw_input().split())

        elapsed_time = 0.0
        num_farms = 0
        while True:
            to_bake = X / (2 + (num_farms * F))
            to_farm_bake = (C / (2 + (num_farms * F))) + (X / (2 + ((num_farms+1) * F)))
            if to_bake <= to_farm_bake:
                elapsed_time += X/(2 + (num_farms * F))
                break
            else:
                elapsed_time += C/(2 + (num_farms * F))
                num_farms += 1

        print 'Case #%d: %f' % (test_case+1, round(elapsed_time, 7))


if __name__ == '__main__':
    main()
