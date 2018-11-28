#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
using namespace std;

const int inf = (int)1e9 + 10;
struct info {
	int hd, ad, hk, ak;
	info() {
		hd = ad = hk = ak = 0;
	}
	info(int _hd, int _ad, int _hk, int _ak) {
		hd = _hd;
		ad = _ad;
		hk = _hk;
		ak = _ak;
	}
	bool operator < (const info& nxt) const{
		if (hd != nxt.hd) return hd < nxt.hd;
		if (ad != nxt.ad) return ad < nxt.ad;
		if (hk != nxt.hk) return hk < nxt.hk;
		if (ak != nxt.ak) return ak < nxt.ak;
		return false;
	}
};

int Hd, Hk, Ad, Ak, B, D;
map<info, int> hashdp;

int DP(int hd, int ad, int hk, int ak) {
	if (hk <= 0) {
		return 0;
	}
	if (hd <= 0) {
		return inf;
	}
	if (hashdp.count(info(hd, ad, hk, ak)) > 0) {
		return hashdp[info(hd, ad, hk, ak)];
	}
	int &ans = hashdp[info(hd, ad, hk, ak)];
	ans = inf;
	//printf("(%d,%d,%d,%d) nowmp=%d\n", hd, ad, hk, ak, hashdp[info(hd, ad, hk, ak)]);

	// attack 
	info nxt = info(hd, ad, hk - ad, ak);
	if (nxt.hk > 0) {
		nxt.hd -= nxt.ak;
	}
	ans = min(ans, DP(nxt.hd, nxt.ad, nxt.hk, nxt.ak) + 1);

	nxt = info(hd, min(100, ad + B), hk, ak);
	if (nxt.hk > 0) {
		nxt.hd -= nxt.ak;
	}
	ans = min(ans, DP(nxt.hd, nxt.ad, nxt.hk, nxt.ak) + 1);

	nxt = info(Hd, ad, hk, ak);
	if (nxt.hk > 0) {
		nxt.hd -= nxt.ak;
	}
	ans = min(ans, DP(nxt.hd, nxt.ad, nxt.hk, nxt.ak) + 1);

	nxt = info(hd, ad, hk, max(0, ak - D));
	if (nxt.hk > 0) {
		nxt.hd -= nxt.ak;
	}
	ans = min(ans, DP(nxt.hd, nxt.ad, nxt.hk, nxt.ak) + 1);
	//printf("(%d,%d,%d,%d) nowmp=%d\n", hd, ad, hk, ak, hashdp[info(hd, ad, hk, ak)]);

	return ans;
}

void solve(int testcase) {
	hashdp.clear();
	scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
	int ans = DP(Hd, Ad, Hk, Ak);
	if (ans > (int)1e7) 
		printf("Case #%d: IMPOSSIBLE\n", testcase);
	else printf("Case #%d: %d\n", testcase, ans);
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int t = 1; t <= tst; t ++) {
		solve(t);
	}
	return 0;
}
