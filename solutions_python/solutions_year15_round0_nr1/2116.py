__author__ = 'carlos'

def threshold_crossed(num_list, threshold):
    count = 0

    for i in range( len(num_list) ):
        if count >= i:
            count += num_list[i]

    return count >= threshold


f = open('sample.txt', 'r')

output = open("output.txt", 'w')

num_trials = int( f.readline() )

trial_num = 1

for line in f:
    trial = line.split()
    threshold = int( trial[0] )
    audience = trial[1]

    aud_list = []

    for char in audience:
        aud_list.append( int( char ))

    mem_needed = 0

    while not threshold_crossed(aud_list, threshold):
        for i in range( len(aud_list) ):
            if aud_list[i] < 9:
                aud_list[i] += 1
                mem_needed += 1

            if threshold_crossed(aud_list, threshold):
                break

    output.write("Case #" + str(trial_num) + ": " + str(mem_needed) + '\n')
    trial_num += 1

output.close()
f.close()