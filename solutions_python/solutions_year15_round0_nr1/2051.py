g = open("A-large.in")

'''
input_string = """4
4 11111
1 09
5 110011
0 0"""
'''

if __name__ == "__main__":
    #inputs = input_string.split("\n")[1:]

    # throw away the first line
    numlines = int(g.readline().replace("\n",''))

    # open a file to store the output
    f = open("ovation.out", "w")
    
    j = 1
    
    for input_args in g.readlines():
        args = input_args.replace("\n",'').split(" ")
        S_max = int(args[0])
        num_members_by_S_i = [int(d) for d in args[1]]
        num_friends_to_invite = 0

        for i in range(S_max + 1):
            num_already_standing = sum(num_members_by_S_i[0:i])
            if num_already_standing < i:
                # record the number of friends you'll have to invite
                num_friends_to_invite += i - num_already_standing
                # add them to the tier one lower than the one you're checking
                num_members_by_S_i[i] += i - num_already_standing

        #print "Case #" + str(j) + ":", str(num_friends_to_invite)
        f.write("Case #" + str(j) + ": " + str(num_friends_to_invite) + "\n")
        j += 1

    f.close()
