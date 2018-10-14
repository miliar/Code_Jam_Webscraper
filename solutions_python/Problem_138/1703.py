import sys
import copy

def deceitful_war(naomi_blocks, ken_blocks, blocks):
    naomi_score = 0
    for naomi_weight in naomi_blocks:
        found_smaller = False
        for i in range(len(ken_blocks)):
            ken_weight = ken_blocks[i]
            if naomi_weight > ken_weight:
                found_smaller = True
                found_id = i
                break

        if found_smaller:
            naomi_score += 1
            del ken_blocks[found_id]
        else:
            del ken_blocks[-1]

    return naomi_score

def war(naomi_blocks, ken_blocks, blocks):
    naomi_score = 0

    for naomi_weight in naomi_blocks:
        found_bigger = False

        for i in range(len(ken_blocks)):
            ken_weight = ken_blocks[i]
            if ken_weight > naomi_weight:
                found_bigger = True
                selected_id = i
                break

        if found_bigger:
            del ken_blocks[selected_id]
        else:
            naomi_score += 1
            del ken_blocks[0]

    return naomi_score

def writeline(f, line):
    print(line)
    f.write('%s\n' % line)

def main():
    if len(sys.argv) != 2:
        print('Usage: %s INPUT_FILENAME' % sys.argv[0])
        return 1

    input_file = sys.argv[1]
    f = file(input_file)

    output_file = input_file[:-3] + ".out"
    out = file(output_file, 'w')

    number_of_test_cases = int(f.readline())

    for case in range(1, number_of_test_cases + 1):
        line = f.readline()
        blocks = int(line)

        line = f.readline()
        naomi_blocks = [float(x) for x in line.split(' ')]
        naomi_blocks = sorted(naomi_blocks)
        #print('naomi_blocks: %s' % ' '.join((['%0.3f' % x for x in naomi_blocks])))

        line = f.readline()
        ken_blocks = [float(x) for x in line.split(' ')]
        ken_blocks = sorted(ken_blocks)
        #print('ken_blocks:   %s' % ' '.join((['%0.3f' % x for x in ken_blocks])))

        naomi_deceitful = deceitful_war(
            copy.copy(naomi_blocks),
            copy.copy(ken_blocks),
            copy.copy(blocks))

        naomi_war = war(
            copy.copy(naomi_blocks),
            copy.copy(ken_blocks),
            copy.copy(blocks))

        writeline(out, 'Case #%d: %d %d' % (case, naomi_deceitful, naomi_war))

    return 0

if __name__ == '__main__':
    sys.exit(main())

