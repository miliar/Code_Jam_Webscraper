#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); ++i)
#define fi first
#define se second

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
	int T;
	cin >> T;

	ll n,k;
	FOR(t,T) {
	    cin >> n >> k;
	    n++;
	    ll l2 = 1;
	    unordered_map<ll, ll> tab;
	    tab[n] = 1;
	    vector<pair<ll,ll>> vec;
	    l2 *= 2;
	    while (l2 <= k) {
            FOREACH(it, tab) {
                ll x = it->fi;
                ll x1 = x/2;
                ll x2 = x1;
                if (x % 2 != 0) {
                    x2++;
                }
                vec.pb(mp(x1, it->se));
                vec.pb(mp(x2, it->se));
            }
            tab.clear();
            FOREACH(it, vec) {
                tab[it->fi] += it->se;
            }
            vec.clear();
            l2 *= 2;
	    }
	    l2 /= 2;
	    pair<ll,ll> res;
	    if (tab.size() == 1) {
            auto it = tab.begin();
            pair<ll,ll> x1 = *it;
            if (x1.fi%2==0)
                res = mp(x1.fi/2,x1.fi/2);
            else
                res = mp((x1.fi/2)+1,x1.fi/2);
	    } else {
            auto it = tab.begin();
            pair<ll,ll> x1 = *it;
            it++;
            pair<ll,ll> x2 = *it;
            if(x2.fi > x1.fi)
                swap(x1,x2);
            k -= l2;
            k++;
            if (k <= x1.se) {
                if (x1.fi%2 == 0)
                    res = mp(x1.fi/2,x1.fi/2);
                else
                    res = mp((x1.fi/2)+1,x1.fi/2);
            } else {
                if (x2.fi%2 == 0)
                    res = mp(x2.fi/2,x2.fi/2);
                else
                    res = mp((x2.fi/2)+1,x2.fi/2);
            }
	    }
		cout << "Case #" << t+1 << ": ";
        cout << res.fi-1 << " " << res.se-1;
		cout << endl;
	}
	return 0;
}
