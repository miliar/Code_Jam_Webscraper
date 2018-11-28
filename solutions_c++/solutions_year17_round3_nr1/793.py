#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int t;
const long double mPi = 3.14159265359;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    cout.precision(16);

    cin >> t;
    for (int step = 1; step <= t; step++)
    {
        int n, k;
        long double ans = 0;
        vector <pair <long double, long double> > v;
        vector <vector <long double> > dp;

        cin >> n >> k;
        v.resize(n);
        dp.resize(n, vector <long double>(k, 0));
        for (int i = 0; i < n; i++)
            cin >> v[i].first >> v[i].second;

        sort(v.begin(), v.end());

        for (int j = 0; j < k; j++)
        {
            for (int i = n - 1; i >= 0; i--)
            {
                if (j == 0)
                    dp[i][j] = mPi * 2 * v[i].first * v[i].second + mPi * v[i].first * v[i].first;
                else
                {
                    dp[i][j] = dp[i][j - 1];
                    for (int k = i + 1; k < n; k++)
                        dp[i][j] = max(dp[i][j], dp[k][j - 1] + mPi * 2 * v[i].first * v[i].second);
                }
            }
        }

        for (int i = 0; i < n; i++)
            ans = max(ans, dp[i][k - 1]);

        cout << "Case #" << step << ": ";
        cout << ans << endl;
    }
    return 0;
}
