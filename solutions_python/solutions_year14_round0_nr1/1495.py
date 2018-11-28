__author__ = 'anoop'

import numpy as np

INPUT_FILE = 'A-small-attempt0.in'
OUTPUT_FILE = 'A-small-attempt0.out'

GRID_SIZE = 4


def read_matrix_arrangement(file_ptr, GRID_SIZE):
    arrangement = np.zeros((GRID_SIZE, GRID_SIZE))
    for i in range(GRID_SIZE):
        line  = file_ptr.readline()[:-1]
        line = map(int, line.split(' '))
        arrangement[i, :] = np.array(line)
    return arrangement

def main():
    f = open(INPUT_FILE)
    f_out = open(OUTPUT_FILE, "w")
    num_of_samples = int(f.readline()[:-1])
    for sample in range(num_of_samples):

        answer_1  = int(f.readline()[:-1])
        arrangement_1 = np.zeros((GRID_SIZE, GRID_SIZE))
        for i in range(GRID_SIZE):
            line  = f.readline()[:-1]
            line = map(int, line.split(' '))
            arrangement_1[i, :] = np.array(line)

        row_1 = arrangement_1[answer_1 - 1, :]
        answer_2  = int(f.readline()[:-1])

        arrangement_2 = np.zeros((GRID_SIZE, GRID_SIZE))
        for i in range(GRID_SIZE):
            line  = f.readline()[:-1]
            line = map(int, line.split(' '))
            arrangement_2[i, :] = np.array(line)
        row_2 = arrangement_2[answer_2 - 1, :]

        common_elements = list(set(row_1).intersection(row_2))
        write_sample = sample + 1
        if(len(common_elements) == 1):
            f_out.write('Case #%d: %d\n'%(write_sample, int(common_elements[0])))
        if(len(common_elements) > 1):
            f_out.write('Case #%d: Bad magician!\n'%write_sample )
        if(len(common_elements) == 0):
            f_out.write('Case #%d: Volunteer cheated!\n'%write_sample)



    f.close()
    f_out.close()

if __name__ == "__main__":
    main()