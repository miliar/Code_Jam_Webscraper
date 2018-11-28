#include <bits/stdc++.h>
using namespace std;
int T, P, n, m;
const int N = 210;

int L;
int py[N], vx[N], vy[N];
int M[N][N], V[N][N], F[N][N];
int ax[N], ay[N];

int dfs(int t)
{
    vx[t] = 1;
    for (int i = 1; i <= L; ++ i)
        if (!vy[i] && !vx[py[i]] && M[t][i])
        {
            vy[i] = 1;
            if (!py[i] || dfs(py[i]))
            {
                py[i] = t;
                return 1;
            }
        }
    return 0;
}

int main()
{
    cin >> T;
    while (P ++, T --)
    {
        memset(V, 0, sizeof V);
        memset(F, 0, sizeof F);
        cin >> n >> m;
        for (int i = 1; i <= m; ++ i)
        {
            string st; int x, y;
            cin >> st >> x >> y;
            if (st[0] != '+') V[x][y] += 1; // x or o
            if (st[0] != 'x') V[x][y] += 2; // + or o
        }

        memset(ax, 0, sizeof ax);
        memset(ay, 0, sizeof ay);
        for (int i = 1; i <= n; ++ i)
            for (int j = 1; j <= n; ++ j)
                if (V[i][j] & 1)
                {
                    F[i][j] |= 1;
                    ax[i] = 1, ay[j] = 1;
                }

        for (int i = 1, j = 1; i <= n && j <= n; ++ i, ++ j)
        {
            while (ax[i]) i ++;
            while (ay[j]) j ++;
            F[i][j] |= 1;
        }
        /*
        for (int i = 1; i <= n; ++ i)
        {
            for (int j = 1; j <= n; ++ j)
                cout << F[i][j] << " ";
            cout << "\n";
        }
        */
        memset(ax, 0, sizeof ax);
        memset(ay, 0, sizeof ay);
        memset(M, 0, sizeof M);
        for (int i = 1; i <= n; ++ i)
            for (int j = 1; j <= n; ++ j)
            {
                int x = i + j - 1, y = i - j + n;
                if (V[i][j] & 2)
                {
                    ax[x] = ay[y] = 1;
                    F[i][j] |= 2;
                }
                M[x][y] = 1;
            }
        L = n * 2 - 1;
        for (int i = 1; i <= L; ++ i)
            for (int j = 1; j <= L; ++ j)
                if (ax[i] || ay[j])
                    M[i][j] = 0;

                    /*
        for (int i = 1; i <= L; ++ i)
        {
            for (int j = 1; j <= L; ++ j)
                cout << M[i][j] << " ";
            cout << "\n";
        }*/

        memset(py, 0, sizeof py);
        memset(vx, 0, sizeof vx);
        memset(vy, 0, sizeof vy);
        for (int i = 1; i <= L; ++ i)
        {
            for (int j = 1; j <= L; ++ j) vx[j] = vy[j] = 0;
            dfs(i);
        }

        for (int d = 1; d <= L; ++ d)
            if (py[d])
            {
                int x = py[d], y = d;
                int i = (x + y + 1 - n) / 2, j = (x - y + 1 + n) / 2;
                F[i][j] |= 2;
            }

        int ans = 0, cnt = 0;
        for (int i = 1; i <= n; ++ i)
            for (int j = 1; j <= n; ++ j)
            {
                if (F[i][j] == 1 || F[i][j] == 2) ans ++;
                else if (F[i][j] == 3) ans += 2;
                if (F[i][j] == V[i][j]) F[i][j] -= V[i][j];
                if (F[i][j]) cnt ++;
            }

        cout << "Case #" << P << ": " << ans << " " << cnt << "\n";
        for (int i = 1; i <= n; ++ i)
            for (int j = 1; j <= n; ++ j)
                if (F[i][j] == 1) cout << "x" << " " << i << " " << j << "\n";
                else if (F[i][j] == 2) cout << "+" << " " << i << " " << j << "\n";
                else if (F[i][j] == 3) cout << "o" << " " << i << " " << j << "\n";

        /*
        for (int i = 1; i <= n; ++ i)
        {
            for (int j = 1; j <= n; ++ j)
                cout << F[i][j] << " ";
            cout << "\n";
        }
        */

    }
}
