#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll e[107], s[107];
ll mt[107][107];
ll dt[107][107];
double dp[107];

int main(void)
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    ll t, ti, n, q, i, j, k, u, v;
    cin >> t;
    for (ti = 1; ti <= t; ti++) {
        cin >> n >> q;
        for (i = 1; i <= n; i++) cin >> e[i] >> s[i];
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                cin >> mt[i][j];
                if (mt[i][j]==-1) mt[i][j] = 1000000000000000;
            }
        }

        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                for (k = 1; k <= n; k++) {
                    // j to i, i to k
                    if (mt[j][k] >= mt[j][i]+mt[i][k]) {
                        mt[j][k] = mt[j][i]+mt[i][k];
                    }
                }
            }
        }
        cout << "Case #" << ti << ":";
        while (q--) {
            cin >> u >> v;
            for (i = 1; i <= n; i++) dp[i] = 1000000000000;
            queue< pair< ll , double > > q;
            q.push(make_pair(u, 0.0));
            pair< ll , double > a, b;

            while (!q.empty()) {
                a = q.front(); q.pop();
                u = a.first;
                //cout <<  u << ' ' << a.second << ' ' << dp[u]<< endl;
                if (dp[u] > a.second) {
                    //cout << "reached " << u << " with " << a.second << endl;
                    dp[u] = a.second;
                    for (i = 1; i <= n; i++) {
                        if (i==u) continue;
                        if (mt[u][i]<=e[u]) {
                            q.push(make_pair(i, a.second+(double)mt[u][i]/s[u]));
                        }
                    }
                }
            }
            printf(" %.8lf", dp[v]);
        }
        cout << endl;
    }


    return 0;
}
