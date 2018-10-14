import sys
import numpy as np

def solve(s_max, audience):
    friends = 0
    stood_up = 0
    for i in range(len(audience)):
        members = int(audience[i])
        if members > 0:
            if i > (stood_up+friends):
                friends += i-(stood_up+friends)
            stood_up += members
            if (stood_up+friends) >= s_max:
                break
    return friends


if __name__ == '__main__':
    f_in = open('A-large.in', 'r')
    f_out = open('out_large.txt', 'w')
    cases = int(f_in.readline())
    for i in range(cases):
        [s_max, audience] = f_in.readline().split()
        friends = solve(int(s_max), audience)
        f_out.write('Case #' + str(i+1) + ": " + str(friends) + "\n")