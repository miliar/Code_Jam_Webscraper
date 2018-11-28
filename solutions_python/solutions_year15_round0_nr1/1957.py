def runner(max_shyness, audience):
    friends, total = 0, 0
    
    for i, members in enumerate(audience):
        total += members
        if total <= i:
            friends = friends + (total - i+1)
            total = total + (total - i+1)

    return friends


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File input for Google Code Jam")
    parser.add_argument('infile', help="input file location")

    parse_results = parser.parse_args()
    infile = parse_results.infile

    with open(infile, 'r') as fin:
        cases = int(fin.readline())

        for n in range(cases):
            max_shyness, audience = fin.readline().split()

            max_shyness = int(max_shyness)
            audience = [int(i) for i in audience]

            retval = runner(max_shyness, audience)
            print("Case #{}: {}".format(n+1, retval))
