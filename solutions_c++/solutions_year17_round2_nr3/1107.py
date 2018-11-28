#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
using namespace std;
const double inf = 1e30;
int N, Q;
int E[200], S[200];
int D[200][200];
int U[200], V[200];
int Sum[200];

void read() {
	cin >> N >> Q;
	for (int i = 0; i < N; ++i) {
		cin >> E[i] >> S[i];
	}
	Sum[0] = 0;
	int next = 1;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> D[i][j];
			if (i + 1 == j) {
				Sum[next] = Sum[next - 1] + D[i][j];
				next++;
			}
		}
	}
	for (int i = 0; i < Q; ++i) {
		cin >> U[i] >> V[i];
	}
}

bool mark[110][110];
double dp[110][110];

double rec(int k, int l) {
	if (k == N - 1) {
		return 0.0;
	}
	if (mark[k][l]) {
		return dp[k][l];
	}
	double r1 = inf, r2 = inf;
	// k+1..k+2
	if (Sum[k + 1] - Sum[k] <= E[k]) {
		r1 = rec(k + 1, k);
		if (r1 != inf) {
			r1 += D[k][k + 1] * 1.0 / S[k];
		}	
	}
	
	// l+1..k+2
	if (Sum[k + 1] - Sum[l] <= E[l]) {
		r2 = rec(k + 1, l);
		if (r2 != inf) {
			r2 += D[k][k + 1] * 1.0 / S[l];
		}
	}
	mark[k][l] = true;	
	return dp[k][l] = min(r1, r2);
}

void solve(int tst) {	
	read();
	for (int i = 0; i <= N; ++i) {
		for (int j = 0; j <= N; ++j) {
			mark[i][j] = false;
		}
	}
	double ans = rec(0, 0);
	printf("Case #%d: %0.6lf\n", tst, ans);	
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
