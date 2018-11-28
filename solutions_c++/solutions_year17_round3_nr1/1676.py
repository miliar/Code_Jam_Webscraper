#include <cstdio>
#include <cmath>
#include <cassert>
#include <vector>
#include <unordered_map>
using namespace std;

typedef pair<long long, long long> pll;
typedef pair<long double, long long> pdi;
const long double PI = acos(-1.0);
pll cake[1004];

inline long double addup(const pll &down, const pll &up) {
    long double c = (down.first * down.first - up.first * up.first) * PI;
    long double h = 2 * PI * down.first * down.second;
    return c + h;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        int N, K;
        scanf("%d%d", &N, &K);
        for(int i=1; i<=N; ++i)
            scanf("%lld%lld", &cake[i].first, &cake[i].second);
        sort(&cake[1], &cake[N+1], [](const pll &l, const pll &r) {
            return l.first < r.first;
        });
        cake[0] = {0, 0};

        long double ans = 0;
        vector<pdi> dp(K+1, {0, 0});
        for(int i=1; i<=N; ++i)
            for(int j=K; j>0; --j) {
                long double nowA = dp[j-1].first + addup(cake[i], cake[dp[j-1].second]);
                ans = max(ans, nowA);
                if( dp[j].first - cake[dp[j].second].first * cake[dp[j].second].first * PI
                        < nowA - cake[i].first * cake[i].first * PI )
                    dp[j] = {nowA, i};
            }

        printf("Case #%d: %.9Lf\n", NCASE, ans);
    }
    return 0;
}
