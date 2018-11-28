#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<ld, ld> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;

ld d;
int n;
vector<pt> p;

inline bool read() {
	cin >> d >> n;
	p.resize(n);
	forn (i, n) {
		cin >> p[i].x >> p[i].y;
	}
	
	return true;
}

void print(vector<pt> p) {
	for (pt c : p)
		cerr << c.x << ' ' << c.y << endl;
	cerr << endl;
}

bool ok(ld v) {
	forn (j, n) {
		ld t = (0 - p[j].x) / (p[j].y - v);
		ld x = v * t;
		if (v <= p[j].y)
			continue;
		if (x <= d)
			return false;
	}
	return true;
}
   
inline void solve() {   
	
	sort(all(p));
	
	for (int i = n - 1; i >= 0; --i) {
		bool ok = true;
		for (int j = i + 1; j < sz(p); ++j) {
			if (p[i].y <= p[j].y)
				continue;
			ld t = (p[i].x - p[j].x) / (p[j].y - p[i].y);
			ld x = p[i].x + p[i].y * t;
			if (x + EPS >= d)
				continue;
			ok = false;
		}
		if (!ok) {
			p.erase(p.begin() + i, p.begin() + i + 1);
			n--;
		}
	}
	
	
	ld l = 0, r = INF64;
	forn (it, 300) {
		ld mid = (l + r) / 2;
		if (ok(mid))
			l = mid;
		else
			r = mid;
	}
	cout << l << endl;
}

int main()
{
#ifdef SU2
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(6) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int t;
	cin >> t;
	forn (i, t) {
		read();
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}