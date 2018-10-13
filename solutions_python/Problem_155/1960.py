import argparse

cmd_parser = argparse.ArgumentParser(description='GCJ 2015 - Store Credit')
cmd_parser.add_argument('-i', dest='infile', required=True)

args = cmd_parser.parse_args()


datain = open(args.infile, 'r') # open data file for reading
dataout = open(args.infile + '.out', 'w') # open output file

num_cases = int(datain.readline())
print("Processing %d cases." % num_cases)

for i in range(0, num_cases):
    dataout.write("Case #{0}: ".format(i+1)) # write case id to file

    case = datain.readline().split()
    max_shyness = int(case[0])

    shy_vect = case[1]
    cur_standing = 0
    friends_needed = 0

    for level, members in enumerate(shy_vect):
        # get number of audience members who will stand at this level
        m = int(members)
        
        # determine if there are enough currently standing members for these
        # members to stand up
        if cur_standing >= level:
            # Alright! This group will stand :)
            cur_standing += m
        else:
            # These members are too shy. Let's send just enough friends to
            # encourage them.
            friends_needed += (level - cur_standing)
            # Hooray! Everybody's standing!
            cur_standing +=   (level - cur_standing) + m
        
    dataout.write('{0}\n'.format(friends_needed))

print('done')
