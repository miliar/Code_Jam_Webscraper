#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;


const int inf = 1e9 + 7;
const long double eps = 1e-7;

void prt(int tt, int l, int ans) {
    cout << "Case #" << tt + 1 << ": " << l << ' ' << ans << endl;
}

vector<int> dt;

int check(int k) {
    int snow = 0;
    for (int i = 0; i < dt.size(); ++i) {
        snow += dt[i];
        if (snow > (i + 1) * k)
            return -1;
    }
    int ans = 0;
    for (auto x : dt)
        ans += max(0, x - k);
    return ans;
}

int main() {
ios_base::sync_with_stdio(0);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, c, m;
        cin >> n >> c >> m;

        dt.assign(n, 0);
        vector<int> ss(c);
        for (int i = 0; i < m; ++i) {
            int p, b;
            cin >> p >> b;
            --p;
            dt[p] ++;
            ss[b - 1] ++;
        }

        int minx = 0;
        for (auto x : ss)
            minx = max(minx, x);

        int l = minx - 1;
        int r = m;

        while (l != r - 1) {
            int m = (l + r) / 2;
            if (check(m) != -1)
                r = m;
            else
                l = m;
        }

        prt(tt, r, check(r));
    }
    return 0;
}