#include <bits/stdc++.h>

using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll big = 1000000007ll;
ll big2 = 1000000009ll;
ll n,m,q,T,k;

ll d;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    ll a,b,c;

    cin >> T;

    for(ll c4 = 0; c4 < T; c4++){
        cin >> d >> n;
        vector<ld> K;
        vector<ld> S;
        for(ll c1 = 0; c1 < n; c1++){
            cin >> a >> b;
            K.push_back(ld(a));
            S.push_back(ld(b));
        }

        ld mi = -big*big;

        for(ll c2 = 0; c2 < n; c2++){
            mi = max(mi , (ld(d) - K[c2]) / S[c2]);
        }

        ld ans = ld(d)/mi;

        cout << "Case #" << c4+1 << ": " << setprecision(18) << ans << "\n";

    }

    return 0;
}
