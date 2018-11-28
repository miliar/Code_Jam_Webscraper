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

int n, p;
const int N = 105;

int a[N];

inline bool read() {
	cin >> n >> p;
	forn (i, n)
		cin >> a[i];
	return true;
}

int dp[N][N][N][4];
   
int calc(int l1, int l2, int l3, int x) {
	if (dp[l1][l2][l3][x] != -1)
		return dp[l1][l2][l3][x];
	if (l1 == 0 && l2 == 0 && l3 == 0)
		return 0;
	int r[4] = {0, l1, l2, l3};
	int &res = dp[l1][l2][l3][x];
	res = x == 0;
	forn (i, 4) {
		if (!r[i])
			continue;
		int nx = (x - i + p) % p;
		r[i]--;
		res = max(res, calc(r[1], r[2], r[3], nx) + (x == 0));
		r[i]++;
	}
	return res;
}

inline void solve() {   
	vector<int> cnt(4, 0);
	memset(dp, -1, sizeof dp);
	forn (i, n)
		cnt[a[i] % p]++;
	cout << cnt[0] + calc(cnt[1], cnt[2], cnt[3], 0) << endl;
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
		cout << "Case #" << i + 1 << ": ";
	assert(read());
	solve();
}
	
#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}	