#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <limits.h>
#include <math.h>
#include <map>
#include <assert.h>
using namespace std;

#define ran(i, a, b) for ((i) = (a); (i) < (b); (i)++)
#define rep(i, a) ran ((i), 0, (a))
#define rep1(i, a) ran ((i), 1, (a)+1)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
#define _0 first
#define _1 second
#define _pb(x) push_back(x)
#define _mp(x, y) make_pair(x, y)
#if defined(SHIROKO1_LOCAL) && !defined(NDEBUG)
#define DEBUG(...) fprintf(stderr, "[DEBUG] " __VA_ARGS__)
#else
#define DEBUG(...) ((void)0)
#endif

ll solve(ll n, ll k)
{
	DEBUG("SOLVE %lli %lli\n", n, k);
	map<ll, ll> m;
	m[n] = 1;
	for (;;) {
		pair<ll, ll> x = *m.rbegin();
		DEBUG("POP %lli %lli\n", x._0, x._1);
		if (k <= x._1)
			return x._0-1;
		m.erase(x._0);
		if (x._0 >= 3) {
			m[(x._0-1)/2] += x._1;
			DEBUG("PUSH %lli += %lli\n", (x._0-1)/2, x._1);
		}
		if (x._0 >= 2) {
			m[(x._0)/2] += x._1;
			DEBUG("PUSH %lli += %lli\n", (x._0)/2, x._1);
		}
		k -= x._1;
	}
}

int main()
{
	int i, t;
	ll n, k;
	cin >> t;
	rep1 (i, t) {
		cin >> n >> k;
		ll x = solve(n, k);
		printf("Case #%i: %lli %lli\n", i, (x+1)/2, x/2);
	}
	return 0;
}
