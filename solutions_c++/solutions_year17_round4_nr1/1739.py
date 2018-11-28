#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int T;
int f[110][110][110];
int a[4];
int main() {
    cin >> T;

    for (int t = 1; t <= T ; ++t)
    {
        int n, m = 0, p, ans = 0;
        memset(f, -0x3f, sizeof(f));
        memset(a, 0, sizeof(a));
        cin >> n >> p;
        for (int i = 0; i < n; ++i)
        {
            int x;
            cin >> x;
            if (x % p)
            {
                ++m;
                ++a[x % p];
            }
            else
                ++ans;
        }
        n = m;
        f[0][0][0] = 0;
        for (int l = 0; l < m; ++l)
            for (int i = 0; i <= l; ++i)
                for (int j = 0; i + j <= l; ++j)
                {
                    int k = l - i - j;
                    int left = (i + 2 * j + 3 * k) % p;
                    int newnum = f[l][i][j] + (left?0:1);
                    if (i < a[1])
                        f[l + 1][i + 1][j] = max(f[l + 1][i + 1][j], newnum);
                    if (i < a[2])
                        f[l + 1][i][j + 1] = max(f[l + 1][i][j + 1], newnum);
                    if (i < a[3])
                        f[l + 1][i][j] = max(f[l + 1][i][j], newnum);
                }
        cout << "Case #" << t << ": " << f[n][a[1]][a[2]] + ans << endl;
    }

	return 0;
}
