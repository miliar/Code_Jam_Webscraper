#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
int sp[105][105][105][105];
struct State {
	int hd, ad, hk, ak;
};
queue<State> Q;
bool relax(int hd, int ad, int hk, int ak, int v) {
	if (hk <= 0) return true;
	if (ak < 0) ak = 0;
	if (ad > 100) ad = 100;
	hd -= ak;
	if (hd <= 0) return false;
	if (sp[hd][ad][hk][ak] != -1) return false;
	Q.push({hd, ad, hk, ak});
	sp[hd][ad][hk][ak] = v + 1;
	return false;
}
void solve(int cn) {
	int hd, ad, hk, ak, B, D;
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &B, &D);
	memset(sp, -1, sizeof(sp));
	while (!Q.empty()) Q.pop();
	Q.push({hd, ad, hk, ak});
	sp[hd][ad][hk][ak] = 0;
	while (!Q.empty()) {
		State x = Q.front();
		Q.pop();
		int d = sp[x.hd][x.ad][x.hk][x.ak];
		if (relax(x.hd, x.ad, x.hk - x.ad, x.ak, d)
			|| relax(x.hd, x.ad + B, x.hk, x.ak, d)
			|| relax(hd, x.ad, x.hk, x.ak, d)
			|| relax(x.hd, x.ad, x.hk, x.ak - D, d)) {
			printf("Case #%d: %d\n", cn, d + 1);
			return;
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", cn);
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		solve(cn);
	}
}

