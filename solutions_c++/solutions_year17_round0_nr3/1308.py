#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <map>
#include <ctime>
#include <set>
using namespace std;

#pragma comment(linker, "/STACK:167772160")

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
typedef pair<ll, ll> pll;


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
		ll n, k;
		scanf("%I64d %I64d", &n, &k);
		ll lastLs, lastRs;
		map<ll, ll> m;
		m[n] = 1;
		while(k>0)
		{
			pll p = *m.rbegin();
			m.erase(p.first);
			lastLs = (p.first - 1) / 2;
			lastRs = p.first - 1 - (p.first - 1) / 2;
			m[lastLs] += p.second;
			m[lastRs] += p.second;
			k -= p.second;
		}
		printf("Case #%d: %I64d %I64d\n", tt + 1, max(lastLs, lastRs), min(lastLs, lastRs));
	}
}


int main()
{
	//gen();
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