#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <numeric>
#include <queue>
#include <random>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TASK "connect"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 7;
const int inf = (int)1e9 + 7;

int solve() {
	int T;
	scanf("%d\n", &T);
	for (int it = 1; it <= T; ++it) {
		ll cnt = 0;
		ll n, k;
		scanf("%lld %lld", &n, &k);
		set<ll> S;
		map<ll, ll> M;
		S.insert(n);
		M[n] = 1;
		while (1) {
			ll K = *S.rbegin();
			S.erase(K);
			if (cnt + M[K] >= k) {
				printf("Case #%d: %lld %lld\n", it, K / 2, K - K / 2 - 1);
				break;
			}
			cnt += M[K];
			M[K / 2] += M[K];
			M[K - K / 2 - 1] += M[K];
			S.insert(K / 2);
			S.insert(K - K / 2 - 1);
		}
	}
	return 0;
}