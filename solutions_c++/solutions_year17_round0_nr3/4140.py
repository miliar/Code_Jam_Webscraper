#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;

ll two = 2ll;
ll one = 1ll;

string solve() {

    ll n, k;
    cin >> n >> k;

    multiset<ll> distances;
    distances.insert(-n);

    rep(i,0,k-1) {
        ll topdist = -(*distances.begin());
        distances.erase(distances.begin());
        if (topdist % two == 0ll) {
            ll d1 = topdist / two;
            ll d2 = d1-one;
            distances.insert(-d1);
            if (d2 > 0) {
                distances.insert(-d2);
            }
        } else {
            ll d = topdist / two;
            if (d > 0ll) {
                distances.insert(-d);
                distances.insert(-d);
            }
        }
    }

    ll lastdist = -(*distances.begin());


    ll minn, maxx;

    if (lastdist % two == 0ll) {
        maxx = lastdist / two;
        minn = maxx-one;
    } else {
        maxx = lastdist / two;
        minn = maxx;
    }

    string ans = to_string(maxx) + " " + to_string(minn);

    return ans;

}

    
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    }


    return 0;
}
