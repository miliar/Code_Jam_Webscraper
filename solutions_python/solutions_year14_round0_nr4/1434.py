__author__ = 'anoop'

import numpy as np
INPUT_FILE = 'D-large.in'
OUTPUT_FILE = 'D-large.out'
# INPUT_FILE = 'D-small-attempt0.in'
# OUTPUT_FILE = 'D-small-attempt0.out'

def main():
    f = open(INPUT_FILE)
    f_out = open(OUTPUT_FILE, "w")
    num_of_samples = int(f.readline()[:-1])
    for sample in range(num_of_samples):

        # (Naomi Score, Ken Score)
        genuine_score = [0,0]
        deceit_score = [0,0]

        num_of_blocks = int(f.readline()[:-1])

        line  = f.readline()[:-1]
        line = map(np.float64, line.split(' '))
        # line = [0.5, 0.1, 0.9]
        noami_blocks = np.sort(np.array(line))
        noami_blocks_1 = np.sort(np.array(line))


        line  = f.readline()[:-1]
        line = map(np.float64, line.split(' '))
        # line =[0.6, 0.4, 0.3]
        # num_of_blocks = 3
        ken_blocks = np.sort(np.array(line))[::-1]
        ken_blocks_1 = np.sort(np.array(line))[::-1]

        for i in range(num_of_blocks):

            #Calculate genuine score of both players

            naomi_plays = noami_blocks[i]
            ken_wins_with_these = ken_blocks[np.where(ken_blocks > naomi_plays)[0]]
            if(ken_wins_with_these.shape[0] > 0):ken_plays = ken_wins_with_these[-1]
            else: ken_plays = ken_blocks[-1]
            ken_blocks = np.delete(ken_blocks, np.where(ken_blocks == ken_plays))
            if(naomi_plays > ken_plays): genuine_score[0] = genuine_score[0] + 1
            else:genuine_score[1] = genuine_score[1] + 1

            #Calculate deceit score of both players

            ken_min_1 = np.min(ken_blocks_1)
            if(np.size(noami_blocks_1[np.where(noami_blocks_1 > ken_min_1)]) > 0):
                naomi_plays_1 = noami_blocks_1[np.where(noami_blocks_1 > ken_min_1)][0]
                noami_tells_1 = np.max(ken_blocks_1) + 0.0000001
            else:
                naomi_plays_1 = np.min(noami_blocks_1)
                noami_tells_1 = np.max(ken_blocks_1) - 0.0000001
            noami_blocks_1 = np.delete(noami_blocks_1, np.where(noami_blocks_1 == naomi_plays_1))
            ken_wins_with_these_1 = ken_blocks_1[np.where(ken_blocks_1 > noami_tells_1)[0]]
            if(ken_wins_with_these_1.shape[0] > 0):
                ken_plays_1 = ken_wins_with_these_1[-1]
            else:
                ken_plays_1 = ken_blocks_1[-1]
            ken_blocks_1 = np.delete(ken_blocks_1, np.where(ken_blocks_1 == ken_plays_1))
            if(naomi_plays_1 > ken_plays_1): deceit_score[0] = deceit_score[0] + 1
            else:deceit_score[1] = deceit_score[1] + 1

        write_sample = sample + 1
        f_out.write('Case #%d: %d %d\n'%(write_sample, deceit_score[0],  genuine_score[0]))

    f.close()
    f_out.close()

if __name__ == "__main__":
    main()