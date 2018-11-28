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

void solve() {
	ll t = get();
	for (ll test = 1; test <= t; test++) {
		string s;
		cin >> s;
		ll k = get();
		ll ans = 0;
		for (ll i = 0; i < s.size() - k + 1; i++) {
			if (s[i] == '-') {
				ans++;
				for (ll j = 0; j < k; j++) {
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
			}
		}
		bool u = true;
		for (ll i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				u = false;
				break;
			}
		}
		cout << "Case #" << test << ": ";
		if (u) {
			cout << ans << '\n';
		} else cout << "IMPOSSIBLE\n";
	}
}
