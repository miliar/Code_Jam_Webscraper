#include <bits/stdc++.h>
using namespace std;

#define MAX 1001
#define MOD 12345

main() {
    #ifdef LOCAL_BUILD
        freopen("2.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios::sync_with_stdio(0);

    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        string s;
        int n;
        cin >> s;
        n = s.size();

        int valid = 1;
        for (int i = 1; i < n; ++i)
            if (s[i] < s[i-1])
                valid = 0;

        if (valid) {
            printf("Case #%d: %s\n", t1, s.c_str());
        } else {
            int p = 0;
            for (int i = 1; i < n; ++i) {
                if (s[i] > s[i-1])
                    p = i;
                if (s[i] < s[i-1])
                    break;
            }
            s[p]--;
            for (int i = p+1; i < n; ++i)
                s[i] = '9';

            int c = 0;
            while (s[c] == '0') c++;
            s = s.substr(c, n-c);

            printf("Case #%d: %s\n", t1, s.c_str());
        }
    }

    return 0;
}
