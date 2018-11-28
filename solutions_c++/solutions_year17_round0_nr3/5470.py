#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (ll (i)=(0);(i)<(ll)(n);++(i))
typedef pair<int, int> P;
typedef long long ll;

inline void output(int i, ll ma, ll mi) {
    cout << "Case #" << i+1 << ": " << ma << " " << mi << endl;
}

int main() {
    ios::sync_with_stdio();
    cin.tie(0);

    ll t;
    cin >> t;

    rep(i, t) {
        ll n, k;
        cin >> n >> k;

        if (n == k) {
            output(i, 0, 0);
            continue;
        }
        else if (k == 1) {
            if (n%2 == 0) {
                output(i, n/2, n/2-1);
            }
            else {
                output(i, n/2, n/2);
            }
            continue;
        }

        vector<ll> p;
        p.push_back(0);
        if (n%2 == 1) {
            p.push_back(n/2+1);
        }
        else {
            p.push_back(n/2);
        }
        ll last = n+1;

        for (ll j=1; j<k; ++j) {
            ll ma = -1;
            pair<ll, ll> pos;

            for (ll l=0; l<p.size()-1; ++l) {
                if (ma < p[l+1]-p[l]-1) {
                    ma = p[l+1]-p[l]-1;
                    pos = make_pair(l, l+1);
                }
            }

            if (ma < last-p[p.size()-1]-1) {
                pos = make_pair(p.size()-1, last);
            }

            int a = p[pos.first];
            int b = 0;
            if (pos.second == last) {
                b = last;
            }
            else {
                b = p[pos.second];
            }

            int P = (a+b)/2;

            if (j+1 == k) {
                p.push_back(n+1);
                auto it = lower_bound(p.begin(), p.end(), P);
                output(i, max(P-*(it-1)-1, (*it)-P-1), min(P-*(it-1)-1, (*it)-P-1));

            }
            else {
                p.push_back(P);
                sort(p.begin(), p.end());
            }

        }

    }
}
