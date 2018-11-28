#include <bits/stdc++.h>
using namespace std;

const char* colors = "RYB";

char s[1111];
char P[1111];

bool create_ans(int *C) {
	int N = C[0] + C[1] + C[2];
	if (C[0] < 0 || C[1] < 0 || C[2] < 0) return false;
	if (C[0]*2 > N || C[1]*2 > N || C[2]*2 > N) return false;
	int last = -1, first = -1;
	for (int i = 0; i < N; i++) {
		// choose max color
		int jj = -1, cj = -1;
		for (int j = 0; j < 3; j++) if (j != last && C[j] > cj) {
			jj = j;
			cj = C[j];
		}
		if (first == -1) first = jj;
		else if (first != last && C[jj] == C[first]) jj = first;
		C[jj]--;
		// cannot find color
		if (jj == -1) return false;
		// add to string
		last = jj;
		s[i] = colors[jj];
	}
	s[N] = 0;
	return true;
}

void solve() {
	int N, R, O, Y, G, B, V;
	scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
	int C[3] = {R - G, Y - V, B - O};
	if (!create_ans(C)) {
		printf("IMPOSSIBLE\n");
		return;
	}
	//
	int ns = strlen(s);
	bool removelast = false;
	if (ns == 0) {
		if (R == G && R + G == N) s[ns++] = 'R', removelast = true;
		if (Y == V && Y + V == N) s[ns++] = 'Y', removelast = true;
		if (B == O && B + O == N) s[ns++] = 'B', removelast = true;
	}
	int np = 0;
	bool RR = true, YY = true, BB = true;
	for (int i = 0; i < ns; i++) {
		P[np++] = s[i];
		if (RR && s[i] == 'R') {
			// transform to RGRGR
			RR = false;
			for (int j = 0; j < G; j++) {
				P[np++] = 'G';
				P[np++] = 'R';
			}
		}
		if (YY && s[i] == 'Y') {
			// transform to YVYV
			YY = false;
			for (int j = 0; j < V; j++) {
				P[np++] = 'V';
				P[np++] = 'Y';
			}
		}
		if (BB && s[i] == 'B') {
			// transform to BOBOBO
			BB = false;
			for (int j = 0; j < O; j++) {
				P[np++] = 'O';
				P[np++] = 'B';
			}
		}
	}
	if (removelast) np--;
	P[np] = 0;
	if (np == N) printf("%s\n", P);
	else printf("IMPOSSIBLE\n");
}

int main() {
	freopen("B.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}