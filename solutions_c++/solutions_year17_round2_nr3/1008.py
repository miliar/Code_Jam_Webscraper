#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <utility>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <cmath>
#include <cassert>

#include <limits>

#define __GCJ__

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn = 10010;

int e[maxn], s[maxn], d[maxn];
double f[maxn];

void solve() {
    int n;
    scanf("%d%*d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", e + i, s + i);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int u;
            scanf("%d", &u);
            if (i + 1 == j) {
                d[i] = u;
            }
        }
    }
    scanf("%*d%*d");
    f[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
        int dis = 0;
        f[i] = std::numeric_limits<double>::max();
        for (int j = i + 1; j < n; ++j) {
            dis += d[j - 1];
            if (dis > e[i]) {
                break;
            }
            f[i] = min(f[i], f[j] + (double)dis / s[i]);
        }
    }
    printf("%.10lf\n", f[0]);
}

int main() {
#ifdef __WYL__
    freopen("t.in", "r", stdin);
    // freopen("t.out", "w", stdout);
#endif

#ifdef __GCJ__
    int __T;
    scanf("%d\n", &__T);
    for (int __i = 1; __i <= __T; ++__i) {
        printf("Case #%d: ", __i);
        solve();
    }
#else
    solve();
#endif

#ifdef __WYL__
    fclose(stdin);
    fclose(stdout);
#endif
    return 0;
};
