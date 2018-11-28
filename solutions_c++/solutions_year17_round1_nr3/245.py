#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;


struct State
{
	int hd, ad, hk, ak;

	State() : hd(), ad(), hk(), ak() {}

	State(int _hd, int _ad, int _hk, int _ak) :
		hd(_hd), ad(_ad), hk(_hk), ak(_ak) {}

	bool operator < (const State &A) const
	{
		if (hd != A.hd) return hd < A.hd;
		if (ad != A.ad) return ad < A.ad;
		if (hk != A.hk) return hk < A.hk;
		if (ak != A.ak) return ak < A.ak;
		return false;
	}
	
	void eprint()
	{
		eprintf("%d %d %d %d\n", hd, ad, hk, ak);
	}
};

const int INF = (int) 1e9;
int max_hd;
int b, d;
map <State, int> ans;

int solve(State S)
{
	if (ans.count(S) ) return ans[S];
	ans[S] = INF;
	if (S.hd <= 0) return ans[S];
	if (S.hk <= S.ad) return ans[S] = 1;

	int x = INF;
	x = min(x, solve(State(S.hd - S.ak, S.ad + b, S.hk, S.ak) ) + 1);
	x = min(x, solve(State(S.hd - max(S.ak - d, 0), S.ad, S.hk, max(0, S.ak - d) ) ) + 1);
	x = min(x, solve(State(S.hd - S.ak, S.ad, S.hk - S.ad, S.ak) ) + 1);
	x = min(x, solve(State(max_hd - S.ak, S.ad, S.hk, S.ak) ) + 1);

	return ans[S] = x;
}

void solve()
{
	ans.clear();

	int hd, ad, hk, ak;
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
	max_hd = hd;

	int answer = solve(State(hd, ad, hk, ak));
	if (answer == INF)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", answer);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


