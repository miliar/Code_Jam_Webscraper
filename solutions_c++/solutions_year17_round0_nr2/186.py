#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

typedef long long i64;

bool isTidy(int64_t n) {
    int last = 9;
    while (n > 0) {
        if (n % 10 > last) {
            return false;
        }
        last = n % 10;
        n /= 10;
    }
    return true;
}

void solve() {
    int64_t n;
    cin >> n;
    int64_t m = n;
    int64_t res = 0;
    if (n < 10) {
        res = n;
    } else {
        vector<int> digs;
        while (n > 0) {
            digs.push_back(n % 10);
            n /= 10;
        }
        int k = SZ(digs);
        reverse(digs.begin(), digs.end());
        int pos = -1;
        for (int i = 0; i < k - 1; ++i) {
            if (digs[i] > digs[i + 1]) {
                pos = i;
                break;
            }
        }
        if (pos == -1) {
            for (int i = 0; i < k; ++i) {
                res = 10 * res + digs[i];
            }
        } else {
            while (pos > 0 && digs[pos - 1] == digs[pos]) {
                --pos;
            }
            for (int i = 0; i < pos; ++i) {
                res = 10 * res + digs[i];
            }
            res = 10 * res + digs[pos] - 1;
            for (int i = pos + 1; i < k; ++i) {
                res = 10 * res + 9;
            }
        }
    }
    // assert(isTidy(res));
    // for (int i = res + 1; i <= m; ++i) {
    //     assert(!isTidy(i));
    // }
    cout << res << '\n';
}

int main() {
    #ifdef LOCAL_RUN
    freopen("task.in", "r", stdin);
    freopen("task.out", "w", stdout);
    //freopen("task.err", "w", stderr);
    #endif // ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
