#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

void solve(int t) {

    int n,k;
    cin>>n>>k;

    cout<<"Case #"<<t<<": ";

    vector<pair<double, double> >a(n+1, make_pair(0, 0));
    for(int i = 1; i <= n; i++) {
        cin>>a[i].first>>a[i].second;
    }

    sort(a.begin(), a.end());
    vector<vector<double> >dp(n+1, vector<double>(k+1, 0.0000000));
    for(int i=1; i<n; i++) {
        dp[i][0] = 0;
        for(int j=1; j<k; j++) {
            dp[i][j] = dp[i-1][j];
            dp[i][j] = max(dp[i-1][j-1] + 2*a[i].first*(double)a[i].second, dp[i][j]);
        }
    }

    double ans = 0;
    for(int i=1; i<=n; i++) {
        if (ans < dp[i-1][k-1]+a[i].first*a[i].second*2 + a[i].first*a[i].first) {
            ans = dp[i-1][k-1]+a[i].first*a[i].second*2 + a[i].first*a[i].first;
        }
    }


    printf("%.10lf\n", ans*M_PI);

}


int main() {

    freopen("A-large (3).in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}