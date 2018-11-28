#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    freopen("a.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum) {
        char s[1010];
        int k;
        cin >> s >> k;
        int ans = 0, len = strlen(s);
        for (int i = 0; i < len - k + 1; i++) {
          if (s[i] == '+') continue;
          for (int j = i; j < i + k; j++)
            s[j] = ((s[j] == '+') ? '-' : '+');
          ans++;
        }
        for (int i = len - 1; i >= len - k + 1; i--) {
          if (s[i] == '-') {
            ans = -1;
            break;
          }
        }
        cout << "Case #" << tnum << ": ";
        if (ans != -1) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
