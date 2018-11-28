//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

long long pows[19];
int ans[19];

long long getNumber() {
    long long x = 0;
    for(int i = 0; i < 18; i++)
        x += pows[i] * ans[17 - i];
    return x;
}

void solveB(int testNumber) {
    long long x;
    cin >> x;
    pows[0] = 1;
    for (int i = 1; i < 18; i++)
        pows[i] = pows[i - 1] * 10;
    memset(ans, -1, sizeof(ans));
    int minAllowed = 0;
    for (int i = 0; i < 18; i++) {
        for (int digit = 9; digit >= minAllowed; digit--) {
            for (int j = i; j < 18; j++)
                ans[j] = digit;
            if (getNumber() <= x) {
                minAllowed = digit;
                break;
            }
        }
    }
    printf("Case #%d: %lld\n", testNumber, getNumber());
}

void runB() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
        solveB(i + 1);
}