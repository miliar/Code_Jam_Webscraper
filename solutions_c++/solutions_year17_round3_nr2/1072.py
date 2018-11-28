#include <bits/stdc++.h>
using namespace std;

typedef vector<int> veci;
typedef pair<int,int> pii;
typedef vector<pii> vecii;
typedef long long ll;
typedef vector<ll> vecl;
typedef pair<ll,ll> pll;
typedef vector<pll> vecll;
typedef tuple<int,int,int> tup;
typedef vector<tup> vtup;
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
    int ac, aj;
    cin >> ac >> aj;

    vtup vt(ac+aj);
    int b, e, val;
    for (int i=0; i<ac; ++i) {
        cin >> b >> e;
        val = 1;
        get<0>(vt[i]) = b;
        get<1>(vt[i]) = e;
        get<2>(vt[i]) = val;
    }

    for (int i=ac; i<ac+aj; ++i) {
        cin >> b >> e;
        val = 2;
        get<0>(vt[i]) = b;
        get<1>(vt[i]) = e;
        get<2>(vt[i]) = val;
    }

    sort(vt.begin(), vt.end());

    int res;
    if (ac+aj==1) {
        res = 2;
    } else if (ac+aj==2) {
        if (ac==2 || aj==2) {
            if (get<1>(vt[1])-get<0>(vt[0])<=720 ||
                    get<1>(vt[0])+(1440-get<0>(vt[1]))<=720) {
                res = 2;
            } else {
                res = 4;
            }
        } else {
            res = 2;
        }
    }

    cout << "Case #" << tc << ": " << res << endl;
}
    return 0;
}
