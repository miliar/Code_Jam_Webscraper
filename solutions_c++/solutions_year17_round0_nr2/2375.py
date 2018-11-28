#include <iostream>
#include <cstring>
#include <sstream>
#include <string>

using namespace std;

long long cnt(long long x) {
    ostringstream ssout; ssout << x;
    string s = ssout.str();

    long long dp[2][10][2] = {};
    int cur = 1, prv = 0;

    dp[prv][0][1] = 1;

    for (int i = 0; i < int(s.size()); ++i) {
        memset(dp[cur], 0, sizeof dp[cur]);

        for (int prvput = 0; prvput <= 9; ++prvput) {
            for (int put = prvput; put <= 9; ++put)
                dp[cur][put][0] += dp[prv][prvput][0];
            for (int put = prvput; put < s[i] - '0'; ++put)
                dp[cur][put][0] += dp[prv][prvput][1];
            if (s[i] - '0' >= prvput)
                dp[cur][s[i] - '0'][1] += dp[prv][prvput][1];
        }

        swap(cur, prv);
    }

    long long ans = 0;
    for (int put = 0; put <= 9; ++put)
        ans += dp[prv][put][0] + dp[prv][put][1];
    return ans - 1;
}

void solve(int e) {
    cout << "Case #" << e << ": ";

    long long mn = 0;
    long long mx; cin >> mx;

    long long total = cnt(mx);

    while (mn < mx) {
        long long md = (mn + mx) / 2;

        long long cur = cnt(md);

        if (total - cur == 0) {
            mx = md;
        } else {
            mn = md + 1;
        }
    }

    cout << mn << endl;
}

int main() {
    int t; cin >> t;
    for (int e = 1; e <= t; ++e)
        solve(e);
}
