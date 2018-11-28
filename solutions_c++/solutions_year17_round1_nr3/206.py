#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

int hd, ad, hk, ak;
int b, d;

const int inf = 1e9;

int model(int buffs, int decreases) {
	int cur_h = hd;
	int cur_a = ad;
	int his_h = hk;
	int his_a = ak;
	int turns = 0;
	while (1) {
		bool made_turn = 0;
		turns++;
		if (his_h <= cur_a) return turns;
		int nxt_his_a = his_a;
		if (decreases) {
			nxt_his_a = his_a - d;
		}
		if (cur_h - nxt_his_a <= 0) { //curing
			cur_h = hd;
			made_turn = 1;
		}
		if (!made_turn && decreases) { //decreasing
			decreases--;
			his_a -= d;
			made_turn = 1;
		}
		if (!made_turn && buffs) { //buffing
			cur_a += b;
			made_turn = 1;
			buffs--;
		}
		if (!made_turn) { //attacking
			his_h -= cur_a;
			made_turn = 1;
		}
		cur_h -= his_a;
		if (turns > 1e5) return inf;
	}
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int q = 0; q < T; q++) {
		cin >> hd >> ad >> hk >> ak;
		cin >> b >> d;
		int ans = inf;
		for (int i = 0; i <= hk; i++) { // buffs
			for (int j = 0; j <= ak; j++) { // decreases
				ans = min(ans, model(i, j));
			}
		}
		printf("Case #%d: ", q + 1);
		if (ans == inf) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}