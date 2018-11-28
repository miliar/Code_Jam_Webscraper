#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <cassert>

using namespace std;

#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long i64;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    i64 tests;
    cin >> tests;
    for (i64 test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        vector<vector<i64> > d;
        vector<pair<i64, i64> > es;
        vector<pair<i64, i64> > se;

        i64 n, q;
        cin >> n >> q;

        es.resize(n);
        d.resize(n, vector<i64>(n));

        for (i64 i = 0; i < n; i++) {
            cin >> es[i].first >> es[i].second;
        }

        for (i64 i = 0; i < n; i++) {
            for (i64 j = 0; j < n; j++) {
                cin >> d[i][j];
            }
        }

        se.resize(q);

        for (i64 i = 0; i < q; i++) {
            cin >> se[i].first >> se[i].second;
        }

        vector<i64> x(n);

        for (i64 i = 1; i < n; i++) {
            x[i] = x[i - 1] + d[i - 1][i];
        }

        vector<long double> dp(n, 1e18);
        dp[0] = 0;
        for (i64 i = 1; i < n; i++) {
            for (i64 j = 0; j < i; j++) {
                if (x[i] - x[j] <= es[j].first) {
                    dp[i] = min(dp[i], dp[j] + 1.0 * (x[i] - x[j]) / es[j].second);
                }
            }
        }

        for (i64 i = 0; i < n; i++) {
            cerr << dp[i] << " ";
        }
        cerr << endl;


        cout << fixed << setprecision(22) << dp[n - 1] << endl;
    }
}