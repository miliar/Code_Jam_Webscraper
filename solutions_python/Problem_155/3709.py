#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(user_input):
    users = user_input.split()[1]
    current_users = 0
    needed_users = 0
    for i in range(0, len(users)):
        if int(users[i]) != 0:
            if i <= current_users:
                current_users += int(users[i])
            else:
                needed_users += (i - current_users)
                current_users += (needed_users + int(users[i]))
    return needed_users

if __name__ == "__main__":
    testcases = input()
    
    for caseNr in xrange(1, testcases+1):
        user_input = raw_input()
        print("Case #%i: %s" % (caseNr, solve(user_input)))