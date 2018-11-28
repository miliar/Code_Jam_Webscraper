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

map<int, int> memo[5];

const int inf = 1000000;
int n, p;
int g[105];

struct state
{
	int cnt[4] = { 0 };
	int get(int k) const
	{
		return (((cnt[0] * 100 + cnt[1]) * 100 + cnt[2]) * 100 + cnt[3]) * 4 + k;
	}
};

int go(state s, int tot, int k)
{
	if (tot == 0) return 0;
	int t = k > 0;
	int key = s.get(k);
	auto it = memo[p].find(key);
	if (it != memo[p].end()) return it->second;
	int &res = memo[p][s.get(k)];
	res = inf;
	for (int i = 0; i < p; i++) if (s.cnt[i])
	{
		s.cnt[i]--;
		res = min(res, t + go(s, tot - 1, (k - i + p) % p));
		s.cnt[i]++;
	}
	return res;
}

void solvecase()
{
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++) scanf("%d", &g[i]);
	state s;
	for (int i = 0; i < n; i++) s.cnt[g[i] % p]++;
	int res = n - go(s, n, 0);
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

#define problem_letter "A"
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