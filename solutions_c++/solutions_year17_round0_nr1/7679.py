#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int ans = 0;
        string s;
        int k;
        cin >> s >> k;

        for (int i = 0; i <= s.size() - k; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = 0; j < k; j++)
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
            }
        }

        int ok = true;
        for (int i = 0; i < s.size(); i++)
            if (s[i] == '-')
                ok = false;

        if (ok)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }
    return 0;
}
