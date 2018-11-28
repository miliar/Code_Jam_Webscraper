#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, k, cases = 1;
    string s;
    cin >> t;
    while (t--) {
        cin >>s >> k;
        int ans = 0;
        for (int i = 0; i <= s.size() - k; i++) {
            if (s[i] == '-') {
                ans ++;
                for (int j = 0;j < k;j++) {
                    s[i + j] = (s[i + j] == '+' ? '-' : '+');
                }
            }
        }
        for (int i = s.size() - k; i < s.size(); i++) {
            if (s[i] == '-') {
                ans = -1;
                break;
            }
        }
        if (ans == -1) {
            cout << "Case #" << cases++ <<": IMPOSSIBLE\n";
        }
        else cout << "Case #" << cases++ << ": " << ans << '\n';


    }
    return 0;
}
