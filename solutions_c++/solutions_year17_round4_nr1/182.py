#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int dp[128][128][128][4];

int n, p;
int a[128];

void read() {
    scanf("%d%d", &n, &p);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
}

int go(int x, int y, int z, int e) {
    if (!x && !y && !z) return 0;
    int &ans = dp[x][y][z][e];
    if (ans != -1) {
        return ans;
    }
    ans = 0;

    if (x) {
        ans = max(ans, go(x - 1, y, z, (e + 1) % p) + !e);
    }
    if (y) {
        ans = max(ans, go(x, y - 1, z, (e + 2) % p) + !e);
    }
    if (z) {
        ans = max(ans, go(x, y, z - 1, (e + 3) % p) + !e);
    }
    return ans;
}


void solve() {
    int c[8];
    memset(c, 0, sizeof c);
    for (int i = 0; i < n; i++) {
        c[ a[i] % p ] ++;
    }

    memset(dp, -1, sizeof dp);
    printf ("%d\n", go(c[1], c[2], c[3], 0) + c[0]);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

