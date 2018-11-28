#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

const double PI = std::atan(1.0)*4;

double solve1(vector<pair<int, int>> &rh, int k) {
    double res = 0.0;
    int n = rh.size();
    sort(rh.begin(), rh.end());

    vector<vector<double>> dp(n + 1, vector<double>(k, 0.0));

    for (int i = 0; i < n; ++i) {
        dp[i][0] = PI * rh[i - 1].first * rh[i - 1].first + 2 * PI * rh[i - 1].first * rh[i - 1].second;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j < k; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (i < n) {
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2.0 * PI * rh[i - 1].first * rh[i - 1].second);
            }
        }
    }

    return dp[n][k - 1];
}

double solve(vector<pair<int, int>> &rh, int k) {
    double res = 0.0;
    int n = rh.size();
    sort(rh.begin(), rh.end());

    priority_queue<double, std::vector<double>, std::greater<double>> h;
    double curh = 0.0;
    for (int i = 0; i < k - 1; ++i) {
        double cur = 2 * PI * rh[i].first * rh[i].second;
        h.push(cur);
        curh += cur;
    }

    res = curh + PI * rh[k - 1].first * rh[k - 1].first + 2 * PI * rh[k - 1].first * rh[k - 1].second;

    for (int i = k; i < n; ++i) {
        if (!h.empty() && 2 * PI * rh[i - 1].first * rh[i - 1].second > h.top()) {
            curh -= h.top();
            h.pop();
            h.push(2 * PI * rh[i - 1].first * rh[i - 1].second);
            curh += 2 * PI * rh[i - 1].first * rh[i - 1].second;
        }
        res = max(res, curh + PI * rh[i].first * rh[i].first + 2 * PI * rh[i].first * rh[i].second);
    }

    return res;
}

int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    std::cout.precision(10);
    for (int t = 1; t <= T; ++t) {
        int n, k;
        cin >> n >> k;
        vector<pair<int, int>> rh(n, make_pair(0, 0));
        for (int i = 0; i < n; ++i) {
            cin >> rh[i].first >> rh[i].second;
        }
        double res = solve(rh, k);
        cout << "Case #" << t << ": " << std::fixed << res << endl;
    }

    return 0;
}
