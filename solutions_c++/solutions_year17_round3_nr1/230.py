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
#define _USE_MATH_DEFINES
#include <cmath>
#include <cassert>

#define __GCJ__

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn = 1010;

pii a[maxn];

void solve() {
    int n, K;
    scanf("%d%d", &n, &K);
    for (int i = 0; i < n; ++i) {
        int r, h;
        scanf("%d%d", &r, &h);
        a[i] = pii(r, h);
    }
    sort(a, a + n);
    // printf("candidate: ");
    // for (int i = 0; i < n; ++i) {
        // printf("(%d %d) ", a[i].X, a[i].Y);
    // }
    vector<ll> H;
    double ans = 0;
    const double pi = M_PI;
    for (int i = K - 1; i < n; ++i) {
        H.clear();
        for (int j = 0; j < i; ++j) {
            H.push_back((ll)a[j].X * a[j].Y);
        }
        sort(H.begin(), H.end(), std::greater<ll>());
        ll sumH = (ll)a[i].X * a[i].Y;
        for (int j = 0; j < K - 1; ++j) {
            sumH += H[j];
        }
        double r = a[i].X;
        // printf("r = %.10lf, sumH = %lld\n", r, sumH);
        ans = max(ans, pi * (r * r + 2.0 * sumH));
    }
    printf("%.10lf\n", ans);
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
