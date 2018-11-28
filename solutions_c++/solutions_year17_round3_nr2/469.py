#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define all(x) begin(x),end(x)
#define sz(x) ((int)(x).size())
#define F(i,n) for (int i = 0; i < n; ++i)
#define mp make_pair
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;

template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ "; for (auto it : c) s << it << " "; s<<"\b]\n";
  return s;
}

typedef pair<pii, int> pii_i;

int main () {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	pair<pii_i, pii_i> tpb[4];
	int an[4];
	tpb[0] = mp(mp(mp(0,0),(0)),mp(mp(1440,1440),(0)));
	an[0] = 0;
	tpb[1] = mp(mp(mp(0,0),(0)),mp(mp(1440,1440),(1)));
	an[1] = 1;
	tpb[2] = mp(mp(mp(0,0),(1)),mp(mp(1440,1440),(0)));
	an[2] = 1;
	tpb[3] = mp(mp(mp(0,0),(1)),mp(mp(1440,1440),(1)));
	an[3] = 0;
	//ios_base::sync_with_stdio(0); cin.tie(0)
	int _; cin >> _; for(int __ = 0; __ < _; ++__) {
	int a, b; cin >> a >> b;
	int T[2]; T[0] = 0; T[1] = 0;
	vector<pii_i> V;
	for (int i = 0; i < a; ++i) {
		int c, d; cin >> c >> d;
		T[1] += d - c;
		V.pb(mp(mp(c, d), 1));
	}
	for (int i = 0; i < b; ++i) {
		int c, d; cin >> c >> d;
		T[0] += d - c; 
		V.pb(mp(mp(c, d), 0));
	}
	//cout << T[0] << ' ' << T[1] << '\n';
	
	
	int Ans = 1000000000;
	for (int meow = 0; meow < 4; ++meow) {
		int t[2]; t[0] = T[0], t[1] = T[1];
		vector<pii_i> v(V);
		v.pb(tpb[meow].fi); v.pb(tpb[meow].se);
		sort(all(v));
		auto ptr = unique(all(v));
		v.resize(ptr - v.begin());
		int tc, im = 0, ans = an[meow]; 
		
		vector<int> to[2];
		for (int i = 0; i < v.size() - 1; ++i) {
			if (v[i].se == v[i + 1].se) {
				to[v[i].se].pb(v[i + 1].fi.fi - v[i].fi.se);
				t[v[i].se] += v[i + 1].fi.fi - v[i].fi.se;
			}
			if (v[i].se != v[i + 1].se) im += v[i + 1].fi.fi - v[i].fi.se, ++ans;
		}
		//cout << meow << ' ' << t[0] << ' ' << t[1] << '\n';
		if (t[0] > t[1]) tc = 0, t[0] -= t[1];
		else tc = 1, t[1] -= t[0];
		if (t[tc] > im) {
			sort(all(to[tc]));
			t[tc] -= im;
			int it = to[tc].size() - 1;
			while (t[tc] > 0) {
				t[tc] -= 2  * to[tc][it];
				--it;
				ans += 2;
			}
		}
		if (ans < Ans) {
			Ans = ans; //cout << meow << "MEOW" << '\n';
		}
	}
	cout << "Case #" << __ + 1 << ": " << Ans << '\n';
	}
	return 0;
}

