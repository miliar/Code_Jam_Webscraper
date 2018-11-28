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

typedef unsigned long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18) + 5;
const ld EPS = 1e-9;

li n;

inline bool read() {
	cin >> n;
	return true;
}

li dp[25][10];
   
li restore(int i, li k) {
	li ans = 0;
	int last = 1;
	for (int ii = 1; ii < i; ++ii)
		for (int j = 1; j < 10; ++j)
			k -= dp[ii][j];
	cerr << k << endl;
	while(i >= 1) {
		for (int j = last; j < 10; ++j)
			if (dp[i][j] > k) {
				ans = min(INF64, ans * 10 + j);
				last = j;
				break;
			} else {
				k -= dp[i][j];
			}
		i--;
	}
	return ans;
}

li getk(li k) {
	li kk = k;
	for (int i = 1; i < 20; ++i)
		for (int j = 1; j < 10; ++j) {
			if (dp[i][j] > kk) {
				return restore(i, k);
			} else {
				kk -= dp[i][j];
			}
		}	
	return INF64;
}

inline void solve(int tc) {   
	cout << "Case #" << tc << ": ";
	li last = 0;
	for (int i = 60; i >= 0; --i)
		if (getk(last + (1 << i)) <= n)
			last += 1 << i;
	cout << getk(last) << endl;
}

void upd(li &a, li b) {
	a += b;
	a = min(a, INF64);
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
	
	forn (i, 10)
		dp[1][i] = 1;
	for (int i = 1; i < 20; ++i)
		for (int j = 1; j < 10; ++j)
			for (int nj = j; nj >= 1; --nj)
				upd(dp[i + 1][nj], dp[i][j]);
	
	forn (i, 10) {
		forn (j, 10)
			cerr << dp[i][j] << ' ';
		cerr << endl;
	}
	int t;
	cin >> t;
	forn (i, t) {
		assert(read());
		solve(i + 1);
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}