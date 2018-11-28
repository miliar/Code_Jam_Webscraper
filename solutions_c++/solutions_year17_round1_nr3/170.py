#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

struct State {
	short Hd, Ad, Hk, Ak;
	State() {}
	State(short Hd, short Ad, short Hk, short Ak) : Hd(Hd), Ad(Ad), Hk(Hk), Ak(Ak) {}
}q[110000005];

int d[105][105][105][105], hd, tl;
void addState(short x, short y, short z, short w, short td) {
	if (d[x][y][z][w] == -1) {
		d[x][y][z][w] = td + 1;
		q[++tl] = State(x, y, z, w);
	}
}

int Hd, Ad, Hk, Ak, B, D;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int full_Hd = Hd;
		memset(d, -1, sizeof d);
		hd = 0, tl = 0;
		q[tl = 1] = State(Hd, Ad, Hk, Ak);
		d[Hd][Ad][Hk][Ak] = 0;
		int ans = -1;
		while (hd < tl) {
			State cur = q[++hd];
			Hd = cur.Hd, Ad = cur.Ad;
			Hk = cur.Hk, Ak = cur.Ak;
			int td = d[Hd][Ad][Hk][Ak];
			if (Hk <= Ad) {
				ans = td + 1;
				break ;
			}
			if (Hd > Ak) addState(Hd - Ak, Ad, Hk - Ad, Ak, td);
			if (Hd > Ak) addState(Hd - Ak, min(100, Ad + B), Hk, Ak, td);
			if (full_Hd > Ak) addState(full_Hd - Ak, Ad, Hk, Ak, td);
			if (Hd > max(0, Ak - D)) addState(Hd - max(0, Ak - D), Ad, Hk, max(0, Ak - D), td);
		}
		printf("Case #%d: ", TK);
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else cout << ans << endl;
	}
	return 0;
}