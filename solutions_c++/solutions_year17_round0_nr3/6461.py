/*
 * GCJ 2017 - Qual
 * Problem C. Bathroom stalls
 */
 
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <map>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

pair<ll, ll> solve(ll n, ll k)
{
	map<ll, ll> have;
	have[n] = 1;
	while (true) {
		auto last = have.rbegin();
		ll size = last->first, count = last->second;
		ll leftPart = (size - 1) / 2;
		ll rightPart = size - 1 - leftPart;
		if (count < k) {
			have[leftPart] += count;
			have[rightPart] += count;
			have.erase(size);
			k -= count;
		} else {
			return make_pair(rightPart, leftPart);
		}
	}
}

int main(void)
{
	int T;
	//freopen("/home/vesko/c.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		ll n, k;
		scanf("%lld%lld", &n, &k);
		pair<ll, ll> result = solve(n, k);
		printf("%lld %lld\n", result.first, result.second);
	}
	return 0;
}
