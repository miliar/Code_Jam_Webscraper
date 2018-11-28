#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e3 + 10, INF = 2e18;

int n, q, st, fn;

double t[N][N], len[N], speed[N], dp[N];

void sol(int cs) {
    cin >> n >> q;
    memset(t, 0, sizeof(t));
    for(int i = 1; i <= n; i++) {
        cin >> len[i] >> speed[i];
    }
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            int a;
            cin >> a;
            t[i][j] = a;
            if(t[i][j] == -1) t[i][j] = INF;
        }
    }
    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                if(t[i][k] + t[k][j] < t[i][j]) {
                    t[i][j] = t[i][k] + t[k][j];
                }
            }
        }
    }
    memset(dp, 100, sizeof(dp));
    dp[1] = 0;
    cin >> st >> fn;
    for(int i = 1; i <= n; i++) {
        for(int j = i + 1; j <= n; j++) {
            if(t[i][j] <= len[i] && dp[j] > dp[i] + t[i][j] / speed[i]) {
                dp[j] = dp[i] + t[i][j] / speed[i];
            }
        }
    }
    printf("%.10f", dp[n]);
}

main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        sol(i);
        cout << endl;
    }
}

