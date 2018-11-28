#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream cin("A.in");
    ofstream cout("A.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        
        int n, d; cin >> d >> n;
    
        vector<pair<int, int>> v(n);
        
        for(int i = 0; i < n; ++i)
            cin >> v[i].first >> v[i].second;
        
        vector<int> p(n, 0);

        for(int i = 0; i < n; ++i)
            p[i] = i;

        sort(p.begin(), p.end(), [&] (int a, int b) {
            return v[b].first > v[a].first;
        });
    
        vector<double> dp(n, 0);
        
        for(int i = 0; i < n; ++i) {
            dp[i] = (d - v[p[i]].first - 0.0) / v[p[i]].second;
            if(i >= 1)
                dp[i] = max(dp[i], dp[i - 1]);
        }

        double ans = d / dp[n - 1];

        cout.precision(10);
        cout << ans << "\n";

        cerr << t_case << "\n";
    }
}
