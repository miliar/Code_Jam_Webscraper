#! /usr/bin/env python3
# -*- coding: utf8 -*-
# vim: expandtab ts=4 ai

def main():
    for c in range(int(input())):
        first_ans = int(input())
        first_spread = [];

        for i in range(4):
            first_spread.append(
                list( map(int,raw_input().split()) ))

        first_candidate = set(first_spread[first_ans-1])

        second_ans = int(input())
        second_spread = [];

        for i in range(4):
            second_spread.append(
                list( map(int,raw_input().split()) ))

        second_candidate = set(second_spread[second_ans-1])

        candidate = first_candidate & second_candidate

 
        if len(candidate) == 0:
            judge = 'Volunteer cheated!'
        elif len(candidate) == 1:
            judge = list(candidate)[0]
        else:
            judge = 'Bad magician!'

        print('Case #%d: %s' % ( c+1, judge ))

if __name__ == '__main__':
    main()
