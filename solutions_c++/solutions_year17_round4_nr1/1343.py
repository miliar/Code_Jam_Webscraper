#include <bits/stdc++.h>
using namespace std;

const int N = 101;

int n, t, p, cnt[4];
int f[N][N][N][4];

int cal(int a, int b, int c, int d) {
    int &ret = f[a][b][c][d];
    if (ret != -1) return ret;
    ret = 0;
    if (a + 1 <= cnt[1]) {
        ret = max(ret, cal(a + 1, b, c, (d + 1) % p) + (!d));
    }
    if (b + 1 <= cnt[2]) {
        ret = max(ret, cal(a, b + 1, c, (d + 2) % p) + (!d));
    }
    if (c + 1 <= cnt[3]) {
        ret = max(ret, cal(a, b, c + 1, (d + 3) % p) + (!d));
    }
    return ret;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        memset(cnt, 0, sizeof(cnt));
        cin >> n >> p;
        while (n--) {
            int x; cin >> x; cnt[x % p]++;
        }
        for (int i = 0; i <= cnt[1]; ++i) {
            for (int j = 0; j <= cnt[2]; ++j) {
                for (int k = 0; k <= cnt[3]; ++k) {
                    for (int l = 0; l < 4; ++l) {
                        f[i][j][k][l] = -1;
                    }
                }
            }
        }
        cout << "Case #" << T << ": " << cal(0, 0, 0, 0) + cnt[0] << '\n';
    }
}
