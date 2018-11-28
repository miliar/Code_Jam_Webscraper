/* Copyright 2017 Rafael Rendón Pablo <rafaelrendonpablo@gmail.com> */
// region Template
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long           int64;
typedef unsigned long long  uint64;
const int kMax      = 1005;
// endregion

double dp[kMax][kMax];
bool defined[kMax][kMax];

double area(double r) {
    return M_PI * r * r;
}

double bandarea(double r, double h) {
    return h * 2 * M_PI * r;
}

double f(int p, int k, const vector<pair<double, double>>& P) {
    if (k == 0) {
        return area(P[p].first);
    }
    double& ans = dp[p][k];
    if (defined[p][k]) {
        return ans;
    }
    defined[p][k] = true;
    ans = 0;
    for (int i = 0; i < int(P.size()); i++) {
        double r = P[i].first;
        double h = P[i].second;
        if (i == p) {
            continue;
        }
        if (r <= P[p].first) {
            double s = area(P[p].first) - area(r) + bandarea(r, h);
            ans = std::max(ans, s + f(i, k - 1, P));
        }
    }
    return ans;
}

double solve(vector<pair<double, double>>& P, int K) {
    double ans = -1e12;
    for (int i = 0; i < int(P.size()); i++) {
        ans = std::max(ans, f(i, K - 1, P) + bandarea(P[i].first, P[i].second));
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    cout << std::fixed << std::setprecision(10);
    for (int tc = 1; tc <= T; tc++) {
        int N, K;
        cin >> N >> K;
        vector<pair<double, double>> P(N);
        for (auto& p : P) {
            cin >> p.first >> p.second;
        }
        memset(defined, false, sizeof defined);
        cout << "Case #" << tc << ": " << solve(P, K) << "\n";
    }

    return EXIT_SUCCESS;
}
