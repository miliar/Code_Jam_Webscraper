#include<bits/stdc++.h>
using namespace std;

int main ()
{
    freopen("/Users/KhalidRamadan/Desktop/input.txt", "r", stdin);
    freopen("/Users/KhalidRamadan/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        int n;
        long double d;
        cin >> d >> n;
        vector< pair<long double, long double> > horses(n);
        for(int i = 0; i < n; i++)
            cin >> horses[i].first >> horses[i].second;
        sort(horses.rbegin(), horses.rend());
        long double time = 0;
        for(int i = 0; i < n; i++)
        {
            long double cc = d - horses[i].first;
            cc = cc / horses[i].second;
            time = max(cc, time);
        }
        cout << "Case #" << T << ": ";
        cout << setprecision(6) << fixed;
        long double ans = d / time;
        cout << ans << endl;
    }
}

