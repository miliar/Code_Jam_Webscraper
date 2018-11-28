#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int test, tt;
int p, n, g[4];

int d[101][101][101][4];

int solve(int a, int b, int c, int rem) {
    if (d[a][b][c][rem] != -1) {
        return d[a][b][c][rem];
    }
    if (a == 0 && b == 0 && c == 0) {
        return 0;
    }
    int ans = 12341234;
    if (a > 0) ans = min(ans, solve(a - 1, b, c, (rem + 1) % p));
    if (b > 0) ans = min(ans, solve(a, b - 1, c, (rem + 2) % p));
    if (c > 0) ans = min(ans, solve(a, b, c - 1, (rem + 3) % p));
    if (rem > 0) ++ans;
    return d[a][b][c][rem] = ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &p);
        forn(i, 4) g[i] = 0;
        forn(i, n) {
            int x;
            scanf("%d", &x);
            ++g[x % p];
        }
        memset(d, -1, sizeof d);
        int ans = n - solve(g[1], g[2], g[3], 0);
        printf("%d\n", ans);
        cerr << "Done " << test << endl;
    }
    return 0;
}
