/*
 * tesuji
 * Google Code Jam 2017
 */

#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    char S[2000];
    int K;
    for (int i = 1; i <= T; ++i) {
        scanf("%s %d", S, &K);
        int lenS = strlen(S);
        int zeros = 0, flips = 0;
        for (int j = 0; j < lenS; ++j) {
            if (S[j] == '-') {
                ++zeros;
            }
        }
        for (int j = 0; j <= lenS - K; ++j) {
            if (S[j] == '-') {
                S[j] = '+';
                --zeros;
                ++flips;
                for (int k = 1; k < K; ++k) {
                    if (S[j + k] == '-') {
                        S[j + k] = '+';
                        --zeros;
                    } else {
                        S[j + k] = '-';
                        ++zeros;
                    }
                }
            }
        }

        printf("Case #%d:", i);
        if (zeros == 0) {
            printf(" %d", flips);
        } else {
            printf(" IMPOSSIBLE");
        }

        printf("\n");
    }
}
