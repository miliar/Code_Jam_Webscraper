#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <iomanip>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

const double pi = acos(-1);
const int N = 1017;

long long dp[N][N];

int main() {

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int testN; cin >> testN;

    for (int t = 1; t <= testN; t++) {

        cout << "Case #" << t << ": ";
        int n, k; cin >> n >> k;

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = 0;
            }
        }

        vector <pair <long long, long long> > v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i].first >> v[i].second;
        }

        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());

        for (int i = 0; i < n; i++) {
            dp[1][i] = (long long)v[i].first * v[i].first + (long long)2 * v[i].first * v[i].second;
        }

        for (int i = 2; i <= k; i++) {
            for (int j = 0; j < n; j++) {
                for (int wina = 0; wina < j; wina++) {
                    if (dp[i - 1][wina] != 0) {
                        dp[i][j] = max(dp[i][j], dp[i - 1][wina] + (long long)2 * v[j].first * v[j].second);
                    }
                }
            }
        }

        long long result = 0;
        for (int i = 0; i < n; i++) {
            result = max(result, dp[k][i]);
        }

        cout << fixed << setprecision(10) << result * pi << "\n";
    }

    return 0;
}
