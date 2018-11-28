#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
typedef long long LL;
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
const int inf = 2100000000;

void init()
{

}

int hd, ad, hk, ak, b, d;

int calc2(int ak, int ad, int hp)
{
	if (ak >= hd && ad < hk)
		return inf;
	if (2 * ak >= hd && 2 * ad < hk)
		return inf;
	int res = 0;
	int ehp = hk;
	while (true)
	{
		if (ehp <= ad) return res + 1;
		if (hp <= ak)
		{
			hp = hd;
			if (hp - ak <= ak) return inf;
		}
		else
			ehp -= ad;
		hp -= ak;
		res++;
	}
	return inf;
}

int calc(int ak, int hp)
{
	int extra_moves = 0;
	int ad2 = ad;
	int last = inf;
	for (int buff = 0; buff <= 100; buff++)
	{
		int t = calc2(ak, ad2, hp) + extra_moves;
		//if (t > last) return last;
		last = min(t, last);
		if (b == 0) break;
		ad2 += b;
		extra_moves++;
		if (hp <= ak)
		{
			extra_moves++;
			hp = hd - ak;
		}
		hp -= ak;
		if (hp <= 0) break;
	}
	return last;
}

void solvecase()
{
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
	int last = inf;
	int ak2 = ak;
	int extra_moves = 0;
	int curhp = hd;
	for (int debuff = 0; debuff <= 100; debuff++)
	{
		int t = calc(ak2, curhp) + extra_moves;
		//if (t > last) break;
		last = min(t, last);
		if (d == 0) break;
		int oldak = ak2;
		ak2 = max(0, ak2 - d);
		extra_moves++;
		if (curhp <= ak2) {
			extra_moves++; curhp = hd - oldak;
		}
		curhp -= ak2;
		if (curhp <= 0) break;
	}
	if (last == inf)
	{
		printf("IMPOSSIBLE");
		return;
	}
	printf("%d", last);
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "C"
//#define fname problem_letter
//#define fname problem_letter "-small-attempt0"
#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
//#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}