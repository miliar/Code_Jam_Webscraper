#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>
#include <functional>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long long llong;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
        cerr << (*i) << " ";
    }
    cerr << "\n";
}

int n, p;
int dp[120][120][120];
int a[120];
int cc[5];

void solve() {
    cin >> n >> p;
    for (int i = 0; i < 5; ++i)
        cc[i] = 0;
    int ss = 0;
    for (int i = 0; i < n; ++i)
        cin >> a[i], a[i] %= p, ss += a[i], cc[a[i]]++;
    ss %= p;
    for (int i = 0; i <= cc[1]; ++i)
        for (int j = 0; j <= cc[2]; ++j)
            for (int k = 0; k <= cc[3]; ++k)
                dp[i][j][k] = 0;
    for (int i = 0; i <= cc[1]; ++i)
        for (int j = 0; j <= cc[2]; ++j)
            for (int k = 0; k <= cc[3]; ++k) {
                int ss = (i + 2 * j + 3 * k) % p;
                if (ss == 0)
                    ss = 1;
                else
                    ss = 0;
                if (i != cc[1])
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + ss);
                if (j != cc[2])
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k] + ss);
                if (k != cc[3])
                    dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + ss);
            }
    cout << dp[cc[1]][cc[2]][cc[3]] + cc[0] << "\n";
}

int main() {
    int tt;
    cin >> tt;
    for (int i = 0; i < tt; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}


