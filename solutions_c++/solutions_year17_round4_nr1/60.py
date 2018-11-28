#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
#define LOG
#endif

const int N = 1000;
int n, m;
int a[N];

bool read() {
	if (!(cin >> n >> m))
		return false;
	memset(a, 0, sizeof(a));
	forn(i, n) {
		int x;
		assert(cin >> x);
		a[x % m]++;
	}
	return true;
}

map <vector <int>, int> ans;

int calc(int sum, vector <int> v) {
	if (ans.count(v))
		return ans[v];
	ans[v] = 0;
	int &res = ans[v];
	forn(i, m - 1) {
		if (v[i] + 1 <= a[i + 1]) {
			v[i]++;
			res = max(res, (sum == 0) + calc((sum + i + 1) % m, v));
			v[i]--;
		}
	}
	return res;
}

void solve(int tc) {
	printf("Case #%d: ", tc + 1);
	int res = 0;
	res += a[0];
	ans.clear();
	res += calc(0, vector <int> (m - 1, 0));
	cout << res << endl;
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int t;
	assert(cin >> t);

	forn(test, t) {
		assert(read());
		ld stime = gett();
		solve(test);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
