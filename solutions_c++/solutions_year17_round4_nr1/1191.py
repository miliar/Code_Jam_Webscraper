#include <bits/stdc++.h>
using namespace std;

#define all(x) begin(x), end(x)
#define task "A-large"

typedef long long ll;
typedef long double ld;

const int N = 105;

int dp[N][N][N];
void relax(int &x, int new_val) {
    x = max(x, new_val);
}

void solve() {
    int n, p;
    cin >> n >> p;
    vector<int> os(4);
    vector<int> g(n);
    memset(dp, 0, sizeof(dp));

    for (int i = 0; i < n; i++) {
        cin >> g[i];
        os[g[i] % p]++;
    }

    dp[0][0][0] = os[0];
    for (int i = 0; i <= os[1]; i++) {
        for (int j = 0; j <= os[2]; j++) {
            for (int k = 0; k <= os[3]; k++) {
                int o = (i * 1 + j * 2 + k * 3) % p;
                int new_val = dp[i][j][k] + (int)(o == 0);
                relax(dp[i + 1][j][k], new_val);
                relax(dp[i][j + 1][k], new_val);
                relax(dp[i][j][k + 1], new_val);
            }
        }
    }
    cout << dp[os[1]][os[2]][os[3]] << endl;
}

int main() {
    #ifdef ShapeOfYou
        freopen(task".in", "r", stdin);
        freopen(task".out", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << + i << ": ";
        solve();
    }
    return 0;
}
