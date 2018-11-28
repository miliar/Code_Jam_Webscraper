#!/usr/bin/env python
# google code jam 2015 -- standing ovation solution
#
# this will just print to stdout; should redirect into file for upload


def main():
    """Main function"""
    import sys
    with open(sys.argv[1]) as input_file:
        cases = input_file.readline()
        for x in range(int(cases)):
            max_shyness, shyness_data = input_file.readline().replace("\n", "").split(" ")
            print(
                "Case #{}: {}".format(
                    x+1,
                    calculate_shyness(shyness_data, max_shyness)))


def calculate_shyness(shyness_data, max_shyness):
    """Calculates the number of friends we need to invite based on the
    max_shyness of the crowd and the shyness_data that we receive.
    Unsure if we even really need max_shyness here, but I'm assuming we'll
    have cases where the length of shyness_data is less than max_shyness .. ?
    Seems like we wouldn't need it either way to be honest"""
    total = 0
    invites = 0
    for number, data in enumerate(shyness_data):
        if number > total:
            invites += number - total
            total += number - total
        total += int(data)
    return invites


if __name__ == '__main__':
    main()
