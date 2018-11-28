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

int n, c, m;
int a[12000];
int cc[12000];

void solve() {
    cin >> n >> c >> m;
    for (int i = 0; i < c; ++i)
        cc[i] = 0;
    for (int i = 0; i < n; ++i)
        a[i] = 0;
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        --x;
        --y;
        ++cc[y];
        ++a[x];
    }
    int mx = 0;
    for (int i = 0; i < c; ++i)
        mx = max(mx, cc[i]);
    int l = mx - 1;
    int r = 2000;
    while (r - l > 1) {
        int mid = (l + r) >> 1;
        int now = 0;
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] > mid)
                now -= a[i] - mid, cur += a[i] - mid;
            else
                now += mid - a[i];
            if (now < 0)
                break;
        }
        if (now < 0)
            l = mid;
        else
            r = mid;
    }
    int mid = r;
    int now = 0;
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] > mid)
            now -= a[i] - mid, cur += a[i] - mid;
        else
            now += mid - a[i];
        if (now < 0)
            break;
    }
    cout << r << " " << cur << "\n";
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


