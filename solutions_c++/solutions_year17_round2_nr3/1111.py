#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

#ifndef _WIN32
#define gc getchar_unlocked
#else
#define gc getchar
#endif // _WIN32
void ri(int &a) {
    a = 0;
    register int x = gc();
    bool neg = false;
    while (x < '0' || x > '9') {
        if (x == '-') neg = true;
        x = gc();
    }
    while (x >= '0' && x <= '9') {
        a = (a << 3) + (a << 1) + (x-'0');
        x = gc();
    }
    if (neg) a = -a;
}

const int maxn = 105, INF = (1 << 30)-1;
int t, n, q;
int endur[maxn], speed[maxn];
int dist[maxn][maxn];
double dp[maxn];

int main() {
    freopen("output.out", "w", stdout);
    ri(t);
    for (int casenum = 1; casenum <= t; casenum++) {
        printf("Case #%d: ", casenum);
        ri(n), ri(q);
        for (int i = 0; i < n; i++) {
            ri(endur[i]), ri(speed[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ri(dist[i][j]);
            }
        }
        fill(dp, dp+n, 1e18);
        dp[0] = 0;
        for (int a, b; q--; ) {
            ri(a), ri(b);
            for (int i = 0; i < n-1; i++) {
                ll cdist = 0;
                for (int j = i+1; j < n; j++) {
                    cdist += dist[j-1][j];
                    if (cdist > endur[i]) {
                        break;
                    }
                    dp[j] = min(dp[j], dp[i]+(double)(cdist)/speed[i]);
                }
            }
            printf("%.9f\n", dp[n-1]);
            break;
        }
    }
    return 0;
}
