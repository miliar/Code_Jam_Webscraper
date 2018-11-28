//Pranet Verma
#include <bits/stdc++.h>
using namespace std;
int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    int t, tt = 0;
    cin >> t;
    while (t--) {
        cout << "Case #"<< ++tt << ": ";
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i + k - 1 < (int)s.size(); ++i) {
            if (s[i] == '-') {
                ++ans;
                for (int j = i; j < i + k; ++j) {
                    s[j] = '+' + '-' - s[j];
                }
            }
        }
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                ans = 100000;
            }
        }
        if (ans == 100000) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << ans << endl;
        }
    } 
}