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

const ll INF = 1e18;
ll hd, ad, hk, ak, b, d;
const int MX = 200;
void solve() {
    cin >> hd >> ad >> hk >> ak >> b >> d;
    ll ans = INF;
    for (int n = 0; n < MX; ++n)
        for (int m = 0; m < MX; ++m) {
            ll cnt = 0;
            ll now = hd;
            for (int i = 0; i < m; ++i) {
                if (ak - (i + 1) * d >= now) {
                    ++cnt;
                    now = hd - (ak - i * d);
                }
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
                ++cnt;
                now -= ak - (i + 1) * d;
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
            }
            if (cnt >= INF)
                continue;
            for (int i = 0; i < n; ++i) {
                if (ak - m * d >= now) {
                    ++cnt;
                    now = hd - (ak - d * m);
                }
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
                ++cnt;
                now -= ak - m * d;
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
            }
            if (cnt == INF)
                continue;
            ll nowk = hk;
            while (nowk > 0) {
                if (nowk <= ad + n * b) {
                    ++cnt;
                    break;
                }
                if (ak - m * d >= now) {
                    ++cnt;
                    now = hd - (ak - d * m);
                }
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
                ++cnt;
                nowk -= ad + n * b;
                now -= ak - m * d;
                if (now <= 0) {
                    cnt = INF;
                    break;
                }
            }
            ans = min(ans, cnt);
        }
    if (ans >= INF)
        cout << "IMPOSSIBLE\n";
    else
        cout << ans << "\n";
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


