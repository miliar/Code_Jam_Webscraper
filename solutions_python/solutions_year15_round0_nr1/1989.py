#!/usr/bin/python3

def main():
    n = int(input())

    for case in range(n):
        max_people, nums = input().split(" ")
        max_people = int(max_people)

        current = 0
        to_invite = 0

        for i in range(len(nums)):
            need_to_be_standing = i
            standing = current
            to_invite_here = 0

            if standing < need_to_be_standing:
                to_invite_here += need_to_be_standing - standing

            to_invite += to_invite_here
            current += to_invite_here
            current += int(nums[i])

        print("Case #{}: {}".format(case + 1, to_invite))

main()
