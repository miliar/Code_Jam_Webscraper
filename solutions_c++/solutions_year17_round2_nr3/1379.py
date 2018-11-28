#include <bits/stdc++.h>
using namespace std;
typedef std::pair<int, int> ii;
typedef long long ll;

void preprocess() {
}

void process_testcase(const int testcase, const int should_run) {
    int n, q;
    cin>>n>>q;
    ll e[n], s[n];
    for (int i = 0; i < n; ++i)
        cin>>e[i]>>s[i];
    ll dist[n][n];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin>>dist[i][j];
    long double from_start[n];
    from_start[0] = 0;
    for (int i = 1; i < n; ++i)
        from_start[i] = from_start[i-1] + dist[i-1][i];

    if (should_run) {
        printf("Case #%d:", testcase);
        while (q--) {
            int u, v;
            cin>>u>>v;
            --u; --v;
            long double dp[n];
            for (int i = 0; i < n; ++i)
                dp[i] = 1e18;
            dp[0] = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = i+1; j < n; ++j) {
                    long double dist = from_start[j] - from_start[i];
                    if (dist <= e[i]) {
                        long double time = dist / s[i];
                        dp[j] = min(dp[j], dp[i] + time);
                    }
                }
            }
            long double ans = dp[n-1];
            cout<<' '<<fixed<<setprecision(9)<<ans;
        }
        puts("");
    } else {
        while (q--) {
            int u, v;
            cin>>u>>v;
        }
    }
}
