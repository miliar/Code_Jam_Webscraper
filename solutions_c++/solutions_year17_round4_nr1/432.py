#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 110

using namespace std;

int n, p, ans;
int w[MaxN];
int counts[5];
bool vis[MaxN][MaxN][MaxN];
int f[MaxN][MaxN][MaxN];

int search(int a, int b, int c, int d) {
    if (vis[a][b][c] == 1) {
        return f[a][b][c];
    }
    vis[a][b][c] = 1;

    if (a > 0) {
        f[a][b][c] = max(f[a][b][c], search(a - 1, b, c, (d + 1) % p) + (d == 0));
    }
    if (b > 0) {
        f[a][b][c] = max(f[a][b][c], search(a, b - 1, c, (d + 2) % p) + (d == 0));
    }
    if (c > 0) {
        f[a][b][c] = max(f[a][b][c], search(a, b, c - 1, (d + 3) % p) + (d == 0));
    }
    return f[a][b][c];
}

int main() {
    int T, T0 = 0;
    scanf("%d", &T);
    for ( ; T; --T) {
        memset(counts, 0, sizeof(counts));
        memset(f, 0, sizeof(f));
        memset(vis, 0, sizeof(vis));
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &w[i]);
            w[i] %= p;
            ++counts[w[i]];
        }
        ans = counts[0] + search(counts[1], counts[2], counts[3], 0);
        printf("Case #%d: %d\n", ++T0, ans);
    }
}
