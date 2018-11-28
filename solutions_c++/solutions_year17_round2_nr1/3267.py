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

int main()
{
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int tc=1; tc<=tcases; ++tc)
{
    int d, k;
    cin >> d >> k;

    vecii v(k);
    for (int i=0; i<k; ++i) {
        cin >> v[i].fi >> v[i].se;
    }

    double l = 0;
    double r = 1e15;
    for (int loop=0; loop<200; ++loop) {
        double mid = l + (r-l)/2.0;

        double time_annie = double(d)/mid;
        bool flag = true;
        for (int i=0; i<k; ++i) {
            double time_others = double(d-v[i].fi)/double(v[i].se);
            if (time_annie<time_others) {
                flag = false;
                break;
            }
        }

        if (flag)
            l = mid+EPS;
        else
            r = mid;
    }

    cout << "Case #" << tc << ": " << fixed << setprecision(10) << l << endl;
}
    return 0;
}
