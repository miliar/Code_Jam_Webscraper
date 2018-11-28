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

int n, m;
char a[30][30];

void solvecase()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) scanf("%s", a[i]);
	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < m; j++)
			if (a[i][j] == '?' && a[i][j - 1] != '?') a[i][j] = a[i][j - 1];
		for (int j = m - 2; j >= 0; j--)
			if (a[i][j] == '?' && a[i][j + 1] != '?') a[i][j] = a[i][j + 1];
	}
	for (int j = 0; j < m; j++)
	{
		for (int i = 1; i < n; i++)
			if (a[i][j] == '?' && a[i - 1][j] != '?') a[i][j] = a[i - 1][j];
		for (int i = n - 2; i >= 0; i--)
			if (a[i][j] == '?' && a[i + 1][j] != '?') a[i][j] = a[i + 1][j];
	}
	for (int i = 0; i < n; i++) printf("\n%s", a[i]);
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

#define problem_letter "A"
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