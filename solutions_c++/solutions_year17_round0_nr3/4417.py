#include <iostream>
#include <string>
#include <set>

using namespace std;

typedef long long ll;

ll get_last(multiset<ll> &s) {
    auto it = s.end();
    it--;
    ll v = (*it);
    s.erase(it);
    return v;
}

void solve(ll n, ll k) {
    multiset<ll> s;
    s.insert(n);
    for (int i = 1; i < k; i++) {
        ll v = get_last(s);
        ll a = v / 2;
        ll b = v - 1 - a;
        if (a > 0)
            s.insert(a);
        if (b > 0)
            s.insert(b);
    }
    ll v = get_last(s);
    ll a = v / 2, b = v - 1 - v / 2;
    cout << max(a, b) << " " << min(a, b) << endl;
}

int main(int argc, char **argv) {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        ll n, k;
        cin >> n >> k;
        cout << "Case #" << i + 1 << ": ";
        solve(n, k);
    }
    return 0;
}
