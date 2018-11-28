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
template <class T> void prc(T a, T b) {cout << "["; for (T i = a; i != b; ++i) {if (i != a) cout << ", "; cout << *i;} cout << "]";cout<<endl;}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);

	int t; cin >> t; FOR (tc, 1, t) {
		int n, k; cin >> n >> k;
		long double u;
		cin >> u;
		vector<long double> a(n);
		FOR (i, 0, n - 1) cin >> a[i];
		sort(all(a));
		a.push_back(1);++n;
		int f = 1;
		long double val = a[0];
		FOR (i, 1, n-1) {
			if ((a[i] - val)*f <= u) {
				u -= (a[i] - val)*f;
				f++;
				val = a[i];
			}
			else {
				val += u/f;
				u = 0;
				break;	
			}
		}
		long double ans = 1;
		FOR (i, 0, n - 1) {
			if (i < f) ans *= val;
			else ans *= a[i];
		}
		cout << "Case #" << tc << ": " << fixed << setprecision(10) << ans << "\n";
	}

	return 0;
}