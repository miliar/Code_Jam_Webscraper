#include <bits/stdc++.h>

using namespace std;

int Hd, Ad, Hk, Ak, B, D;

const int INF = 1e9;

int dp[101][201][101][101];

int calc(int hd, int ad, int hk, int ak) {
	if (hk <= 0) return 0;
	if (hd <= 0) return INF;
	if (ad >= hk) return 1;
	int &ret = dp[hd][ad][hk][ak];
	if (ret != -1) return ret;
	ret = min(INF, 1 + calc(hd - ak, ad, hk - ad, ak)); // attack
	if (B)
		ret = min(ret, 1 + calc(hd - ak, ad + B, hk, ak)); // buff
	if (hd < Hd - ak)
		ret = min(ret, calc(Hd - ak, ad, hk, ak) + 1); // cure
	if (D && ak) {
		int x = max(ak - D, 0);
		ret = min(ret, calc(hd - x, ad, hk, x) + 1); // debuff
	}
	return ret;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		memset(dp, -1, sizeof dp);
		printf("Case #%d: ", tc);
		if (calc(Hd, Ad, Hk, Ak) != INF) {
			printf("%d\n", calc(Hd, Ad, Hk, Ak));
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}