#include <bits/stdc++.h>
using namespace std;
int N, P;
int n[4];
int memo[101][101][101][4];

int opt(int n_1, int n_2, int n_3, int mod) {
    if(memo[n_1][n_2][n_3][mod] == -1) {
        int ans;
        if(n_1 == 0 && n_2 == 0 && n_3 == 0) {
            ans = 0;
        } else {
            ans = 0;
            if(n_1 > 0) {
                ans = max(ans, opt(n_1 - 1, n_2, n_3, (mod + 1) % P));
            }
            if(n_2 > 0) {
                ans = max(ans, opt(n_1, n_2 - 1, n_3, (mod + 2) % P));
            }
            if(n_3 > 0) {
                ans = max(ans, opt(n_1, n_2, n_3 - 1, (mod + 3) % P));
            }
            ans += (mod == 0 ? 1 : 0);
        }
        memo[n_1][n_2][n_3][mod] = ans;
    }
    return memo[n_1][n_2][n_3][mod];
}
int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N >> P;
        memset(n, 0, sizeof n);
        for(int i = 0; i < N; i++) {
            int G;
            cin >> G;
            n[G % P]++;
        }
        memset(memo, -1, sizeof memo);
        int ans = n[0] + opt(n[1], n[2], n[3], 0);
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
