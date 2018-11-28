#include <bits/stdc++.h>

using namespace std;

int solve() {
    int n, p;
    cin >> n >> p;
    vector<int> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
    }
    vector<vector<int> > q(n, vector<int>(p));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            cin >> q[i][j];
        }
        sort(q[i].begin(), q[i].end());
    }

    vector<int> ptr(n, 0);
    for (int i = 0; i < n; ++i) {
        ptr[i] = 0;
        for (int j = 0; j < p; ++j) {
            if (q[i][j] * 100 < r[i] * 90)
                ++ptr[i];
            else
                break;
        }
    }
    int ans = 0;
    vector<int> low(n), high(n);
    while (1) {
        bool check = false;
        for (int i = 0; i < n; ++i) {
            if (ptr[i] == p) {
                check = true;
            }
        }
        if (check) {
            break;
        }
        int x = 0, mn = INT_MAX, mx = -1;
        for (int i = 0; i < n; ++i) {
            low[i] = (100 * q[i][ptr[i]] + 110 * r[i] - 1) / (110 * r[i]);
            high[i] = (100 * q[i][ptr[i]]) / (90 * r[i]);
            if (high[i] < high[x]) {
                x = i;
            }
            mn = min(mn, high[i]);
            mx = max(mx, low[i]);
        }
        if (mn == 0 || mn < mx) {
            ++ptr[x];
        } else {
            ++ans;
            for (int i = 0; i < n; ++i) {
                ++ptr[i];
            }
        }
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cout << "Case #" << test << ": " << solve() << '\n';
        cerr << "Solved case " << test << '\n';
    }
    return 0;
}