#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        string s;
        int K;
        cin >> s >> K;
        int cnt = 0;
        for (int i = 0; i + K <= s.size(); i++) {
            if (s[i] == '-') {
                cnt++;
                for (int j = i; j < i + K; j++) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }
        }
        bool valid = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                valid = false;
            }
        }
        if (valid) {
            cerr << cnt << endl;
            printf("Case #%d: %d\n", cas, cnt);
        } else {
            cerr << "IMPOSSIBLE" << endl;
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
    }
    return 0;
}
