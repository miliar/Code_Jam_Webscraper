#include <bits/stdc++.h>
using namespace std;
#define unordered_map map

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int tc; cin >> tc;
    for (int tci = 1; tci <= tc; ++tci) {
        string s; int k; cin >> s >> k;
        int ans = 0;
        for (int i = 0; i <= s.length()-k; ++i) if (s[i] == '-') {
            ++ans;
            for (int j = 0; j < k; ++j) s[i+j] = (s[i+j]=='-'?'+':'-');
        }
        bool flag = true;
        for (int i = 0; i <= s.length(); ++i)
        if (s[i] == '-') {flag = false; break;}
        cout << "Case #" << tci << ": ";
        //cout << s << " ";
        if (flag) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
