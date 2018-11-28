#include <bits/stdc++.h>

using namespace std;

bool prefixOk(int l, string s) {
    for (int i = 1; i <= l; ++i)
        if (s[i] < s[i-1])
            return false;
    return true;
}

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        cout << "Case #" << ti << ": ";
        string s;
        cin >> s;

        int l = s.length();

        if (prefixOk(l-1, s)) {
            cout << s << "\n";
        }
        else {
            bool fnd = false;
            for (int i = l-3; i >= 0; --i) {
                if (prefixOk(i, s) && s[i]+1 <= s[i+1]) {
                    cout << s.substr(0, i+1) << char(s[i+1]-1);
                    for (int j = i+2; j < l; ++j)
                        cout << 9;
                    cout << "\n";
                    fnd = true;
                    break;
                }
            }
            if (!fnd && s[0] > 49) {
                cout << char(s[0]-1);
                for (int i = 1; i < l; ++i)
                    cout << 9;
                cout << "\n";
            }
            else if (!fnd) {
                for (int i = 1; i < l; ++i)
                    cout << 9;
                cout << "\n";
            }
        }
    }
    return 0;
}
