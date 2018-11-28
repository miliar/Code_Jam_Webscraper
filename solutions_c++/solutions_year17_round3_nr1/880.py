#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <queue>

using namespace std;

#define DEBUG

int T;
int n, k;
vector<pair<long double, long double> > p;
vector < long double > u;

long double foo() {
    long double best = 0;
    for (int i = 0; i < (1 << n); ++i) {
        if (__builtin_popcount(i) == k) {
            long double ans = 0;
            double max_r = 0;

            for (int j = 0; j < n; ++j) {
                if (i & (1 << j)) {
                    ans += 2 * M_PI * p[j].first * p[j].second;
                    max_r = max(max_r, (double)p[j].second);
                }
            }

            ans += M_PI * max_r * max_r;
            best = max(best, ans);
        }

    }

    return best;
}

bool cmp(int i, int j) {
    return p[i].first * p[i].second < p[j].first * p[j].second;
}

long double solve() {
    scanf("%d %d", &n, &k);

    p.resize(n);
    for (int i = 0; i < n; ++i) {
        scanf("%Lf %Lf", &p[i].second, &p[i].first);
    }

    u.resize(n);
    for (int i = 0; i < n; ++i) {
        u[i] = i;
    }

    sort(u.begin(), u.end(), cmp);

    long double best_ans = 0;

    for (int i = 0; i < n; ++i) {
        long double ans = M_PI * p[u[i]].second * p[u[i]].second + 2.0 * M_PI * p[u[i]].first * p[u[i]].second;

        int cnt = k - 1;
        for (int j = n - 1; j >= 0 && cnt > 0; --j) {
            if (j == i) {
                continue;
            }

            if (p[u[j]].second <= p[u[i]].second) {
                ans += 2 * M_PI * p[u[j]].first * p[u[j]].second;
                --cnt;
            }
        }

        best_ans = max(best_ans, ans);
    }

    return best_ans;
}

int main() {
    ios::sync_with_stdio(false);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %0.10Lf\n", t, solve());
    }

    return 0;
}