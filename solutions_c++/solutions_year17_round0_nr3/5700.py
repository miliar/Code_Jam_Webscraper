#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <cmath>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define X first
#define Y second

const int maxn = 1010;

bool v[maxn];

void pre() {
}

void solve() {
    int n, K;
    scanf("%d%d", &n, &K);
    set<int> S;
    S.insert(0);
    S.insert(n + 1);
    int u, v;
    while (K--) {
        int arg;
        u = -1;
        for (int i = 1; i <= n; ++i) {
            if (S.find(i) != S.end()) continue;
            auto iter = S.lower_bound(i);
            int x = *iter - i - 1;
            --iter;
            int y = i - *iter - 1;
            // printf("eval: at i = %d, l = %d, r = %d\n", i, y, x);
            if (x > y) swap(x, y);
            if (x > u || (x == u && y > v)) {
                u = x, v = y, arg = i;
            }
        }
        // printf("arg = %d\n", arg);
        S.insert(arg);
    }
    printf("%d %d", v, u);
}

int main() {
#ifdef __WYL__
    freopen("t.in", "r", stdin);
    // freopen("t.out", "w", stdout);
#endif

    pre();

    int T;
    scanf("%d\n", &T);
    for (int _T = 1; _T <= T; ++_T) {
        printf("Case #%d: ", _T);
        solve();
        printf("\n");
    }

#ifdef __WYL__
    fclose(stdin);
    fclose(stdout);
#endif
    return 0;
};
