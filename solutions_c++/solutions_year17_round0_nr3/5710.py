#include <bits/stdc++.h>
#define d(x) if(debug) cerr<<#x<<": "<<x<<endl;
#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;

bool debug = 0;

template<class T> ostream& operator<<(ostream& os, vector<T>& v) {for (auto i : v) os << i << " "; return os;}
template<class T> ostream& operator<<(ostream& os, set<T>& v) {for (auto i : v) os << i << " "; return os;}
template<class T, class R> ostream& operator<<(ostream& os, pair<T, R>& v) {os << '(' << v.X << ' ' << v.Y << ')' << ' '; return os;}

inline ll get() {
	ll x;
	cin >> x;
	return x;
}

void solve();

int main() {
#ifdef The_Fusy
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	debug = 1;
#endif
	ios_base::sync_with_stdio(false);
	solve();
	if (debug)
		cerr << endl << "Time: " << (ld(clock()) / ld(CLOCKS_PER_SEC)) << endl << endl;
	return 0;
}

void tp(ll test, ll mn, ll mx){
	cout << "Case #"<< test << ": "<< mx << ' ' << mn << "\n";
}

void solve() {
	ll t = get();
	for(ll test = 1; test <= t; test++){
		ll n = get(), k = get();
		vector<ll> v(n + 2);
		v[0] = 1, v.back() = 1;
		ll nw, mn, mx;
		for(ll i = 0; i < k; i++){
			nw = mn = mx = -1;
			for(ll i = 1; i <= n; i++){
				if(v[i] == 1) continue;
				ll nwl = 0;
				ll nwr = 0;
				for(ll j = i - 1; j >= 1; j--){
					if(v[j] == 1) break;
					nwl++;
				}
				for(ll j = i + 1; j <= n; j++){
					if(v[j] == 1) break;
					nwr++;
				}
				ll mnn = min(nwl, nwr);
				ll mxn = max(nwl, nwr);
				if(nw == -1 || mnn > mn || mnn == mn && mxn > mx){
					nw = i;
					mn = mnn;
					mx = mxn;
				}
			}
			v[nw] = 1;
		}
		tp(test, mn, mx);
	}
}
