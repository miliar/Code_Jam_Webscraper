#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <set>
#include <cassert>
#include <map>
using namespace std;

#pragma comment(linker, "/STACK:567772160")

#define mp(x, y) make_pair(x, y)
#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d %d", &x, &y)
#define scl(x) scanf("%I64d", &x)
#define scl2(x, y) scanf("%I64d %I64d", &x, &y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define all(x) x.begin(), x.end()
#define pr(x) printf("%d ", x)

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

const long double EPS = 1e-8;
const long double PI = atan((long double)1) * 4;
const int inf = (int)1e9;
const ll INF = (ll)1e18;

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		int d, n;
		sc2(d, n);
		vector<int> k(n), s(n);
		vector<double> h(n);
		forn(i, 0, n) {
			sc2(k[i], s[i]);
			h[i] = (double)(d-k[i])/s[i];
		}
		double mx = *max_element(all(h));
		double ans = d / mx;
		printf("Case #%d: %.10lf\n", tt + 1, ans);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
#ifndef ONLINE_JUDGE
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}