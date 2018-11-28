#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define FORD(i,a,b) for(int i=int(a);i>=int(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
typedef long long int64;

char cake[30][30];
int r, c;

int64 ceil(int64 a, int64 b) {
	return a / b + (bool) (a % b);
}

int minn(int a, int b) {
	if (a < 0) return b;
	else return min(a, b);
}

int main() {
	int tN;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		int hd, ad, hk, ak, b, d;
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		int minBA = 1e9;
		FOR(cntB, 0, 1e6) {
			minBA = min((int64) minBA, ceil(hk, ad + 1LL*cntB*b) + cntB);
		}
		// printf("minBA = %d, ", minBA);
		int ans = -1;
		int numTurn = 0;
		int HP = hd;
		FOR(cntD, 0, 1e9) {
			if (cntD > 0 && d == 0) break;
			if (ak == 0) {
				ans = minn(ans, numTurn + minBA);
				break;
			}
			int cycle = (hd-1) / ak;
			int b4Heal = (HP-1) / ak;
			// printf("cntD = %d, cycle = %d, b4Heal = %d\n", cntD, cycle, b4Heal);
			if (b4Heal+1 >= minBA) ans = minn(ans, numTurn + minBA);
			else if (cycle > 1) {
				int cntHeal = ceil(minBA - b4Heal - 1, cycle-1);
				ans = minn(ans, numTurn + minBA + cntHeal);
				// printf("cntD = %d, res = %d\n", cntD, numTurn + minBA + cntHeal);
			}
			++numTurn;
			ak = max(0, ak - d);
			HP -= ak;
			if (HP <= 0) {
				++numTurn;
				HP = hd - (ak+d) - ak;
				if (HP <= 0) break;
			}
		}
		printf("Case #%d: ", cN);
		if (ans >= 0) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}
