#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

int Kiriage(int a, int b)
{
	return (a + b - 1) / b;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int Hd, Ad, Hk, Ak, B, D;
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int kougeki = 10000000;
		if (B == 0) {
			kougeki = Kiriage(Hk, Ad);
		} else {
			/*
			double l = 0, r = Kiriage(Hk, B) + 1;
			while (true) {
				double x0 = (l * 2 + r) / 3;
				double x1 = (l + r * 2) / 3;
				double y0 = Hk / (Ad + x0 * B) + x0;
				double y1 = Hk / (Ad + x1 * B) + x1;
				if (y0 > y1) {
					l = x0;
				} else {
					r = x1;
				}
				if (r - l < 0.9) {
					break;
				}
			}
			kougeki = Kiriage(Hk, (Ad + (int)r * B)) + (int)r;
			*/
			for (int i = 0; i <= 100; i++) {
				kougeki = min(kougeki, Kiriage(Hk, Ad + i * B) + i);
			}
		}
		int ret = 10000000;
		if (kougeki == 1) {
			ret = 1;
		} else if (kougeki == 2 && Hd > Ak) {
			ret = 2;
		} else {
			for (int i = 0; i <= 100; i++) {
				int curHd = Hd;
				int curAd = Ad;
				int curHk = Hk;
				int curAk = Ak;
				int debuff = 0;
				int kou = 0;
				int j = 0;
				for (; j < 1000; j++) {
					if (debuff < i) {
						if (curHd <= curAk - D) {
							curHd = Hd;
						} else {
							debuff++;
							curAk -= D;
						}
						curHd -= curAk;
					} else {
						if (kou == kougeki - 1) {
							break;
						} else if (curHd <= curAk) {
							curHd = Hd;
						} else {
							kou++;
						}
						curHd -= curAk;
					}
				}
				ret = min(ret, j + 1);
				/*
				int kaku;
				if (Ak - D * i <= 0) {
					kaku = 100000000;
				} else {
					kaku = Kiriage(Hd, Ak - D * i);
				}
				if (kaku <= 2) {
					continue;
				}
				ret = min(ret, kougeki + (kougeki - 3) / (kaku - 2) + i);
				*/
			}
		}
		if (ret >= 1000) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%d: %d\n", t, ret);
		}
	}
	return 0;
}
