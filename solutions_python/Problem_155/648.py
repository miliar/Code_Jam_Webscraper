#!/usr/bin/env python3

def invite_standing(people):
    accumulate = 0
    friend_invites = 0
    for shyness, audience in enumerate(people):
        shortage = max(0, shyness - accumulate)
        accumulate += audience + shortage
        friend_invites += shortage
    return friend_invites


for case in range(int(input())):
    _, raw_people = input().split()
    people = [int(i) for i in raw_people]
    ans = invite_standing(people)
    print('Case #{}: {}'.format(case+1, ans))
