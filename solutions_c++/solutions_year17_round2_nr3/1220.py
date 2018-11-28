#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define MOD (1000000000000007LL)
#define LL long long

#define sqr(x) ((x) * (x))
#define Nmax 200333

inline void test_out() {
    static int test_id = 0;
    test_id ++;
    cout << "Case #" << test_id << ": ";
}

int n,q;
int e[Nmax], s[Nmax];
int main() {
    ios_base::sync_with_stdio(0);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("answer.txt", "w", stdout);

    int test_number;
    cin >> test_number;
    while (test_number --> 0) {
        cin >> n >> q;
        assert(q == 1);
        for (int i = 1; i <= n; i ++) {
            cin >> e[i] >> s[i];
        }
        vector<double> dist(1, 0);
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= n; j ++) {
                int x;
                cin >> x;
                if (x != -1) {
                    dist.push_back(x);
                }
            }
        }
        assert(dist.size() == n);
        int u, v;
        cin >> u >> v;
        assert(u == 1);
        assert(v == n);

        vector< double > dp(n + 1, 0.0);
        for (int i = n - 1; i >= 1; i --) {
            assert(dist[i] <= e[i]);
            dp[i] = dp[i + 1] + (dist[i] * 1.0 / s[i]);
            double temp = 0.0;
            for (int j = i + 1; j <= n; j ++) {
                temp += dist[j - 1];
                if (temp > e[i]) break;
                dp[i] = min(dp[i], dp[j] + (temp * 1.0 / s[i]));
            }
        }
        test_out();
        cout.precision(9);
        cout << fixed << dp[1] << endl;
    }
    return 0;
}
