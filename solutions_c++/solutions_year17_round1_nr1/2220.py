#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
using namespace std;

int t, n, m, dp[50][50][1000], k[1000];
char c[50][50];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        cin >> n >> m;
        for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        {
            cin >> c[i][j];
            k[c[i][j]]++;
            for(char cc = 'A'; cc <= 'Z'; ++cc)
            {
                dp[i][j][cc] = dp[i-1][j][cc] + dp[i][j-1][cc] - dp[i-1][j-1][cc];
                if(c[i][j] == cc) dp[i][j][cc]++;
            }
        }

        for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        for(int ii = n; ii >= i; --ii)
        for(int jj = m; jj >= j; --jj)
        {
            bool flag = true;
            char otv = '?';
            for(char cc = 'A'; cc <= 'Z'; ++cc)
            {
                int kol = dp[ii][jj][cc] - dp[i-1][jj][cc] - dp[ii][j-1][cc] + dp[i-1][j-1][cc];
                if(kol == k[cc] && k[cc] > 0)
                {
                    //cout << i << ' ' << j << ' ' << ii << ' ' << jj << ' ' << cc << endl;
                    if(otv == '?') otv = cc;
                    else
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if(flag == true && otv != '?')
            {
                bool ff = true;
                for(int i1 = i; i1 <= ii; ++i1)
                for(int j1 = j; j1 <= jj; ++j1)
                    if(c[i1][j1] != '?' && c[i1][j1] != otv)
                    {
                        ff = false;
                        break;
                    }
                if(ff == true)
                {
                    for(int i1 = i; i1 <= ii; ++i1)
                    for(int j1 = j; j1 <= jj; ++j1)
                        c[i1][j1] = otv;
                    k[otv]++;
                }
            }
        }

        cout << "Case #" << q+1 << ":\n";
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= m; ++j)
                cout << c[i][j];
            cout << "\n";
        }

        for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        for(char cc = 'A'; cc <= 'Z'; ++cc)
            dp[i][j][cc] = 0;

        for(char cc = 'A'; cc <= 'Z'; ++cc)
            k[cc] = 0;
    }
}
