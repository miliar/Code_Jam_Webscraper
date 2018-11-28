#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
int R[55], Q[55][55], pt[55];
void solve(int cn) {
	int N, P;
	scanf("%d%d", &N, &P);
	for (int i = 1; i <= N; ++i) scanf("%d", &R[i]);
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= P; ++j) scanf("%d", &Q[i][j]);
		sort(Q[i] + 1, Q[i] + P + 1);
	}
	for (int i = 1; i <= N; ++i) pt[i] = 1;
	int ans = 0;
	for (int s = 1;;) {
		// Try to make s servings
		bool ok = true;
		for (int i = 1; i <= N; ++i) {
			while (pt[i] <= P && Q[i][pt[i]] * 10 < (ll)R[i] * s * 9) ++pt[i];
			if (pt[i] > P) {
				printf("Case #%d: %d\n", cn, ans);
				return;
			}
			if (Q[i][pt[i]] * 10 > (ll)R[i] * s * 11) ok = false;
		}
		if (ok) {
			++ans;
			for (int i = 1; i <= N; ++i) ++pt[i];
		} else {
			++s;
		}
	}
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		solve(cn);
	}
}

