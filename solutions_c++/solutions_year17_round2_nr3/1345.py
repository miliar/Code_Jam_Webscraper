#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int n;
vector<int> e, s, d;
double dp[110];
double calc(int i) {
    if(dp[i] > -0.5) return dp[i];
    if(i == n - 1) return 0;
    int dd = 0;
    dp[i] = 1e100;
    for(int j = i + 1; j < n; j ++) {
        dd += d[j - 1];
        if(e[i] < dd) break;
        dp[i] = min(dp[i], 1.0 * dd / s[i] + calc(j));
    }
    return dp[i];
}

int main() {
    int T;
    cin >> T;
    forn(t, T) {
        int Q;
        forn(i, 110) dp[i] = -1;
        cin >> n >> Q;
        e.resize(n); s.resize(n); d.resize(n);
        forn(i, n) cin >> e[i] >> s[i];
        forn(i, n) forn(j, n) {
            int x;
            cin >> x;
            if(i + 1 == j) d[i] = x;
        }
        int U, V;
        cin >> U >> V;
        cout << "Case #" << t + 1 << ": " << setprecision(9) << fixed << calc(0) << endl;
    }
}
