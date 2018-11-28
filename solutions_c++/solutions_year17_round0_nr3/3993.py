#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <assert.h>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <math.h>
#include <bitset>

#pragma comment(linker, "/STACK:256000000")

using namespace std;

typedef long long int ll;
typedef long double ld;

const int INF = 1000 * 1000 * 1000 + 21;
const ll LLINF = (1ll << 60) + 5;
const int MOD = 1000 * 1000 * 1000 + 7;

struct point
{
	ll l;
	ll r;
};

bool operator<(const point &a, const point &b)
{
	return (a.r - a.l < b.r - b.l) || (a.r - a.l == b.r - b.l && a.l < b.l);
}

ll n, k;
multiset<point> gg;

int main()
{
#ifdef CH_EGOR
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	//freopen("", "r", stdin);
	//freopen("", "w", stdout);
#endif 	

	int t;
	scanf("%d", &t);
	for (int it = 1; it <= t; ++it)
	{
		scanf("%lld%lld", &n, &k);
		gg.clear();
		gg.insert({0, n + 1});
		for (int i = 0; i < k - 1; ++i)
		{
			auto kek = gg.end();
			--kek;
			point ff = *kek;
			gg.erase(kek);
			gg.insert({ff.l, (ff.r + ff.l) / 2});
			gg.insert({(ff.r + ff.l) / 2, ff.r});
		}

		auto kek = gg.end();
		--kek;
		point ff = *kek;
		ll tt = (ff.r + ff.l) / 2;
		ll l = ff.r - tt - 1;
		ll r = tt - ff.l - 1;
		printf("Case #%d: %lld %lld\n", it, l, r);
	}

	return 0;
}

