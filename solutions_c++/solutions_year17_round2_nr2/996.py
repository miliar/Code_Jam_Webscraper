#include <bits/stdc++.h>

using namespace std;

void bad() {
    cout << "IMPOSSIBLE" << endl;
}

void solve(int t) {
    cout << "Case #" << t << ": ";
    int n;
    cin >> n;
    int r, o, y, g, b, v;
    int cnt[3];
    cin >> cnt[0] >> o >> cnt[1] >> g >> cnt[2] >> v;
    if (n == 1) {
        for (int i = 0; i < 3; ++i) {
            if (cnt[i] != 0) {
                if (i == 0) {
                    cout << "R";
                } else if (i == 1) {
                    cout << "Y";
                } else {
                cout << "B";
                }
            }
        }
        cout << endl;
        return;
    }
    if (max(cnt[0], max(cnt[1], cnt[2])) > n / 2) {
        bad();
        return;
    }
    vector<int> s(n, -1);
    int best, mx = 0;
    for (int i = 0; i < 3; ++i) {
        if (mx < cnt[i]) {
            mx = cnt[i];
            best = i;
        }
    }

    vector<int> cur;
    for (int i = 0; i < 3; ++i) {
        if (i != best) {
            cur.push_back(i);
        }
    }

    for (int i = 0; i < n; i += 2) {
        s[i] = best;
        --cnt[best];
        if (cnt[best] == 0) {
            break;
        }
    }
    int ind = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == -1) {
            if (cnt[cur[ind]] == 0) {
                ind = (ind + 1) % 2;
            }
            s[i] = cur[ind];
            --cnt[cur[ind]];
            ind = (ind + 1) % 2;
        }
    }
    for (int i = 1; i < n; ++i) {
        if (s[i] == s[i - 1]) {
            assert(false);
        }
    }
    if (s[0] == s.back()) {
        assert(false);
    }
    for (int i = 0; i < n; ++i) {
        if (s[i] == 0) {
            cout << "R";
        } else if (s[i] == 1) {
            cout << "Y";
        } else {
            cout << "B";
        }
    }
    cout << endl;
}

int main() {
    freopen("B-small-attempt4.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
