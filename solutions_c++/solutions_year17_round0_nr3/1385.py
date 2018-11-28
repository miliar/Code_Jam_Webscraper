#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <cmath>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <limits.h>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <time.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:336777216")
using namespace std;

#define mp make_pair
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define szz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define ldb ldouble

typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;

int IT_MAX = 1 << 17;
const ll MOD = 1000000007;
const int INF = 1034567891;
const ll LL_INF = 1234567890123456789ll;
const db PI = acos(-1);
const db ERR = 1E-11;

pll aa(ll x, pll v, ll K) {
	if (x == 1) {
		if (v.second >= K) return pll(1, 0);
		else return pll(0, 0);
	}

	if (v.second >= K) return pll(x - x / 2, x / 2);
	if(v.first + v.second >= K) return pll((x - 1) - (x - 1) / 2, (x - 1) / 2);

	map <ll, ll> Mx;
	Mx[x - x / 2] += v.second;
	Mx[x / 2] += v.second;
	Mx[(x - 1) - (x - 1) / 2] += v.first;
	Mx[(x - 1) / 2] += v.first;
	assert(Mx.size() <= 2);

	auto it = Mx.begin();
	ll x2 = Mx.begin()->first;
	pll v2 = pll(Mx[x2], Mx[x2 + 1]);
	ll K2 = K - v.first - v.second;
	return aa(x2, v2, K2);
}
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		ll N, K;
		scanf("%lld %lld", &N, &K);

		pll rv = aa(N, pll(1, 0), K);
		printf("Case #%d: %lld %lld\n", tc, rv.first, rv.second);
	}
	return 0;
}