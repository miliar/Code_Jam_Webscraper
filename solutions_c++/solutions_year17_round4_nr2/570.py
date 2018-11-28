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

void init()
{

}

const int maxn = 1005;

int n, c, m;
int b[maxn], p[maxn];

void solvecase()
{
	scanf("%d%d%d", &n, &c, &m);
	vector<vector<int> > seats(c);
	vector<map<int, int> > cnt(c);
	vector<int> sums(n+1);
	for (int i = 0; i < m; i++)
	{
		scanf("%d%d", &p[i], &b[i]);
		seats[b[i]-1].push_back(p[i]);
		cnt[b[i] - 1][p[i]]++;
		sums[p[i]]++;
	}
	auto ret = [](int a, int b)
	{
		printf("%d %d", a, b);
	};
	int t = 0;
	for (auto &xxx : seats) t = max(t, (int)xxx.size());
	//int t2 = sums[1];
	//t = max(t, t2);

	int l = t - 1, r = m;
	while (l + 1 < r)
	{
		int q = (l + r) / 2;
		bool ok = true;
		int fdfdf = 0;
		for (int i = 1; i <= n; i++)
		{
			fdfdf += sums[i];
			if (fdfdf > q * i) { ok = false; break; }
		}
		if (ok) r = q; else l = q;
	}
	int res2 = 0;
	for (int i = 1; i <= n; i++) res2 += max(0, sums[i] - r);
	ret(r, res2);
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

#define problem_letter "B"
//#define fname "test"
//#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}