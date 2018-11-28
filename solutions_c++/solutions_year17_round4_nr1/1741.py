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

void solve() {
    int n, p;
    scanf("%d%d", &n, &p);
    int c[9];
    for (int i = 0; i < p; ++i) {
        c[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        c[x % p]++;
    }
    int ans = 0;
    if (p == 2) {
        ans += c[0];
        ans += (c[1] + 1) / 2;
    } else if (p == 3) {
        ans += c[0];
        int x = c[1], y = c[2];
        if (x > y) swap(x, y);
        ans += x;
        ans += ((y - x) + 2) / 3;
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
