#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef double LF;

const int maxN = 1000 + 5;

int T, D, n;
int K[maxN], S[maxN];

LF maxT, ans;
LF t[maxN];

int main() {
    //freopen("1.in", "r", stdin);
    //freopen("1.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%d%d", &D, &n);
        maxT = 0.0;
        for (int i = 1; i <= n; ++i) {
            scanf("%d%d", &K[i], &S[i]);
            t[i] = (LF)(D - K[i]) / (LF)S[i];
            maxT = max(maxT, t[i]);
        }
        ans = (LF)D / maxT;
        printf("Case #%d: %.7f\n", testCase, ans);

    }
    return 0;
}
