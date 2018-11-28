#include <iostream>
#include <fstream>
#include <algorithm>
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

typedef long long ll;

using namespace std;

#define X first
#define Y second

const int maxn = 1010;

int d[maxn];
ll pt[maxn];

void pre() {
    pt[0] = 1;
    for (int i = 1; i <= 19; ++i) {
        pt[i] = pt[i - 1] * 10;
    }
}

void solve() {
    ll n;
    scanf("%lld", &n);
    ++n;
    int m = 0;
    for (; n; n /= 10) {
        d[m] = n % 10;
        ++m;
    }
    ll s = 0;
    ll ans = 0;
    int cur = -1;
    for (int i = m - 1; i >= 0; --i) {
        if (d[i] < cur) {
            break;
        }
        s += d[i] * pt[i];
        if (d[i] - 1 >= cur) {
            ans = max(ans, s - 1);
        }
        cur = d[i];
    }
    printf("%lld", ans);
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
