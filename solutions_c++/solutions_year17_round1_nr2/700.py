#include <bits/stdc++.h>

using namespace std;

#define ll long long

int TEST;

void solve() {
    int n, p;
    cin >> n >> p;

    vector<int> need(n), L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> need[i];
        L[i] = need[i] * 9;
        R[i] = need[i] * 11;
        need[i] *= 10;
    }

    vector<vector<ll>> ing(n, vector<ll>(p));
    vector<map<pair<ll, ll>, ll>> have(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            cin >> ing[i][j];
            ll p = ing[i][j] * 10;
            ll right = (p) / L[i];
            ll left = p / R[i];

            if (!(left * L[i] <= p && p <= left * R[i])) {
                ++left;
            }
            if (!(right * L[i] <= p && p <= right * R[i])) {
                --right;
            }

            left = max(1LL, left);

            if (left <= right) {
                ++have[i][{left, right}];
            }
        }
    }

    // for (auto it : have) {
    //     for (auto tt : it) {
    //         cout << '(' << tt.first.first << ' ' << tt.first.second << ' ' << tt.second << ')' << ' ';
    //     }
    //     cout << endl;
    // }

    ll res = 0;
    while (true) {
        bool good = 1;
        for (int i = 0; i < n; ++i) {
            if (have[i].empty()) {
                good = 0;
                break;
            }
        }

        if (!good) {
            break;
        }

        ll cur_c = have[0].begin()->second;
        pair<ll, ll> cur_cnt = have[0].begin()->first;
        
        for (int i = 1; i < n; ++i) {
            cur_cnt.first = max(cur_cnt.first, have[i].begin()->first.first);
            cur_cnt.second = min(cur_cnt.second, have[i].begin()->first.second);
            cur_c = min(cur_c, have[i].begin()->second);
        }

        // cout << cur_cnt.first << ' ' << cur_cnt.second << ' ' << cur_c << endl;

        if (cur_cnt.first > cur_cnt.second || cur_c == 0) {
            cur_cnt = have[0].begin()->first;
            for (int i = 0; i < n; ++i) {
                if (have[i].begin()->first.first != cur_cnt.first) {
                    if (have[i].begin()->first.first < cur_cnt.first) {
                        cur_cnt = have[i].begin()->first;
                    }
                } else if (have[i].begin()->first.second < cur_cnt.second) {
                    cur_cnt = have[i].begin()->first;
                }
            }
            for (int i = 0; i < n; ++i) {
                if (have[i].begin()->first == cur_cnt) {
                    have[i].erase(have[i].begin());
                }
            }
        } else {
            res += cur_c;
            for (int i = 0; i < n; ++i) {
                have[i].begin()->second -= cur_c;
                if (have[i].begin()->second == 0) {
                    have[i].erase(have[i].begin());
                }
            }
        }
    }

    printf("Case #%d: ", TEST);
    cout << res << '\n';
}

int main() {
    int t;
    cin >> t;

    for (TEST = 1; TEST <= t; ++TEST) {
        solve();
    }

    return 0;
}
