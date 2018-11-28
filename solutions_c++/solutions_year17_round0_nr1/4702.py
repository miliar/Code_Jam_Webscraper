#include <bits/stdc++.h>
using namespace std;

int T;
string s;
int k;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for(int kase = 1; kase <= T; kase++) {
        cin >> s >> k;
        int ans = 0;
        //cout << "[check] " << s << endl;
        for(int i = 0; i <= s.length() - k; i++) {
            if (s[i] == '+') continue;
            for(int j = i; j < i + k; j++) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
            ans++;
            //cout << "[check] " << s << endl;
        }
        bool impossible = false;
        for(int i = 0; i < s.length(); i++) {
            if (s[i] == '-') {
                impossible = true;
                break;
            }
        }
        cout << "Case #" << kase << ": ";
        if (impossible) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
}
