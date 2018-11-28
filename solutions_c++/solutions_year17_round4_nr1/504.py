#include <bits/stdc++.h>
using namespace std;
int T;
int n, p;
const int N = 105;
int f[N][N][3], g[N][N][N][4];
int main()
{
    for (int i = 0; i < N; ++ i)
        for (int j = 0; j < N; ++ j)
            for (int k = 0; k < 3; ++ k)
            {
                if (i) f[i][j][k] = max(f[i][j][k], f[i - 1][j][(k + 1) % 3] + ((k + 1) == 3));
                if (j) f[i][j][k] = max(f[i][j][k], f[i][j - 1][(k + 2) % 3] + ((k + 2) == 3));
            }
    for (int i = 0; i < N; ++ i)
        for (int j = 0; j < N; ++ j)
            for (int k = 0; k < N; ++ k)
                for (int p = 0; p < 4; ++ p)
                {
                    if (i) g[i][j][k][p] = max(g[i][j][k][p], g[i - 1][j][k][(p + 1) % 4] + ((p + 1) == 4));
                    if (j) g[i][j][k][p] = max(g[i][j][k][p], g[i][j - 1][k][(p + 2) % 4] + ((p + 2) == 4));
                    if (k) g[i][j][k][p] = max(g[i][j][k][p], g[i][j][k - 1][(p + 3) % 4] + ((p + 3) == 4));
                }
    int PPP = 0;
    scanf("%d", &T);
    while (T --)
    {
        PPP ++;
        scanf("%d%d", &n, &p);
        int x[4] = {0}, ans = 0, sum = 0;
        for (int i = 1; i <= n; ++ i)
        {
            int a;
            scanf("%d", &a);
            sum = (sum + a) % p;
            x[a % p] ++;
        }
        cout << "Case #" << PPP << ": ";
        if (p == 2) ans = x[0] + x[1] / 2;
        else if (p == 3) ans = x[0] + f[x[1]][x[2]][0];
        else ans = x[0] + g[x[1]][x[2]][x[3]][0];
        cout << ans + (sum != 0) << endl;
    }
}
