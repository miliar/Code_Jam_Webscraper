#include <bits/stdc++.h>
using namespace std;

int T;
int n, m;

int hd, ad, hk, ak, b, d;

int doit(int debuff, int buff) {
	int hdt = hd;
	int adt = ad;
	int hkt = hk;
	int akt = ak;

	int res = 0;

	for (int i = 0; i < debuff; i++) {
		res++;
		akt -= d;
		if (akt < 0)
			akt = 0;
		hdt -= akt;
		while (hdt < 0) {

		}
	}

	while (1) {
		res++;

		if (hdt <= 0)
			return 1 << 30;
		if (hkt <= 0)
			return res;
	}
}

int main() {
	scanf("%d", &T);

	int ansa = 0;
	for (int t = 1; t <= T; t++) {
		scanf("%d", &hd);
		scanf("%d", &ad);
		scanf("%d", &hk);
		scanf("%d", &ak);
		scanf("%d", &b);
		scanf("%d", &d);

		int ansa = 1 << 30;
		for (int debuff = 0; debuff <= 100; debuff++) {
			for (int buff = 0; buff <= 100; buff++) {
				ansa = min(ansa, doit(debuff, buff));
			}
		}

		printf("Case #%d: ", t);
		if (ansa == 1 << 30) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ansa);
		}
	}

	return 0;
}
