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

const int maxn = 1010;

int a[maxn];

void solve() {
    int n, A, B, C;
    scanf("%d%d%*d%d%*d%d%*d", &n, &A, &B, &C);
    char cl[] = {"RYB"};
    if (A < B) swap(A, B), swap(cl[0], cl[1]);
    if (B < C) swap(B, C), swap(cl[1], cl[2]);
    if (A < B) swap(A, B), swap(cl[0], cl[1]);
    // printf("%d %d %d %d\n", n, A, B, C);
    if (A > n / 2) {
        printf("IMPOSSIBLE\n");
        return;
    }
    for (int i = 0; i < n; ++i) {
        a[i] = 0;
    }
    int p = 0;
    // printf("=>\n");
    while (A--) {
        // printf("%d: %d\n", p, 1);
        a[p] = 1;
        p = (p + 2) % n;
    }
    while (B--) {
        while (a[p]) {
            p = (p + 1) % n;
        }
        // printf("%d: %d\n", p, 2);
        a[p] = 2;
        p = (p + 2) % n;
    }
    while (C--) {
        while (a[p]) {
            p = (p + 1) % n;
        }
        // printf("%d: %d\n", p, 3);
        a[p] = 3;
    }
    for (int i = 0; i < n; ++i) {
        printf("%c", cl[a[i] - 1]);
    }
    printf("\n");
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
