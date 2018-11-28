#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>

using namespace std;
typedef long long li;
typedef pair <li, li> pi;
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)

const string impossible = "IMPOSSIBLE";


int dp[5][100][100][100];

int rec(int p, int one, int two, int tre) {
    if (p < 0 || one < 0 || two < 0 || tre < 0) {
        return -1;
    }
    int& res = dp[p][one][two][tre];
    if (res != -1) {
        return res;
    }

    res = 0;

    if (one) {
        int rem = (one - 1 + two * 2 + tre * 3) % p;
        int ok = (rem == 0) ? 1 : 0;
        res = max(res, rec(p, one - 1, two, tre) + ok);
    }
    if (two) {
        int rem = (one + (two - 1) * 2 + tre * 3) % p;
        int ok = (rem == 0) ? 1 : 0;
        res = max(res, rec(p, one, two - 1, tre) + ok);
    }
    if (tre) {
        int rem = (one + two * 2 + (tre - 1) * 3) % p;
        int ok = (rem == 0) ? 1 : 0;
        res = max(res, rec(p, one, two, tre - 1) + ok);
    }
    return res;
}

void solve() {
    int n, p;
    cin >> n >> p;

    int cnt[4] = {};
    rep(i, n) {
        int x;
        cin >> x;
        cnt[x % p]++;
    }

    int res = rec(p, cnt[1], cnt[2], cnt[3]) + cnt[0];

    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    memset(dp, -1, sizeof dp);
    rep(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
