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

int main() {
	freopen("C-small-attempt5.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		ll Hd, Ad, Hk, Ak, B, D, i;
		scanf("%lld %lld %lld %lld %lld %lld", &Hd, &Ad, &Hk, &Ak, &B, &D);

		ll at = LL_INF;
		for (i = 0; i <= 80000; i++) {
			ll t1 = Hk;
			ll t2 = Ad + B * i;
			at = min(at, i + (t1 + t2 - 1) / t2);
		}

		printf("Case #%d: ", tc);
		if (at == 1) {
			printf("1\n");
			continue;
		}
		if (Ak - D >= Hd) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (at == 2 && Hd > Ak) {
			printf("2\n");
			continue;
		}

		ll ans = LL_INF;
		if (2 * Ak < Hd) {
			ll x = (Hd + Ak - 1) / Ak;
			if (at <= x) {
				printf("%lld\n", at);
				continue;
			}

			ll lat = at - x + 1;

			if (x - 2 == 1) ans = min(ans, x + 2 * lat - 2);
			else {
				ll v1 = lat / (x - 2);
				ll v2 = lat % (x - 2);

				ll a = v1*(x - 1) + v2;
				if (v1 >= 1 && v2 <= 1) a--;
				ans = min(ans, a + x);
			}
		}
		if (D == 0) {
			if (ans == LL_INF) printf("IMPOSSIBLE\n");
			else printf("%lld\n", ans);
			continue;
		}

		ll curh = Hd, turn = 0;
		for (i = 1; i <= 300000; i++) {
			if (curh <= Ak - D*i) {
				turn++;
				curh = Hd - Ak + D*(i - 1);
				if (curh <= Ak - D*i) break;
			}
			turn++;
			curh -= Ak - D*i;

			ll cura = Ak - D*i;
			if (cura <= 0) {
				ans = min(ans, turn + at);
				break;
			}

			if ((curh + cura - 1) / cura >= at) {
				ans = min(ans, turn + at);
				break;
			}

			if (cura * 2 >= Hd) continue;

			ll lat = at - (curh - 1) / cura;
			ll tturn = turn + (curh - 1) / cura + 1;
			ll x = (Hd - 1) / cura - 1;

			if (x == 1) ans = min(ans, tturn + lat * 2 - 2);
			else {
				ll v1 = lat / x;
				ll v2 = lat % x;
				ll a = v1*(x + 1) + v2;
				if (v1 >= 1 && v2 <= 1) a--;

				ans = min(ans, tturn + a);
			}
		}
		if (ans == LL_INF) printf("IMPOSSIBLE\n");
		else printf("%lld\n", ans);
	}
	return 0;
}