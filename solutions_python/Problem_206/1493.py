def format_output(output, case):
    return "Case #{}: {}\n".format(case, output)


def main():
    import math
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f, open(args.input_file.replace("in", "out"), "w") as out:
        test_nums = int(f.readline().strip())
        for index in range(test_nums):
            distance, num_ponies = (int(num) for num in f.readline().strip().split())
            max_t = -1
            for _ in range(num_ponies):
                distance_traveled, speed = (int(num) for num in f.readline().strip().split())
                pony_finish_time = (distance - distance_traveled)/speed
                if pony_finish_time > max_t:
                    max_t = pony_finish_time
            my_pony_speed = distance / max_t

            out.write(format_output(my_pony_speed, index + 1))


if __name__ == "__main__":
    main()
