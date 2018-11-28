#include <bits/stdc++.h>
using namespace std;

int t, n, m;
long double dp[200], e[200], s[200], d[200], inf = 1e15;

int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        cin >> n >> m;
        for(int i = 1; i <= n; ++i)
        {
            cin >> e[i] >> s[i];
        }
        for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
        {
            int dd;
            cin >> dd;
            if(dd != -1)
            {
                d[i+1] = dd;
                //cout << dd << endl;
                d[i+1] += d[i];
            }

        }
        /*for(int i = 1; i <= n; ++i)
            cout << d[i] << ' ';
        cout << endl;
        */
        int ss, ff;
        cin >> ss >> ff;
        dp[ss] = 0.;
        for(int i = 2; i <= n; ++i)
        {
            dp[i] = inf;
            for(int j = i-1; j >= 1; --j)
            {
                if(d[i] - d[j] <= e[j])
                {
                    long double t1 = dp[j]+(d[i]-d[j])/s[j];
                    dp[i] = min(dp[i], t1);
                }
            }
        }
        cout << "Case #" << q+1 << ": ";
        cout << fixed << setprecision(8) << dp[n] << "\n";
        for(int i = 1; i <= n; ++i)
            d[i] = 0.;
    }
}
