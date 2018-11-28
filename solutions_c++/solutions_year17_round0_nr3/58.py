#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <tuple>
using namespace std;
using ll = long long;

#define FU(i, a, b) for (auto i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (auto i = (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb emplace_back

int main() {
    ios::sync_with_stdio(false);
    ll T;
    cin >> T;
    for (ll t = 1; t <= T; ++t) {
        ll n, k;
        cin >> n >> k;
        map<ll,ll,greater<ll>> q;
        q.emplace(n, 1);
        ll last = n;
        while (k > 0) {
            ll size, count;
            auto it = q.begin();
            tie(size, count) = *it;
            q.erase(it);
            last = size;
            k -= count;
            q[size/2] += count;
            q[(size-1)/2] += count;
        }
        cout << "Case #" << t << ": "
             << (last/2) << " " << ((last-1)/2) << endl;
    }
    return 0;
}
