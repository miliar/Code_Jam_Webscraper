#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define debug printf
typedef long long ll;

ll dp[19][10];

ll exp[19];
int num[19];

void solve(int T) {
    ll number; scanf("%lld", &number);
    for (int i = 0; i < 19; i++)
        num[i] = number / exp[i] % 10;

    for (int i = 0; i < 10; i++)
        dp[0][i] = i > num[0] ? -1 : num[0];
    int sf;
    for (sf = 1; sf < 19 && exp[sf] <= number; sf++) {
        ll best = -1;
        for (int v = 9; v >= 0; v--) {
            if (v == num[sf]) {
                ll pot = dp[sf-1][v];
                if (pot != -1)
                    best = max(best, v * exp[sf] + pot);
            } else if (v < num[sf]) {
                best = max(best, (v+1) * exp[sf] - 1);
            }
            dp[sf][v] = best;
        }
    }
    sf -= 1;
    printf("Case #%d: %lld\n", T, dp[sf][0]);
}

int main() {
    exp[0] = 1;
    for (int i = 1; i < 19; i++)
        exp[i] = exp[i-1] * 10;

    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
