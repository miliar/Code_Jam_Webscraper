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

int k;
string s;

inline bool read() {
	cin >> s >> k;
	return true;
}
   
inline void solve(int tc) {   
	cout << "Case #" << tc << ": ";
	int ans = 0;
	forn (i, sz(s)) {
		if (s[i] == '-') {
			forn (j, k) {
				if (i + j >= sz(s)) {
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				s[i + j] = s[i + j] == '+' ? '-' : '+';
			}
			ans++;
		//	cerr << s << endl;
		}
	}
	cout << ans << endl;
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
		read();
		solve(i + 1);
	}
	
#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}