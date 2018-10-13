import sys
import collections

def can_trim_line(lawn, index, height):
    line = lawn[index]
    for h in line:
        if h > height: return False
    return True

def trim_line(lawn, index, height):
    lawn[index][:] = [height if i > height else i for i in lawn[index]]

def can_trim_row(lawn, index, height):
    for line in lawn:
        if line[index] > height: return False
    return True

def trim_row(lawn, index, height):
    for line in lawn:
        if line[index] > height: line[index] = height


def trim_to_height (current_lawn, target_lawn, points, height):
    trimmed_lines = []
    trimmed_rows = []
    for point_to_trim in points:
        line_index = point_to_trim[0]
        row_index = point_to_trim[1]
        #print('point', point_to_trim, 'height', height)
        if line_index in trimmed_lines or row_index in trimmed_rows:
            #print('skip')
            continue
        if can_trim_line(target_lawn, line_index, height):
            trim_line(current_lawn, line_index, height)
            trimmed_lines.append(line_index)
        elif can_trim_row(target_lawn, row_index, height):
            trim_row(current_lawn, row_index, height)
            trimmed_rows.append(row_index)
        else: return False
        #print('trimmed', current_lawn)
    return True

def mow_lawn (file):
    nb_lines, nb_rows = (int(x) for x in file.readline().split())
    case_by_height = collections.defaultdict(list)
    target_lawn = []
    for line in range(nb_lines):
        line_heights = [int(x) for x in file.readline().split()]
        target_lawn.append(line_heights)
        for row, height in enumerate(line_heights):
            case_by_height[height].append((line, row))

    current_lawn = [[100 for j in range(nb_rows)] for i in range(nb_lines)]

    target_heights = sorted(case_by_height.keys())
    target_heights.reverse()

    for height in target_heights:
        could_trim = trim_to_height(current_lawn, target_lawn, case_by_height[height], height)
        if not could_trim: return False

    return True

def main():
    file_name = sys.argv[1]
    file = open(file_name, 'rU')
    output_file = open(sys.argv[2], 'w')
    num_test_cases = int(file.readline())
    for test_case in range(num_test_cases):
        is_lawn_mown = mow_lawn(file)
        output_file.write('Case #' + str(test_case+1) + ': ' + ('YES' if is_lawn_mown else 'NO') + '\n')
    file.close()

if __name__ == '__main__':
    main()
