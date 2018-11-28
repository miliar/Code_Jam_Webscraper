#include <bits/stdc++.h>
using namespace std;

#define MAX 1001
#define MOD 12345

int a[MAX];

main() {
    #ifdef LOCAL_BUILD
        freopen("2.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios::sync_with_stdio(0);

    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        string s;
        int n, m;
        cin >> s >> n;
        m = s.size();

        for (int i = 0; i < m; ++i)
            a[i] = (s[i] == '+');

        int ans = 0, valid = 1;
        for (int i = 0; i < m; ++i) {
            if (!a[i]) {
                if (i+n > m) {
                    valid = 0;
                    break;
                }
                for (int j = i; j < i+n; ++j) {
                    a[j] = 1-a[j];
                }
                ++ans;
            }
        }
        if (valid) {
            printf("Case #%d: %d\n", c, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
    }

    return 0;
}
