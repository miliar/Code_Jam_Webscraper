import csv
import os
os.chdir("/home/user/Dokumentumok")


def guests_required(S_max, aud):
    people_standing = 0
    invited_guests = 0
    print aud
    for S_i in range(0, int(S_max)+1):
        print "S_i"
        print S_i
        if people_standing + invited_guests > d_reader[x].split()[0]:
            break
        if (S_i > people_standing + invited_guests) & (int(aud[S_i]) != 0):
            invited_guests = S_i - people_standing
            print ("invite {}".format(invited_guests))
        people_standing = int(aud[S_i]) + people_standing
        print people_standing
    return invited_guests


# this creates a new file object: open's first argument is the file's name, "w: is for writing
f = open("Standing_ovation_out.txt", "w")

with open("A-large.in", "r") as opera_A:
    d_reader = opera_A.readlines()
    for x in range(1, int(d_reader[0])+1):
        sol = guests_required(d_reader[x].split()[0], list(d_reader[x].split()[1]))
        sentence = "Case #{}: {}\n".format(x, sol)
        f.write(sentence)
        print(sentence)
        print(d_reader[x])
        print(d_reader[x].split()[0])



# if we open a file object, we have to close it, too. Upon closing, it gets saved.
f.close()



opera_A.close()





