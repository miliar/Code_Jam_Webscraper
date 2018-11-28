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
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;

int n, k;

inline bool read() {
	cin >> n >> k;
	return true;
}

struct e {
	int len;
	int l, r;
	e (int cl, int cr) {
		l = cl, r = cr;
		len = r - l;
	}
};

bool operator < (const e &a, const e &b) {
	if (a.len != b.len)
		return a.len < b.len;
	return a.l > b.l;
}
   
inline void solve() {
	set<e> s;
	s.insert(e(0, n - 1));
	e last(0, 0);
	forn (i, k) {
		last = *s.rbegin();
		s.erase(--s.end());
		int mid = (last.l + last.r) / 2;
		if (last.l <= mid - 1)
			s.insert(e(last.l, mid - 1));
		if (mid + 1 <= last.r)
			s.insert(e(mid + 1, last.r));
	}
	int mid = (last.l + last.r) / 2;
	int fl = mid - last.l;
	int fr = last.r - mid;
	cout << max(fl, fr) << ' ' << min(fl, fr) << endl;
}

int main()
{
#ifdef SU2
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int t;
	cin >> t;
	forn (i, t) {
		assert(read());
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}