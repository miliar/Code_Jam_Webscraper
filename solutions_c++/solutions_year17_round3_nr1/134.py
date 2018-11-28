#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define NFOR(i,a,b) for(int i = (a); i >= (b); --i)
#define all(x) (x).begin(), (x).end()
#define sz(x) int(x.size())
typedef long long ll; typedef pair <int, int> ii; typedef vector <int> vi; const int inf = 1e9 + 7;
#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cout << str << " : " << t << endl;}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cout << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cout << "["; for (T i = a; i != b; ++i) {if (i != a) cout << ", "; cout << *i;} cout << "]"; cout << endl;}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);

	int t; cin >> t; FOR (tc, 1, t) {
		int n, k; cin >> n >> k;
		vector<pair<ll, ll>> a(n);
		FOR (i, 0, n - 1) cin >> a[i].F >> a[i].S;
		sort(all(a), [](const pair<ll, ll> &x, const pair<ll, ll> &y) {
			return x.F * x.S < y.F * y.S;
		});
		ll ans = 0;
		--k;
		FOR (i, 0, n - 1) {
			int done = 0;
			ll now = a[i].F * a[i].F + 2 * a[i].F * a[i].S;
			NFOR (j, n - 1, 0) {
				if (done == k) {
					break;
				}
				if (j == i or a[j].F > a[i].F) continue;
				++done;
				now += 2 * a[j].F * a[j].S;
			}
			if (done == k) {
				ans = max(ans, now);
			}
		}

		cout << fixed << setprecision(10) << "Case #" << tc << ": " << (M_PI * ans) << "\n";
	}

	return 0;
}


