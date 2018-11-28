#include <deque>
#include <vector>
#include <algorithm>
#include <iostream>

#include <map>
#include <set>
#include <math.h>

using namespace std;



void solve(int i0) {
	int hd, ad, hk, ak, b, d;
	cin >> hd >> ad >> hk >> ak >> b >> d;

	int attack_round = 100000000;
	for (int i = 0; i < 200; ++i) {
		int r;
		if (hk % (b*i+ad) == 0)
			r = hk/(b*i+ad);
		else
			r = hk/(b*i+ad)+1;

		//int r = (int)(ceil((hk+0.0) / (b*i+ad+0.0)));
		attack_round = min(attack_round, r+i);
	};


	int def_round = 100000000;

	for (int i = 0; i < 399; ++i) {
		//if (ak < i*d) break;

		int cure_rounds = 0;
		int debuff_rounds = i;
		int h = hd;
		int ak2 = ak;
		int remain = attack_round;

		int z = 0;
		while (debuff_rounds > 0) {
			int next = ak2-d;
			z++;
			if (cure_rounds > 10000) break;
			if (h <= next) {
				cure_rounds++;
				h = hd - ak2;
			}
			else {
				debuff_rounds --;
				ak2 -= d;
				if (ak2 <= 0) {
					ak2 = 0;
				}
				h -= ak2;
			};
		};

		if (cure_rounds >10000) continue;

		if (ak2 <= 0) {
			def_round = min(def_round, z);
		}
		else {
			while (remain > 0) {
				if (cure_rounds > 10000) break;
				z++;
				if (remain > 1 && h <= ak2) {
					// printf("%d %d %d %d\n", hd, h, ak2, i);
					cure_rounds++;
					h = hd-ak2;
				}
				else {
					remain--;
					h -= ak2;
				};
			};	
			if (cure_rounds > 10000) continue;

			def_round = min(def_round, z-attack_round);					
		}

		//printf("%d: %d\n", i, def_round);
	};

	//printf("ad=%d b=%d ar=%d dr=%d\n", ad, b, attack_round, def_round);

	if (attack_round+def_round >= 100000000)
		printf("Case #%d: IMPOSSIBLE\n", i0);
	else
		printf("Case #%d: %d\n", i0, attack_round+def_round);
};

int main() {
	//freopen("C.in", "r", stdin);

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out2", "w", stdout);

	int t;
	cin >> t;
	for (int i0=1; i0<=t; ++i0) {
		solve(i0);
	};

}