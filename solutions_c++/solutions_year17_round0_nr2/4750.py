#include <bits/stdc++.h>

using namespace std;

string solve(string s) {
    string mx = string(s.length(), '0');
    auto tryUpdate = [&] (string c) {
        char prev = '0';
        bool ok = true;
        for (char ch : c) {
            if (ch < prev) {
                ok = false;
            }
            prev = ch;
        }
        if (ok && c > mx) {
            mx = c;
        }
    };

    tryUpdate(s);
    for (int i = 0; i < s.length(); i++) {
        string cur = s;
        if (cur[i] > '0') {
            cur[i]--;
            for (int j = i+1; j < cur.length(); j++) {
                cur[j] = '9';
            }
            tryUpdate(cur);
        }
    }
    if (mx[0] == '0') {
        mx = mx.substr(1);
    }
    return mx;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string str;
        cin >> str;
        cout << "Case #" << i << ": " << solve(str) << endl;
    }
}
