#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

int n, p;
int cnt[10];
int f[MAXN][MAXN][MAXN][4], g[MAXN][MAXN][MAXN][4];

void solve() {
    for(int i = 0; i <= n; ++i)
        for(int j = 0; j <= n; ++j)
            for(int k = 0; k <= n; ++k)
                for(int t = 0; t <= p; ++t)
                    f[i][j][k][t] = -INF;
    f[0][0][0][0] = 0;
    for(int ii = 0; ii < cnt[1] + cnt[2] + cnt[3]; ++ii) {
        for(int i = 0; i <= cnt[1]; ++i)
            for(int j = 0; j <= cnt[2]; ++j)
                for(int k = 0; k <= cnt[3]; ++k)
                    for(int t = 0; t < p; ++t)
                        g[i][j][k][t] = -INF;
        for(int i = 0; i <= cnt[1]; ++i)
            for(int j = 0; j <= cnt[2]; ++j) {
                int k = ii - i - j;
                if ((k >= 0) && (k <= cnt[3])) {
                    for(int t = 0; t < p; ++t)
                    if (f[i][j][k][t] >= 0) {
                        if (i < cnt[1]) {
                            g[i + 1][j][k][(t + 1) % p] = max(g[i + 1][j][k][(t + 1) % p], f[i][j][k][t] + ((t + 1) % p == 0));
                        }
                        if (j < cnt[2]) {
                            g[i][j + 1][k][(t + 2) % p] = max(g[i][j + 1][k][(t + 2) % p], f[i][j][k][t] + ((t + 2) % p == 0));
                        }
                        if (k < cnt[3]) {
                            g[i][j][k + 1][(t + 3) % p] = max(g[i][j][k + 1][(t + 3) % p], f[i][j][k][t] + ((t + 3) % p == 0));
                        }
                    }
                }
            }
        for(int i = 0; i <= cnt[1]; ++i)
            for(int j = 0; j <= cnt[2]; ++j)
                for(int k = 0; k <= cnt[3]; ++k)
                    for(int t = 0; t < p; ++t)
                        f[i][j][k][t] = g[i][j][k][t];
    }

    int res = 0;
    for(int i = 0; i < p; ++i) res = max(res, f[cnt[1]][cnt[2]][cnt[3]][i]);
    ++res;
    int x = (cnt[1] * 1 + cnt[2] * 2 + cnt[3] * 3) % p;
    res -= ((x % p) == 0);
    res += cnt[0];
    cout << res << endl;
}

void run() {
    cin >> n >> p;
    for(int i = 0; i <= 4; ++i) cnt[i] = 0;
    int s = 0;
    for(int i = 1; i <= n; ++i) {
        int j; cin >> j;
        ++cnt[j % p];
        s = (s + j) % p;
    }
    solve();
    return;
    int res = 0;
    if (p == 2) {
        res = cnt[0] + cnt[1] / 2;
    }
    else if (p == 3) {
        res = cnt[0];
        int x = 0;
        for(int i = 0; i <= cnt[1]; ++i)
            if (i <= cnt[2])
                x = max(x, i + cnt[1] / 3);
        res += x;
    }
    else {
        res = cnt[0];
        int x = 0;
        for(int i = 0; i <= cnt[2]; ++i)
            for(int j = 0; j <= cnt[2] - i; ++j) {
                if ((i <= cnt[1]) && (j <= cnt[3])) {
                    cnt[3] += i; cnt[1] += j;
                    cnt[2] -= i + j;
                    x = max(x, cnt[2] / 2 + min(cnt[1], cnt[3]));
                    cnt[3] -= i; cnt[1] -= j;
                    cnt[2] += i + j;
                }
            }
        res += x;
    }
    res -= (s == 0);
    res++;
    cout << res << "\n";
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cerr << tc << "\n";
        cout << "Case #" << tc << ": ";
        run();
    }
}

