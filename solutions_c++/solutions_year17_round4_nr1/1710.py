#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        vector<int> mods = vector<int>(3, 0);
        int N, P;
        cin >> N >> P;
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            mods[x % P]++;
        }
        int ans = 0;
        ans += mods[0];
        if (P == 2) {
            ans += (mods[1] + 1)/ 2;
        } else if (P == 3) {
            int both = min(mods[1], mods[2]);
            ans += (2 * both + 1) / 2;
            mods[1] -= both;
            mods[2] -= both;
            ans += (mods[1] + 2) / 3;
            ans += (mods[2] + 2) / 3;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
