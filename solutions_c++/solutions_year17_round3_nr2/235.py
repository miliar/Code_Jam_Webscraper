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

#define __GCJ__

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxt = 24 * 60;
// 0 - C, 1 - J

bool can[maxt][2];
int f[maxt + 1][maxt + 1][2];

void solve() {
    int n, m;
    scanf("%d%d", &n, &m);
    memset(can, true, sizeof(can));
    for (int i = 0; i < n; ++i) {
        int x, y;
        scanf("%d%d", &x, &y);
        for (int j = x; j < y; ++j) {
            can[j][0] = false;
        }
    }
    for (int i = 0; i < m; ++i) {
        int x, y;
        scanf("%d%d", &x, &y);
        for (int j = x; j < y; ++j) {
            can[j][1] = false;
        }
    }
    const int M = maxt;
    int ans = M;
    for (int start = 0; start < 2; ++start) {
        f[0][0][start] = 0;
        f[0][0][1 - start] = M;
        for (int i = 1; i <= maxt; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (can[i - 1][0] && j > 0) {
                    f[i][j][0] = min(f[i - 1][j - 1][0], f[i - 1][j - 1][1] + 1);
                } else {
                    f[i][j][0] = M;
                }
                if (can[i - 1][1] && j < i) {
                    f[i][j][1] = min(f[i - 1][j][0] + 1, f[i - 1][j][1]);
                } else {
                    f[i][j][1] = M;
                }
            }
        }
        ans = min(ans, f[maxt][maxt / 2][start]);
    }
    printf("%d\n", ans);
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
