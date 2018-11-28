#include <bits/stdc++.h>
using namespace std;
const int MAXN = 111;
int a[MAXN], f[MAXN][MAXN][MAXN], cnt[4], n, p;
int main()
{
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        cout << "Case #" << cas << ": ";

        memset(f, 0, sizeof(f));
        memset(cnt, 0, sizeof(cnt));

        cin >> n >> p;
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i];
            cnt[a[i] % p]++;
        }
        f[0][0][0] = 0;
        for (int i = 0; i <= cnt[1]; i++)
        {
            for (int j = 0; j <= cnt[2]; j++)
            {
                for (int k = 0; k <= cnt[3]; k++)
                {
                    if (i + j + k == 0)
                        continue;
                    int tmp = (cnt[1] - i) + (cnt[2] - j) * 2 + (cnt[3] - k) * 3;
                    tmp %= p;
                    if (i > 0)
                        f[i][j][k] = max(f[i][j][k], f[i - 1][j][k]);
                    if (j > 0)
                        f[i][j][k] = max(f[i][j][k], f[i][j - 1][k]);
                    if (k > 0)
                        f[i][j][k] = max(f[i][j][k], f[i][j][k - 1]);
                    if (tmp == 0)
                        f[i][j][k]++;
                }
            }
        }
        cout << cnt[0] + f[cnt[1]][cnt[2]][cnt[3]] << endl;
    }
    return 0;
}
