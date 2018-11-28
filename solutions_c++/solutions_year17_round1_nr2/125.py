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
const int MX = 2e6;

multiset<int> ss[60];
int n, p;
vector<pair<int, int> > st[MX];
ll nd[60];

void solve() {
    cin >> n >> p;
    for (int i = 0; i < n; ++i)
        cin >> nd[i];
    for (int i = 0; i < MX; ++i)
        st[i].clear();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            ll x;
            cin >> x;
            ll lb = 0;
            ll rb = 2 * x;
            while (rb - lb > 1) {
                ll mid = (lb + rb) >> 1;
                if (10 * x >= 9 * mid * nd[i])
                    lb = mid;
                else
                    rb = mid;
            }
            ll mx = lb;
            lb = 0;
            rb = 2 * x;
            while (rb - lb > 1) {
                ll mid = (lb + rb) >> 1;
                if (10 * x <= 11 * mid * nd[i])
                    rb = mid;
                else
                    lb = mid;
            }
            ll mn = rb;
            if (mn <= mx)
                st[mn].push_back(make_pair(mx, i));
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i)
        ss[i].clear();
    for (int i = 0; i < MX; ++i) {
        for (auto x: st[i]) {
            ss[x.second].insert(x.first);
        }
        while (true) {
            int fl = 0;
            for (int j = 0; j < n; ++j) {
                while (!ss[j].empty() && *(ss[j].begin()) < i)
                    ss[j].erase(ss[j].begin());
                if (ss[j].empty())
                    fl = 1;
            }
            if (fl)
                break;
            ++ans;
            for (int j = 0; j < n; ++j)
                ss[j].erase(ss[j].begin());
        }
    }
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


