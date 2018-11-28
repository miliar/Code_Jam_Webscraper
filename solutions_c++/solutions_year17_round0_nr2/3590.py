#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string s;

bool good(string f) {
    if (f[0] == '0') return false;
    for(int i = 1; i < (int)f.length(); ++i)
        if (f[i] < f[i - 1]) return false;
    return true;
}

void solve() {
    cin >> s;
    int n = (int)s.length();
    if (good(s)) {
        cout << s << '\n';
        return;
    }
    for(int i = 1; i < n; ++i)
        if (s[i] < s[i - 1]) {
            for(int k = i - 1; k >= 0; --k) {
                string f = "";
                for(int j = 0; j < k; ++j)
                    f += s[j];
                f += char(s[k] - 1);
                for(int j = k + 1; j < n; ++j)
                    f += '9';
                if (good(f)) {
                    cout << f << '\n';
                    return;
                }
            }
            for(int j = 0; j < n - 1; ++j)
                cout << '9';
            cout << '\n';
            return;
        }
}

int main() {
    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        solve();
    }
    return 0;
}