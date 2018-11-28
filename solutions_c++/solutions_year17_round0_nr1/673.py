#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int tc = 1;

    while (t--) {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;
        for (int i = 0; i < s.size() - k + 1; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = 0; j < k; j++) {
                    s[j + i] = (s[j + i] == '-') ? '+' : '-';
                }
            }
        }

        bool pos = true;
        for (char c : s) {
            if (c != '+') {
                pos = false;
                break;
            }
        }

        printf("Case #%d: ", tc++);
        if (pos) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}
