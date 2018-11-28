#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char r[1111];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		int i, j, R, O, Y, G, B, V, X, rn;
		scanf("%*d%d%d%d%d%d%d", &R, &O, &Y, &G, &B, &V);
		//printf("%d %d %d %d %d %d\n", R, O, Y, G, B, V);
		R -= G;
		Y -= V;
		B -= O;
		if (R < 0 || Y < 0 || B < 0 || R > Y + B || Y > R + B || B > R + Y) {
			printf("Case #%d: IMPOSSIBLE\n", T);
			continue;
		}
		rn = 0;
		if (R >= Y && R >= B) {
			X = Y + B - R;
			for (i = 0; i < Y - X; i++) {
				r[rn++] = 'R';
				r[rn++] = 'Y';
			}
			for (i = 0; i < B - X; i++) {
				r[rn++] = 'R';
				r[rn++] = 'B';
			}
			for (i = 0; i < X; i++) {
				r[rn++] = 'R';
				r[rn++] = 'Y';
				r[rn++] = 'B';
			}
		}
		else if (Y >= R && Y >= B) {
			X = R + B - Y;
			for (i = 0; i < R - X; i++) {
				r[rn++] = 'Y';
				r[rn++] = 'R';
			}
			for (i = 0; i < B - X; i++) {
				r[rn++] = 'Y';
				r[rn++] = 'B';
			}
			for (i = 0; i < X; i++) {
				r[rn++] = 'Y';
				r[rn++] = 'R';
				r[rn++] = 'B';
			}
		}
		else {
			X = R + Y - B;
			for (i = 0; i < R - X; i++) {
				r[rn++] = 'B';
				r[rn++] = 'R';
			}
			for (i = 0; i < Y - X; i++) {
				r[rn++] = 'B';
				r[rn++] = 'Y';
			}
			for (i = 0; i < X; i++) {
				r[rn++] = 'B';
				r[rn++] = 'R';
				r[rn++] = 'Y';
			}
		}
		if (G) {
			for (i = 0; i < rn; i++) if (r[i] == 'R') break;
			memmove(r + i + G + G, r + i, rn - i);
			rn += G + G;
			while (G--) {
				r[i++] = 'R';
				r[i++] = 'G';
			}
		}
		if (V) {
			for (i = 0; i < rn; i++) if (r[i] == 'Y') break;
			memmove(r + i + V + V, r + i, rn - i);
			rn += V + V;
			while (V--) {
				r[i++] = 'Y';
				r[i++] = 'V';
			}
		}
		if (O) {
			for (i = 0; i < rn; i++) if (r[i] == 'B') break;
			memmove(r + i + O + O, r + i, rn - i);
			rn += O + O;
			while (O--) {
				r[i++] = 'B';
				r[i++] = 'O';
			}
		}
		r[rn] = r[0];
		for (i = 0; i < rn; i++) {
			if ((r[i] == 'R' || r[i] == 'O' || r[i] == 'V') && (r[i + 1] == 'R' || r[i + 1] == 'O' || r[i + 1] == 'V')) break;
			if ((r[i] == 'Y' || r[i] == 'O' || r[i] == 'G') && (r[i + 1] == 'Y' || r[i + 1] == 'O' || r[i + 1] == 'G')) break;
			if ((r[i] == 'G' || r[i] == 'B' || r[i] == 'V') && (r[i + 1] == 'G' || r[i + 1] == 'B' || r[i + 1] == 'V')) break;
		}
		if (i < rn) {
			printf("Case #%d: IMPOSSIBLE\n", T);
			continue;
		}
		r[rn] = 0;
		printf("Case #%d: %s\n", T, r);
	}
}