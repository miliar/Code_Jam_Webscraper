#include <iostream>
#include <map>
using namespace std;
typedef long long ll;
int main () {
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        ll n, k, last;
        cin >> n >> k;
        map <ll, ll> a;
        a[n] = 1;
        while (k > 0) {
            ll sz = a.rbegin()->first, cnt = a[sz];
            a.erase(sz);
            last = sz;
            k -= cnt;
            a[sz/2] += cnt;
            a[(sz-1)/2] += cnt;
        }
        cout << "Case #" << t << ": ";
        cout << last/2 << " " << (last-1)/2 << endl;
    }
}
