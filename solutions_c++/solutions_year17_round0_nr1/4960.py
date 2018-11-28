//
// a.cpp
// google codejam qualifier
//
// Copyright (c) 2015-2017 mikewaneyindustries
//

#include "io.h"

/***************************** START COPY ************************************/

#include "bits/stdc++.h"
using namespace std;

#ifdef LOCAL
struct dbger {
	template<typename T> dbger& operator,(const T& v) { cerr << v << " "; return *this; }
} dbg;
#define debug(...) { cerr << #__VA_ARGS__ << " : "; dbg, __VA_ARGS__; cerr << '\n'; }
#define file "a"
#define REOPEN() freopen(file".in", "r", stdin); freopen(file".out", "w", stdout); freopen("test.err", "w", stderr);
struct file_stdio { file_stdio() { REOPEN() }; } file_stdio;
struct timer { clock_t t = clock();  
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

bool is_good(string& s)
{
	for (auto ch : s) if (ch == '-') return false;
	return true;
}

int solve(string& s, int b, int e, int k)
{

	if (e - b + 1 < k) return 0;
	int nflips = 0;
	if (s[b] == '-') {
		nflips++;
		for (int i = 0; i < k; ++i) s[b+i] = (s[b+i] == '-') ? '+' : '-';
	}
	if (s[e] == '-') {
		nflips++;
		for (int i = 0; i < k; ++i) s[e-i] = (s[e-i] == '-') ? '+' : '-';
	}
	return nflips + solve(s, b+1, e-1, k);
}

int main()
{
	int nt; cin >> nt;
	int t = 1;
	while (t <= nt)
	{
		string s; int k; cin >> s >> k;
		int n = solve(s, 0, s.length()-1, k);
		debug(s);
		cout << "Case #" << t << ": ";
		if (is_good(s)) cout << n << '\n';
		else cout << "IMPOSSIBLE\n";
		t++;
	}

	return 0;
}

/****************************** END COPY *************************************/
