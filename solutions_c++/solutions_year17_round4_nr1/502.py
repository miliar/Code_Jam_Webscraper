#include <bits/stdc++.h>
using namespace std;
const int N = 128;

int f[N][N][N][4];
int d[4];
int n, p;

int dfs(int x, int y, int z, int k) {
    if (x == 0 && y == 0 && z == 0 && k == 0) return 0;
    if (f[x][y][z][k] > -1) return f[x][y][z][k];
    int ret = 0;
    //printf("%d %d %d %d\n", x, y, z, k);
    if (x) {
        ret = max(ret, dfs(x - 1, y, z, (k - 1 + p) % p) + ((k - 1 + p) % p == 0));
    }
    if (y) {
        ret = max(ret, dfs(x, y - 1, z, (k - 2 + p) % p) + ((k - 2 + p) % p == 0));
    }
    if (z) {
        ret = max(ret, dfs(x, y, z - 1, (k - 3 + p) % p) + ((k - 3 + p) % p == 0));
    }
    f[x][y][z][k] = ret;
    return ret;
}

int main() {
    int T, x;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &p);
        memset(d, 0, sizeof d);
        for (int i = 0; i < n; ++ i) {
            scanf("%d", &x);
            d[x % p]++;
        }
        memset(f, -1, sizeof f);
        printf("Case #%d: %d\n", cas, d[0] + dfs(d[1], d[2], d[3], (d[1] + 2*d[2] + 3*d[3]) % p));
    }
    return 0;
}
