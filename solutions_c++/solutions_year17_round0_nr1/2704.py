#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);

        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int ans = 0;
        for (int i = 0; i + k <= n; i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j++) s[i + j] ^= '-' ^ '+';
                ans++;
            }
        }
        if (s == string(n, '+')) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
