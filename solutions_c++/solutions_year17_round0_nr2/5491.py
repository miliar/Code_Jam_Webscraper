#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    cin >> s;
    for (int i = 0; i + 1 < s.size(); ++i) {
        if (s[i] > s[i + 1]) {
            --s[i];
            for (int j = i + 1; j < s.size(); ++j) {
                s[j] = '9';
            }
            i -= 2;
        }
    }
    string ans = "";
    bool fl = false;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] != '0')
            fl = true;
        if (fl)
            ans += s[i];
    }
    cout << ans << endl;
}

void solve_stupid() {
    long long n;
    cin >> n;
    for (long long i = n; i >= 0; --i) {
        bool ok = true;
        string s = to_string(i);
        for (int j = 0; j + 1 < s.size(); ++j) {
            if (s[j] > s[j + 1])
                ok = false;
        }
        if (ok) {
            cout << i << endl;
            return;
        }
    }
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cerr << "Case #" << tt << " is working" << endl;
        cout << "Case #" << tt << ": ";
        solve();
    }

    return 0;
}

