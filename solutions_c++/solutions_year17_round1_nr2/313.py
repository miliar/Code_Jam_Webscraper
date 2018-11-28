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

int n, p;
int r[55];
//int a[55][55];
vector<pair<int, int>> lims[55];

inline int rup(int a, int b) {
	return (a + b - 1) / b;
}

void solvecase()
{
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++) scanf("%d", &r[i]);
	for (int i = 0; i < n; i++)
	{
		lims[i].clear();
		for (int j = 0; j < p; j++)
		{
			int a;
			scanf("%d", &a);
			int mi = rup(a * 10, (11 * r[i]));
			int ma = a * 10 / (9 * r[i]);
			if (mi <= ma && mi > 0) lims[i].push_back({ mi, ma });
		}
		sort(ALL(lims[i]));
	}
	int res = 0;
	while (true)
	{
		int mi = 0, ma = 100000000;
		bool end = false;
		pair<int, int> maxp(0, 0);
		int max_idx = -1;
		for (int i = 0; i < n; i++)
		{
			if (lims[i].empty()) {
				end = true;
				break;
			}
			mi = max(mi, lims[i].back().first);
			ma = min(ma, lims[i].back().second);
			if (lims[i].back() > maxp)
			{
				maxp = lims[i].back();
				max_idx = i;
			}
		}
		if (end) break;
		if (mi <= ma)
		{
			res++;
			for (int i = 0; i < n; i++) lims[i].pop_back();
		}
		else
		{
			lims[max_idx].pop_back();
		}
	}
	printf("%d", res);
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
//#define fname problem_letter
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