#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)
#define ll long long

using namespace std;

ll find(ll n, ll m, auto& s) {
    if (s.find(n) != s.end()) return s[n];
    if (n <= m) return 0;
    ll x = (n - 1) / 2;
    ll y = n - 1 - x;
    s[n] = 1ll + find(x, m, s) + find(y, m, s);
    return s[n];
}

int main() {
    int T;
    cin >> T;
    cerr << T << endl;
    fin(I, T) {
        cerr << I << endl;
        cout << "Case #" << I + 1 << ": ";
        ll n, k;
        cin >> n >> k;
        k--;
        ll l = 0, r = n;
        while (l != r) {
            ll m = (l + r) / 2;
            map<ll, ll> s;
            int nb = find(n, m, s);
//            cerr << n << " " << k << " : " << m << " " << nb << endl;
            if (nb > k) l = m + 1;
            else r = m;
        }
        cerr << l << endl;
        l--;
        cout << (ll)(l / 2) + (l % 2) << " " << (ll)(l / 2) << endl;
    }
}
