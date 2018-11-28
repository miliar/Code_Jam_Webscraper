#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <deque>

using namespace std;

const int INF = 0x7fffffff;

int Hd, Ad, Hk, Ak, B, D;
int solve(int d, int b) {
	int hd = Hd, ad = Ad, hk = Hk, ak = Ak;
	int turn = 0;
	while(d--) {
		int nk = max(0, ak - D);
		if(hd - nk <= 0) {
			turn++; hd = Hd - ak;
			if(hd - nk <= 0) return INF;
		}
		turn++;
		ak = nk;
		hd -= ak;
		if(turn > 20000) return INF;
	}
	while(b--) {
		if(hd - ak <= 0) {
			turn++; hd = Hd - ak;
			if(hd - ak <= 0) return INF;
		}
		turn++;
		ad += B;
		hd -= ak;
		if(turn > 20000) return INF;
	}
	while(hk > 0) {
		if(hk - ad <= 0) {
			turn++;
			break;
		}
		if(hd - ak <= 0) {
			turn++; hd = Hd - ak;
			if(hd - ak <= 0) return INF;
		}
		turn++;
		hk -= ad;
		hd -= ak;
		if(turn > 20000) return INF;
	}
	return turn;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++) {
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int ans = INF;
		for(int d=0; d<=100; d++) {
			for(int b=0; b<=100; b++) {
				ans = min(ans, solve(d, b));
				if(B == 0) break;
			}
			if(D == 0) break;
		}
		if(ans == INF) printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}