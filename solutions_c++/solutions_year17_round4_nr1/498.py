#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

unordered_map<i64, int> MEM;

int solve(std::array<int, 4> g, int p, int left) {
    i64 hash = 0;
    for (int i = 0; i < 4; ++i) {
        hash = hash * 101 + g[i];
    }
    hash = hash * p + left;

    if (MEM.count(hash)) {
        return MEM[hash];
    }

    auto& ans = MEM[hash] = 0;
    array<int, 4> to = g;
    for (int i = 0; i < p; ++i) {
        if (to[i] > 0) {
            to[i]--;
            int toans = solve(to, p, (left - i + p) % p);
            ans = max(ans, toans + (left == 0));
            to[i]++;
        }
    }
    return ans;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int __ =1; __ <= T; ++__) {
        int N, P;
        cin >> N >> P;

        std::array<int, 4> g = {0};
        for (int i = 0; i < N; ++i) {
            int x;
            cin >> x;
            g[x % P]++;
        }

        MEM.clear();
        auto ans = solve(g, P, 0);
        cout << "Case #" << __ << ": " << ans << endl;
        cerr << __ << endl;
    }

    return 0;
}
