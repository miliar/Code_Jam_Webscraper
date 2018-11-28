#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k;
    double u;
    cin >> n >> k;
    cin >> u;
    map<double,int> m;
    for (int i = 0; i < n; i++)
    {
        double x;
        cin >> x;
        m[x]++;
    }
    vector<pair<double,int>> a;
    for (auto p: m)
        a.push_back(p);
    double ans = 1;
    for (int i = 0; i < a.size(); i++)
    {
        if (u < 0) break;
        double d = u / a[i].second;
        if (i == a.size() - 1
                || d < (a[i+1].first - a[i].first))
        {
            ans *= pow(a[i].first + d, a[i].second);
            for (int j = i + 1; j < a.size(); j++)
                ans *= pow(a[j].first, a[j].second);
            break;
        }
        else
        {
            u -= (a[i+1].first - a[i].first) * a[i].second;
            a[i+1].second += a[i].second;
        }
    }
    cout << setprecision(20) << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
