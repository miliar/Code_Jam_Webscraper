#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

int n, q;
ll d[101][101];
ll e[101], s[101];
double dp[101];

void solve()
{
    cin >> n >> q;
    for(int i = 0; i < n; i++) cin >> e[i] >> s[i];
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> d[i][j];
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) if(d[i][j] == -1) d[i][j] = (ll)1e18;
    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                d[i][j] = min (d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    while(q--){
        for(int i = 0; i < n; i++) dp[i] = 1e18;
        int u, to;
        cin >> u >> to;
        u--, to--;
        dp[u] = 0;
        char used[101] = {};
        for(int i = 0; i < n; i++){
            double mn = 1e18;
            int v = -1;
            for(int j = 0; j < n; j++){
                if(!used[j]){
                    if(dp[j] < mn){
                        mn = dp[j];
                        v = j;
                    }
                }
            }
            if(v == -1) break;
            used[v] = true;
            for(int j = 0; j < n; j++){
                ll dist = d[v][j];
                if(dist <= e[v]){
                    dp[j] = min(dp[j], dp[v] + dist / (double)s[v]);
                }
            }
        }
        cout << fixed << setprecision(12) << dp[to] << ' ';
    }
    cout << endl;
}

int main()
{
    freopen("C.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for(int i = 1; i <= test; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
