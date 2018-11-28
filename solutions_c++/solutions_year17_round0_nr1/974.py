#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string R;
        int K;
        cin >> R >> K;
        string S(R);
        int cnt = 0, l = S.length(), ans = 0;
        for (int dir = 0; dir < 2; ++dir) {
            for (int i = 0; i + K <= l; ++i) {
                if (S[i] == '-') {
                    ++cnt;
                    for (int j = i; j < i + K; ++j) {
                        S[j] = S[j] == '-' ? '+' : '-';
                    }
                }
            }
            for (int i = l - K; i < l; ++i) {
                if (S[i] == '-') {
                    cnt = -1;
                    break;
                }
            }
            if (dir) {
                if (cnt >= 0 && ans >= 0) ans = min(cnt, ans);
                else if (cnt >= 0) ans = cnt;
            } else {
                ans = cnt;
                cnt = 0;
                S = R;
                reverse(S.begin(), S.end());
            }
        }
        if (ans >= 0) cout << "Case #" << t << ": " << ans << "\n";
        else cout << "Case #" << t << ": IMPOSSIBLE\n";
    }
    return 0;
}
