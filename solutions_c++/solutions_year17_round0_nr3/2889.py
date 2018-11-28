#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

void add(set< pair<ll, ll> > & s, ll n, ll k) {
    set< pair<ll, ll> >::iterator it = s.lower_bound(make_pair(n, 0LL));
    if (it == s.end() || it->first != n)
        s.insert(make_pair(n, 0LL));
    it = s.lower_bound(make_pair(n, 0LL));
    pair<ll, ll> new_pair = make_pair(n, it->second + k);
    s.erase(it);
    s.insert(new_pair);
}

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        ll n, k;
        cin >> n >> k;
        set< pair<ll, ll> > s;
        s.insert(make_pair(n, 1LL));
        while (s.size()) {
            set< pair<ll, ll> >::iterator it = s.end();
            --it;
            ll curn = it->first;
            ll curk = it->second;
            s.erase(it);
            if (k <= curk) {
                cout << "Case #" << ttt << ": " << curn / 2LL << " " << (curn - 1LL) / 2LL << "\n";
                break;
            }
            k -= curk;
            add(s, curn / 2LL, curk);
            add(s, (curn - 1LL) / 2LL, curk);
        }
    }

    return 0;
}
