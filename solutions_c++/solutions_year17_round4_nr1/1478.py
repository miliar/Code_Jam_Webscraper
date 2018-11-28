#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)

using namespace std;

int g[4];

int solve4() {
    int ans = g[0];
    int count = g[1] + g[2] + g[3];
    
    if (count == 0) return ans;
    int mi = min(g[1], g[3]);
    int ma = max(g[1], g[3]);
    ans += mi;
    ans += g[2] / 2;
    g[2] %= 2;
    ma -= mi;
    if (g[2] == 1) {
        if (ma >= 2) {
            ma -= 2;
            ans += 1;
        } else {
            ma++;
        }
    }
    ans += (ma + 3) / 4;
    return ans;
}

int solve3() {
    if (g[1] == g[2]) {
        return g[0] + g[1];
    } else {
        int mi = min(g[1], g[2]);
        int ma = max(g[1], g[2]);
        return g[0] + mi + (ma - mi + 2) / 3; 
    }
}

int solve2() {
    return g[0] + (g[1] + 1) / 2;
}

void solve() {
    int N, P;
    cin >> N >> P;
    rep(i, 4) g[i] = 0;
    int ans = 0;
    int count = 0;
    rep(i, N) {
        int a;
        cin >> a;
        g[a % P]++;
    }
    if (P == 2) ans = solve2();
    else if (P == 3) ans = solve3();
    else if (P == 4) ans = solve4();
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
