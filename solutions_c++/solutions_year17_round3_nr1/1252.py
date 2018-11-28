#include <bits/stdc++.h>
using namespace std;

typedef vector<int> veci;
typedef pair<int,int> pii;
typedef vector<pii> vecii;
typedef long long ll;
typedef vector<ll> vecl;
typedef pair<ll,ll> pll;
typedef vector<pll> vecll;
#define EPS (1e-9)
#define MOD (int(1e9+7))
#define INF (int(1e9+9))
#define fi first
#define se second
#define PI acos(-1.0)

int main()
{
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int tc=1; tc<=tcases; ++tc)
{
    int n, k;
    cin >> n >> k;

    vecll v(n);
    for (int i=0; i<n; ++i) {
        cin >> v[i].fi >> v[i].se;
    }

    sort(v.rbegin(), v.rend(),
            [](const pll& l, const pll& r) {
            return (l.fi*l.se<r.fi*r.se); });

    ll max_r_idx = 0;
    ll max_radi = 0;
    for (int i=0; i<n; ++i) {
        if (v[i].fi>max_radi) {
            max_radi = v[i].fi;
            max_r_idx = i;
        }
    }

    ll max_radi_inner = 0;
    long double sum = 0.0;
    for (int i=0; i<k; ++i) {
        sum += 2.0*PI*v[i].fi*v[i].se;
        max_radi_inner = max(max_radi_inner,v[i].fi);
    }
    sum += PI*max_radi_inner*max_radi_inner;

    if (max_radi_inner<max_radi) {
        long double post_sum = sum;
        post_sum -= 2.0*PI*v[k-1].fi*v[k-1].se;
        post_sum -= PI*max_radi_inner*max_radi_inner;
        post_sum += PI*max_radi*max_radi;
        post_sum += 2.0*PI*v[max_r_idx].fi*v[max_r_idx].se;

        sum = max(sum,post_sum);
    }

    cout << "Case #" << tc << ": " << fixed << setprecision(10) << sum << endl;
}
    return 0;
}
