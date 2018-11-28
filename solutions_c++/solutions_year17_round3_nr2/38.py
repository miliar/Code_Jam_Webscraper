#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define REP(i,a) FOR(i,0,(int)(a)-1)
#define reset(a,b) memset(a,b,sizeof(a))
#define BUG(x) cout << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR (_,a,b) cout << x[_] << ' '; cout << endl;}
#define CON(x) {cout << #x << " = "; for(auto i:x) cout << i << ' '; cout << endl;}
#define mod 1000000007
#define pi acos(-1)
#define eps 1e-20
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

int t;
int a, b, st, en, unia, unib, ans;
vector<pair<pair<int, int>, char> > v;
vector<int> va, vb;

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> a >> b;
		v.clear();
		va.clear();
		vb.clear();
		REP (i, a) {
			cin >> st >> en;
			v.pb({{st, en}, 'A'});
		}
		REP (i, b) {
			cin >> st >> en;
			v.pb({{st, en}, 'B'});
		}
		sort(v.begin(), v.end());
		unia = unib = 0;
		int tmp = -1;
		for (auto p: v) {
			if (p._2 == 'B') tmp = -1;
			else {
				unia += p._1._2 - p._1._1;
				if (tmp != -1) unia += p._1._1 - tmp, va.pb(p._1._1 - tmp);
				tmp = p._1._2;
			}
		}
		if (v.back()._2 == 'A' && 'A' == v[0]._2) {
			int aa = v[0]._1._1 + 60 * 24 - v.back()._1._2;
			unia += aa;
			va.pb(aa);
		}
		tmp = -1;
		for (auto p: v) {
			if (p._2 == 'A') tmp = -1;
			else {
				unib += p._1._2 - p._1._1;
				if (tmp != -1) unib += p._1._1 - tmp, vb.pb(p._1._1 - tmp);
				tmp = p._1._2;
			}
		}
		if (v.back()._2 == 'B' && 'B' == v[0]._2) {
			int bb = v[0]._1._1 + 60 * 24 - v.back()._1._2;
			unib += bb;
			vb.pb(bb);
		}
		char c = v[0]._2;
		ans = 0;
		for (auto p: v) {
			if (p._2 != c) ans++;
			c = p._2;
		}
		if (v.back()._2 != v[0]._2) ans++;
		if (unia > 720) {
			sort(va.begin(), va.end());
			while (unia > 720) {
				unia -= va.back();
				va.pop_back();
				ans += 2;
			}
		} else if (unib > 720) {
			sort(vb.begin(), vb.end());
			while (unib > 720) {
				unib -= vb.back();
				vb.pop_back();
				ans += 2;
			}
		}
		cout << ans << endl;
	}
}
