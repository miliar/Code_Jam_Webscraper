#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <algorithm>

using namespace std;

struct Pancake {
    int radius;
    int height;
};

const long double PI = acos(-1.0);

void solve(const int e) {
    cout << "Case #" << e << ": ";

    int n, k; cin >> n >> k;

    Pancake s[1010];
    for (int i=0; i<n; ++i)
        cin >> s[i].radius >> s[i].height;

    sort(s, s+n, [](const Pancake& a, const Pancake& b) { return a.radius > b.radius; });

    long double dp[2][1010] = {};
    int cur = 1;
    int prv = 0;

    for (int i=0; i<n; ++i) {
        memcpy(dp[cur], dp[prv], sizeof dp[cur]);

        for (int prvput=0; prvput<min(k, i+1); ++prvput) {
            long double surface = s[i].height * 2 * PI * s[i].radius;
            if (prvput == 0)
                surface += PI * s[i].radius * s[i].radius;
            dp[cur][prvput + 1] = max(dp[cur][prvput + 1], dp[prv][prvput] + surface);
        }

        swap(cur, prv);
    }

    cout << fixed << setprecision(9) << dp[prv][k] << endl;
}

int main() {
    int t; cin >> t;
    for (int e=1; e<=t; ++e)
        solve(e);
}

