#include<bits/stdc++.h>
using namespace std;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        string s;
        int k, len, ans = 0;
        cin >> s >> k;
        len = (int)s.size();
        for(int i = 0; i + k <= len; i++) {
            if(s[i] == '-') {
                for(int j = i; j < i + k; j++) {
                    s[j] = (s[j] == '+') ? '-' : '+';
                }
                ans++;
            }
        }
        int i;
        for(i = 0; s[i]; i++) if(s[i] == '-') break;
        printf("Case #%d: ", cs);
        if(s[i]) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
