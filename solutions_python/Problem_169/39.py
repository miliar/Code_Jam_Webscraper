#!/usr/bin/env python3.4
import sys
import math

if __name__ == '__main__':
    for test_case in range(int(sys.stdin.readline())):
        sys.stdout.write('Case #{}: '.format(test_case + 1))
        num, vol, tem = map(float, sys.stdin.readline().split())
        num = int(num)
        faucet = []
        for i in range(num):
            faucet.append(tuple(map(float, sys.stdin.readline().split())))
        if num == 1:
            if faucet[0][1] == tem:
                print(vol / faucet[0][0])
            else:
                print('IMPOSSIBLE')
        elif faucet[0][1] == faucet[1][1]:
            if faucet[0][1] == tem:
                print(vol / (faucet[0][0] + faucet[1][0]))
            else:
                print('IMPOSSIBLE')
        else:
            ma = max(faucet[0][1], faucet[1][1])
            mi = min(faucet[0][1], faucet[1][1])
            if tem < mi or ma < tem:
                print('IMPOSSIBLE')
            else:
                q = (vol * tem - faucet[0][1] * vol) / (faucet[1][1] - faucet[0][1])
                p = vol - q
                print(max(p / faucet[0][0], q / faucet[1][0]))
