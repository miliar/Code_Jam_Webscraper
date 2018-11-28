#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

const int maxn = 100 + 10;

int a[maxn], vis[maxn];
int f3[maxn][maxn][5];

int solve2(int n) {
    int ret = 0, cnt = 0;
    for (int i = 0; i < n; i ++) {
        if (a[i] % 2 == 0) {
            ret ++;
        } else {
            cnt ++;
        }
    }
    return ret + (cnt + 1) / 2;
}

int solve3(int n) {
    memset(f3, 0, sizeof(f3));
    int ret = 0, g1 = 0, g2 = 0;
    for (int i = 0; i < n; i ++) {
        int x = a[i] % 3;
        if (x == 0) {
            ret ++;
        } else if (x == 1) {
            g1 ++;
        } else {
            g2 ++;
        }
    }
    int mi = min(g1, g2);
    ret += mi;
    if (g1 > g2) {
        ret += ((g1 - mi) + 2) / 3;
    } else {
        ret += ((g2 - mi) + 2) / 3;
    }
    return ret;
}

int solve4(int n) {
    int ret = 0, g1 = 0, g2 = 0, g3 = 0;
    for (int i = 0; i < n; i ++) {
        int x = a[i] % 4;
        if (x == 0) ret ++;
        if (x == 1) g1 ++;
        if (x == 2) g2 ++;
        if (x == 3) g3 ++;
    }
    
    int p13 = min(g1, g3);
    g1 -= p13;
    g3 -= p13;
    
    int p1111 = g1 / 4;
    g1 -= p1111 * 4;
    int p3333 = g3 / 4;
    g3 -= p3333 * 4;
    
    int p22 = g2 / 2;
    g2 -= p22 * 2;
    
    ret += p13 + p1111 + p3333 + p22;
    if (g2) {
        if (g1 > 2 || g3 > 2) {
            ret += 2;
        } else {
            ret ++;
        }
    } else {
        if (g1 || g3) {
            ret ++;
        }
    }
    return ret;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, kase = 0; scanf("%d",&T);
    while (T--) {
        printf("Case #%d: ",++kase);
        int n, p; scanf("%d%d",&n,&p);
        for (int i = 0; i < n; i ++) {
            scanf("%d",&a[i]);
        }
        int res = 0;
        if (p == 2) res = solve2(n);
        if (p == 3) res = solve3(n);
        if (p == 4) res = solve4(n);
        printf("%d\n",res);
    
    }
    return 0;
}
