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

const int N = int(1e6) + 5;
int ls[N], rs[N];
bool occ[N];
int n, k;

bool read() {
	if (!(cin >> n >> k))
		return false;
	return true;
}

void solve(int tc) {
	cerr << tc << endl;
	forn(i, n) {
		ls[i] = i;
		rs[n - i - 1] = i;
		occ[i] = false;
	}

	set <pair <pt, int> > now;
	forn(i, n)
		now.insert(mp(mp(min(ls[i], rs[i]), max(ls[i], rs[i])), -i));

	int last = -1;
	forn(_, k) {
		auto best = *now.rbegin();
		now.erase(best);
		last = -best.y;
		occ[last] = true;

		forn(i, n) {
			int j = last + i + 1;
			if (occ[j] || j == n)
				break;
			now.erase(mp(mp(min(ls[j], rs[j]), max(ls[j], rs[j])), -j));
			ls[j] = max(0, j - last - 1);
			now.insert(mp(mp(min(ls[j], rs[j]), max(ls[j], rs[j])), -j));
		}

		forn(i, n) {
			int j = last - i - 1;
			if (occ[j] || j == -1)
				break;
			now.erase(mp(mp(min(ls[j], rs[j]), max(ls[j], rs[j])), -j));
			rs[j] = max(0, last - j - 1);
			now.insert(mp(mp(min(ls[j], rs[j]), max(ls[j], rs[j])), -j));
		}
	}

	printf("Case #%d: %d %d\n", tc + 1, max(ls[last], rs[last]), min(ls[last], rs[last]));
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int n;
	assert(cin >> n);
	int tc = 0;

    while (read()) {
		ld stime = gett();
		solve(tc++);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
