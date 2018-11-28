#include <stdio.h>
#include <string.h>
#include <assert.h>
FILE *in = fopen("input.txt", "r"), *out = fopen("output.txt", "w");
//FILE *in = stdin, *out = stdout;
#include <algorithm>
#include <vector>
#define NM 40
#define si(n) fscanf(in,"%d",&n)
#define FOR(i,n,m) for (int i=(n);i<=(m);i++)
#define INF 2e9
#define MOD 1000000007
using namespace std;
typedef long long int ll;
#include <string.h>
int Hd, Ad, Hk, Ak, B, D;
int dy[105][105][105][105];
void input() {
	si(Hd), si(Ad), si(Hk), si(Ak), si(B), si(D);
}
int Dy(int hd, int ad, int hk, int ak) {
	if (dy[hd][ad][hk][ak] >= 0) return dy[hd][ad][hk][ak];
	if (hk == 0) return 0;
	//if (ak == 0) return dy[hd][ad][hk][ak] = (hk + ad - 1) / ad;

	int cnt = INF;
	// Attack
	if (hk - ad > 0) { // live after attack
		if (hd - ak > 0) // live after attacked
			cnt = min(cnt, Dy(hd - ak, ad, hk - ad, ak) + 1);
	}
	else { // kill this turn
		cnt = min(cnt, 1);
	}

	// Buff
	if (B > 0 && ad != 100) {
		if (hd - ak > 0) // live after attacked
			cnt = min(cnt, Dy(hd - ak, min(ad + B, 100), hk, ak) + 1);
	}

	// Cure
	if (Hd - ak > 0 && hd != Hd - ak) { // meaningful
		cnt = min(cnt, Dy(Hd - ak, ad, hk, ak) + 1);
	}

	// Debuff
	if (D > 0 && ak != 0) {
		if (hd - max((ak - D),0) > 0) { // live after attacked
			cnt = min(cnt, Dy(hd - max((ak - D), 0), ad, hk, max(ak - D, 0)) + 1);
		}
	}
	dy[hd][ad][hk][ak] = cnt;
	return dy[hd][ad][hk][ak];
}
int main() {
	int TT; si(TT);
	FOR(tt, 1, TT) {
		input();
		FOR(i, 0, Hd) FOR(j, 0, 100) FOR(k, 0, Hk) FOR(l, 0, 100) dy[i][j][k][l] = -1;
		fprintf(out, "Case #%d: ", tt);
		int t = Dy(Hd, Ad, Hk, Ak);
		if (t != INF) fprintf(out, "%d\n", t);
		else fprintf(out, "IMPOSSIBLE\n");
	}
	return 0;
}