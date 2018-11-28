#include <bits/stdc++.h>
using namespace std;

const int kN = 1e2 + 10;
const int kT = 12 * 60;
pair<int, int> C[kN], J[kN];

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        int ac, aj;
        cin >> ac >> aj;
        for (int i = 0; i < ac; ++i) cin >> C[i].first >> C[i].second;
        for (int i = 0; i < aj; ++i) cin >> J[i].first >> J[i].second;
        sort(C, C + ac);
        sort(J, J + aj);
        int ans = 1000;
        if (ac == 2 || aj == 2) {
            if (aj == 2) C[0] = J[0], C[1] = J[1];
            int tm1 = C[1].second - C[0].first, tm2 = C[0].second + 24 * 60 - C[1].first;
            if (tm1 <= kT || tm2 <= kT) ans = 2;
            else ans = 4;
        } else {
            ans = 2;
        }
        cout << "Case #" << t++ << ": " << ans << "\n";
    }
    return 0;
}
