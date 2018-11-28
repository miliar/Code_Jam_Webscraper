#include <bits/stdc++.h>
using namespace std;

// IOI 2018

int t;
string s;

bool ok(string a, string b) {
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] > b[i]) return 0;
        if (a[i] < b[i]) return 1;
    }
    return 1;
}

int main() {
    freopen("B_in.txt", "r", stdin);
    freopen("B_out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        cin >> s;
        string res;
        for (int i = 0; i < s.size(); ++i) {
            string tmp = res;
            for (int j = i; j < s.size(); ++j) tmp.push_back(s[i]);
            if (ok(tmp, s)) {
                res.push_back(s[i]);
            }
            else {
                res.push_back(s[i] - 1);
                for (int j = i + 1; j < s.size(); ++j) res.push_back('9');
                break;
            }
        }
        if (res[0] == '0' && s != "1") res.erase(0, 1);
        cout << "Case #" << T << ": " << res << '\n';
    }
}
