#include <bits/stdc++.h>
using namespace std;
const int MAXN = 33;
int n, m;
char a[MAXN][MAXN];
int main()
{
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T ; cas++)
    {
        cout << "Case #" << cas << ":\n";
        string str;
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        bool nolastline = true;
        for (int i = 0; i < n; i++)
        {
            bool nothing = true;
            char last;
            for (int j = 0; j < m; j++)
                if (a[i][j] != '?')
                    nothing = false, last = a[i][j];
                else if (!nothing)
                    a[i][j] = last;
            nothing = true;
            for (int j = m - 1; j >= 0; j--)
                if (a[i][j] != '?')
                    nothing = false, last = a[i][j];
                else if (!nothing)
                    a[i][j] = last;
            if (!nothing)
            {
                nolastline = false;
                continue;
            }
            if (!nolastline)
                for (int j = 0; j < m; j++)
                    a[i][j] = a[i - 1][j];
        }

        nolastline = true;
        for (int i = n - 1; i >= 0; i--)
        {
            bool nothing = true;
            char last;
            for (int j = 0; j < m; j++)
                if (a[i][j] != '?')
                    nothing = false, last = a[i][j];
                else if (!nothing)
                    a[i][j] = last;
            nothing = true;
            for (int j = m - 1; j >= 0; j--)
                if (a[i][j] != '?')
                    nothing = false, last = a[i][j];
                else if (!nothing)
                    a[i][j] = last;
            if (!nothing)
            {
                nolastline = false;
                continue;
            }
            if (!nolastline)
                for (int j = 0; j < m; j++)
                    a[i][j] = a[i + 1][j];
        }
        for (int i = 0; i < n; i++)
            cout << a[i] << endl;
    }
    return 0;
}
