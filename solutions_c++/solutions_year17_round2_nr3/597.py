#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <queue>
using namespace std;
 
const int MAXN = 105;

int N;
long long D[MAXN][MAXN];
double T[MAXN];
double E[MAXN], S[MAXN];
bool vis[MAXN];

double solve(int U, int V) {
	for (int i = 0; i < N; ++i) {
		T[i] = 1e30;
		vis[i] = false;
	}
	T[U] = 0;
	for (int i = 0; i < N; ++i) {
		int u = -1;
		for (int j = 0; j < N; ++j) {
			if (!vis[j] && (u == -1 || T[u] > T[j])) {
				u = j;
			}
		}
		if (u == V) {
			break;
		}
		vis[u] = true;
		for (int j = 0; j < N; ++j) {
			if (!vis[j] && D[u][j] != -1 && D[u][j] <= E[u]) {
				double tmp = T[u] + D[u][j] / S[u];
				if (tmp < T[j]) {
					T[j] = tmp;
				}
			}
		}
	}
	return T[V];
}

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int Q;
		cin >> N >> Q;
		for (int i = 0; i < N; ++i) {
			cin >> E[i] >> S[i];
		}
		for (int i = 0; i < N; i ++) {
			for (int j = 0; j < N; j ++) {
				cin >> D[i][j];
				//start from 0;
			}
		}
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i ++) {
				if (D[i][k] == -1) continue;
				for (int j = 0; j < N;j ++) {
					if (D[k][j] == -1) continue;
					if (D[i][j] == -1 || D[i][j] > D[i][k] + D[k][j]) {
						D[i][j] = D[i][k] + D[k][j];

					}
				}
			}
		}
		cout <<"Case #"<<cas<<":";
		for (int i = 0; i < Q; i++) {
			int U, V;
			cin >> U >> V;
			U--;
			V--;
			printf(" %.10f", solve(U, V));
		}
		puts("");
		


	}
}