#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <set>

using namespace std;

typedef long long ll;

void solve() {
    ll n, k;
    cin >> n >> k;
    set<pair<ll, ll> > pt;
    pt.insert({n, 1ll});
    while (true) {
        auto it = pt.end();
        --it;
//        cout << it->first << ' ' << it->second << endl;
        if (it->second >= k) {
            cout << (it->first) / 2 << ' ' << (it->first - 1) / 2 << endl;
            return;
        }
        k -= it->second;
        ll l = (it->first - 1) / 2;
        ll cnt = it->second;
        auto it1 = pt.lower_bound({l, 0});
        if (it1 != pt.end() && it1->first == l) {
            pt.insert({l, cnt + it1->second});
            pt.erase(it1);
        } else {
            pt.insert({l, cnt});
        }
        l = (it->first) / 2;
        cnt = it->second;
        it1 = pt.lower_bound({l, 0});
        if (it1 != pt.end() && it1->first == l) {
            pt.insert({l, cnt + it1->second});
            pt.erase(it1);
        } else {
            pt.insert({l, cnt});
        }
        pt.erase(it);
    }
}

int main() {
//    freopen("sum.in", "r", stdin);
//    freopen("sum.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cout.precision(20);
//    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}