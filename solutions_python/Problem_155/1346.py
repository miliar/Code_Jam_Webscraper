import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, 
                    help='Input file')
args = parser.parse_args()

with open(args.input) as f:
    f.readline()  # Discard # of cases
    for case, line in enumerate(f, start=1):
        croud_string = line.strip().split()[-1]
        croud = [int(x) for x in croud_string]
        missing = 0  # The solution
        for shyness, ammount in enumerate(croud):
            if not ammount:  # Don't bother if there are no shys
                continue
            while sum(croud[:shyness]) + missing < shyness:
                missing += 1
        print('Case #{}: {}'.format(case, missing))
