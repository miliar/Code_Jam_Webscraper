
import csv
import itertools
import copy


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        smax, tmp = csv_r.next()
        shy_lvl=[int(e) for e in tmp]
        test_lst.append([int(smax), shy_lvl])
    f.close() 
    return test_lst 


def is_ok(shy_lvl):
    up = 0
    for shy_id, nb_people in enumerate(shy_lvl):
        if shy_id <= up:
            up += nb_people
    return up == sum(shy_lvl)


def fill_with_new_friends(shy_lvl, nfriends):
    remaining_friends = nfriends
    for i_e, e in enumerate(shy_lvl):
        nseats = 9 - e
        friends = min(remaining_friends, nseats)
        shy_lvl[i_e] += friends
        remaining_friends -= friends
        if remaining_friends == 0:
            break



def solve_test(test_case):
    smax, shy_lvl = test_case
    max_friends = len(shy_lvl)
    for i in xrange(max_friends+1):
        loc_shy_lvl = copy.deepcopy(shy_lvl)
        fill_with_new_friends(loc_shy_lvl, i)
        #print "testing ", loc_shy_lvl
        if is_ok(loc_shy_lvl):
            return i


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %i" % (1+i_test, res)
        ##check_res(test_case, res)


if __name__ == '__main__':
    main('./A-large.in')
    #main('./simple.in')

