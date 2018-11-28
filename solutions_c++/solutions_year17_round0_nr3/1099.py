/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/08
 *  Name:
 *      c.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int cas, now, bef;
long long n, k, l, r;
pair<long long, long long> dp[4];
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%lld%lld", &n, &k);
        now = 0, bef = 1;
        dp[now << 1 | 0] = make_pair(n, 1);
        dp[now << 1 | 1] = make_pair(n + 1, 0);
        for (long long step = 0;;) {
            swap(now, bef);
            dp[now << 1 | 0] = make_pair((dp[bef << 1 | 0].first - 1) >> 1, 0);
            dp[now << 1 | 1] = make_pair((dp[bef << 1 | 1].first - 0) >> 1, 0);
#ifdef DEBUG
            printf("step = %lld, dp[bef][0] = (%lld, %lld)\n", step, dp[bef << 1 | 0].first, dp[bef << 1 | 0].second);
            printf("step = %lld, dp[bef][1] = (%lld, %lld)\n", step, dp[bef << 1 | 1].first, dp[bef << 1 | 1].second);
#endif
            step += dp[bef << 1 | 1].second;
            if (step >= k) {
                l = dp[bef << 1 | 1].first;
                r = (l - 1) >> 1;
                l >>= 1;
                break;
            }
            if (dp[bef << 1 | 1].first & 1) {
                dp[now << 1 | 1].second += dp[bef << 1 | 1].second << 1;
            } else {
                dp[now << 1 | 0].second += dp[bef << 1 | 1].second;
                dp[now << 1 | 1].second += dp[bef << 1 | 1].second;
            }

            if (dp[bef << 1 | 0].first != 0) {
                step += dp[bef << 1 | 0].second;
                if (step >= k) {
                    l = dp[bef << 1 | 0].first;
                    r = (l - 1) >> 1;
                    l >>= 1;
                    break;
                }
                if (dp[bef << 1 | 0].first & 1) {
                    dp[now << 1 | 0].second += dp[bef << 1 | 0].second << 1;
                } else {
                    dp[now << 1 | 0].second += dp[bef << 1 | 0].second;
                    dp[now << 1 | 1].second += dp[bef << 1 | 0].second;
                }
            }
            
        }
        printf("Case #%d: %lld %lld\n", t, l, r);
    }
    return 0;
}
