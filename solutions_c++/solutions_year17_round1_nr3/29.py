#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

const i64 threshold = 40000;

int T;
i64 Hd, Ad, Hk, Ak, B, D;

i64 rup(i64 a, i64 b)
{
	return a / b + (a % b ? 1 : 0);
}

i64 cost(i64 turn, i64 maxhp, i64 curhp, i64 enemy)
{
	// TODO
	int ret = 0;
	for (int i = 0; i < 1000; ++i) {
		if (turn == 1) {
			++ret;
			return ret;
		}
		if (curhp <= enemy) {
			++ret;
			curhp = maxhp - enemy;
			continue;
		}
		--turn;
		curhp -= enemy;
		++ret;
	}
	return 1LL << 60LL;
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%lld%lld%lld%lld%lld%lld", &Hd, &Ad, &Hk, &Ak, &B, &D);

		i64 nCA = 1LL << 60LL;
		i64 ans = 1LL << 60LL;

		for (int c = 0; c <= threshold; ++c) {
			i64 att = Ad + B * c;
			i64 req = rup(Hk, att);
			nCA = min(nCA, c + req);
		}
		if (B > 0) {
			for (int a = 1; a <= threshold; ++a) {
				i64 reqatt = rup(Hk, a);
				i64 reqbuff = (reqatt >= Ad ? rup(reqatt - Ad, B) : 0);
				nCA = min(nCA, reqbuff + a);
			}
		}
		// TODO
		i64 curhp = Hd;
		int add = 0;
		for (int d = 0; d <= 105; ++d) {
			ans = min(ans, add + cost(nCA, Hd, curhp, Ak));
			if (curhp <= Ak - D) {
				++add;
				curhp = Hd - Ak;
				if (curhp <= Ak - D) break;
			}
			++add;
			Ak = max(0LL, Ak - D);
			curhp -= Ak;
		}

		if (ans > 1LL << 40LL) {
			printf("Case #%lld: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%lld: %lld\n", t, ans);
		}
	}

	return 0;
}
