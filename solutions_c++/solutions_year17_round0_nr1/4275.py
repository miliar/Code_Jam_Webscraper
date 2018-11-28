#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        string s;
        int c = 0, n;
        cin >> s >> n;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '-') {
                if (s.length() - i < n) {
                    c = -1;
                    break;
                } else {
                    ++c;
                    for (int j = i; j < i + n; ++j) {
                        s[j] = ((s[j] == '-') ? '+' : '-');
                    }
                }
            }
        }
        if (c >= 0) {
            cout << c << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
}
