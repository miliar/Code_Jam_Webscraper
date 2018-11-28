#!/usr/bin/env python3

def solve():
    return None


T = int(input())

for case_number in range(1, T+1):
    D, N = map(int, input().split())
    annie_speed = float('inf')

    for n in range(N):
        Ki, Si = map(int, input().split())
        yi = D - Ki
        xi = yi / Si
        speed_i = D / xi
        annie_speed = min(annie_speed, speed_i)

    print('Case #%d:' % case_number, annie_speed)
