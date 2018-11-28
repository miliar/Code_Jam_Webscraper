#include <bits/stdc++.h>

using namespace std;

int main() {
    int tt;
    scanf("%d", &tt);

    for (int qq = 1; qq <= tt; qq++) {
        printf("Case #%d: ", qq);
        fflush(stdout);
        // solution start

        string s;
        cin >> s;
        for (int t = 0; t < 22; t++) {
            int ix = 0;
            while (ix < (int) s.size() - 1) {
                if (s[ix] > s[ix + 1]) {
                    s[ix]--;
                    for (int i = ix + 1; i < (int) s.size(); i++) {
                        s[i] = '9';
                    }
                }
                ix++;
            }
        }
        string ans = "";
        int ix = 0;
        while (ix < (int) s.size() && s[ix] == '0') ix++;
        while (ix < (int) s.size()) {
            ans += s[ix];
            ix++;
        }
        cout << ans;

        // solution end
        printf("\n");
        fflush(stdout);
    }

    return 0;
}
