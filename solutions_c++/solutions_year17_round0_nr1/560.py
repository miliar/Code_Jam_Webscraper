#include <bits/stdc++.h>

using namespace std;

void true_main(int testcase) {
    string s;
    int k;
    cin >> s;
    cin >> k;

    int ans = 0;
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == '-') {
            for (int j = 0; j < k; ++j) {
                if (i + j >= s.length()) {
                    cout << "Case #" << testcase << ": IMPOSSIBLE\n";
                    return;
                }
                if (s[i + j] == '-') s[i + j] = '+';
                else s[i + j] = '-';
            }
            ++ans;
        }
    }

    cout << "Case #" << testcase << ": " << ans << "\n";
}

main () {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        true_main(t);
    }
}
