#include <bits/stdc++.h>
using namespace std;

double P[55], dp[55][500001];
int N, K;
double solve(int i, int j)
{
    if (i==N) return 1;
    if (fabs(dp[i][j]+1.0) < 1e-8)
    {
        //dp[i][j] = max(dp[i][j], solve(i+1,j-k)*(P[i]+k/10000.0));
    }
    return dp[i][j];
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> K;
        double U; cin >> U;
        map<double,int> mp;
        for (int i = 0; i < N; i++)
        {
            cin >> P[i];
            mp[P[i]]++;
        }

        while (fabs(U)>1e-8)
        {
            if (mp.size() == 1)
            {
                mp[mp.begin()->first + U/mp.begin()->second] = mp.begin()->second;
                U = 0;
            }
            else
            {
                if (U >= (next(mp.begin())->first - mp.begin()->first) * mp.begin()->second)
                {
                    mp[next(mp.begin())->first] += mp.begin()->second;
                    U -= (next(mp.begin())->first - mp.begin()->first) * mp.begin()->second;
                }
                else
                {
                    mp[mp.begin()->first + U/mp.begin()->second] = mp.begin()->second;
                    U = 0;
                }
            }
            mp.erase(mp.begin());
        }

        cout << "Case #" << t << ": ";
        double ans = 1;
        for (auto i : mp)
            ans *= pow(i.first,i.second);
        /*
        for (int i = 0; i < N; i++)
            for (int j = 0; j <= u; j++)
                dp[i][j] = -1;*
        */
        cout << fixed << setprecision(10) << ans << endl;
    }
}
