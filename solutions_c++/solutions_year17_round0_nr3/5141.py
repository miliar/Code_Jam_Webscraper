#include "io.h"

/***************************** START COPY ************************************/

#include "bits/stdc++.h"
using namespace std;

#define forn(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define forn1(i, n) for(int i = 1; i <= int(n);++(i))
#define rforn(i,n) for(int (i)=n-1;(i)>=(int)(0);--(i))
#define forlu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rforlu(i,l,u) for(int (i)=(int)(u-1);(i)>=(int)(l);--(i))
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define out(x) cout<<x<<'\n';
#define outp(x,pr) cout<<fixed<<setprecision(pr)<<x<<'\n';
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef unsigned long ul; typedef long long ll; typedef unsigned long long ull;
typedef unsigned int ui; typedef long double ld;
typedef vector<int> vi; typedef vector<bool> vb; typedef pair<int, int> pii; typedef vector<pair<int, int>> vpii;
typedef vector<double> vd; typedef pair<double, double> pdd; typedef vector<pdd> vpdd;
typedef vector<string> vs; typedef vector<ll> vll; typedef vector<ld> vld;
typedef set<int> si; typedef map<int, int> mii; typedef multimap<int, int> mmii;

#ifdef LOCAL
struct dbger {
	template<typename T> dbger& operator,(const T& v) { cerr << v << " "; return *this; }
} dbg;
#define debug(...) { cerr << #__VA_ARGS__ << " : "; dbg, __VA_ARGS__; cerr << '\n'; }
#define file "c"
#define REOPEN() freopen(file".in", "r", stdin); freopen(file".out", "w", stdout); freopen("test.err", "w", stderr);
struct file_stdio { file_stdio() { REOPEN() }; } file_stdio;
struct timer {
	clock_t t = clock();
	~timer() { std::cerr << "tot elapsed: " << 1000.0 * (clock() - t) / CLOCKS_PER_SEC << " ms\n"; };
} dt;
#define TSTAMP() std::cerr << "elapsed: " << 1000.0 * (clock() - dt.t) / CLOCKS_PER_SEC << " ms\n";
#else
#define debug(...)
#endif

//const int MAXN = 1200;
//int dp[MAXN][MAXN];
//int dp[MAXN][2];
//void init() { memset(dp, 0, sizeof(dp[0][0]) * (MAXN * 2)); }

//const int MOD = 1000 * 1000 * 1000 + 7;
//const ll MOD2 = 1ll * MOD * MOD;
//inline int mod(int lhs, int rhs = MOD) { return (lhs % rhs + rhs) % rhs; }
//inline int mod(ll lhs, int rhs = MOD) { return (int(lhs % rhs) + rhs) % rhs; }
//inline int mod_add(int lhs, int rhs) { return ((lhs % MOD) + (rhs % MOD)) % MOD; }
//inline int mod_sub(int lhs, int rhs) { return lhs - rhs < 0 ? lhs - rhs + MOD : lhs - rhs; }
//inline int mod_sub2(int lhs, int rhs) { return ((lhs % MOD) - (rhs % MOD)) % MOD; }]\
//#define EPS 1e-7

struct custom_less 
{ 
	bool operator()(pii a, pii b) { 
		return min(a.first,a.second) < min(b.first, b.second) || 
			(min(a.first,a.second) == min(b.first, b.second) && max(a.first, a.second) < max(b.first, b.second));
	} 
};

pii solve(int n, int k)
{
	priority_queue<pii, vector<pii>, custom_less> pq;

	int m = (n + 1) / 2;
	pq.push(make_pair(m-1, n-m));

	while (!pq.empty())
	{
		pii nxt = pq.top(); k--;
		pq.pop();
		if (k == 0) return nxt;
		m = (nxt.first + 1) / 2;
		pq.push(make_pair(m - 1, nxt.first - m));
		m = (nxt.second + 1) / 2;
		pq.push(make_pair(m - 1, nxt.second - m));
	}
}


int main()
{
	int nt; cin >> nt;
	int t = 1;
	while (t <= nt)
	{
		int n, k; cin >> n >> k;
		pii res = solve(n, k);
		cout << "Case #" << t << ": ";
		cout << max(res.first, res.second) << ' ' << min(res.first, res.second) << '\n';
		t++;
	}

	return 0;
}

