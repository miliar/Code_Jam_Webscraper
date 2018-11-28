#pragma warning(disable:4996)
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int E[101];
int S[101];
int D[101][101];
int U[101];
int V[101];
double t[101];
int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	int Q, N;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		cin >> Q;
		for (int i=1; i<=N; i++) {
			cin >> E[i];
			cin >> S[i];
		}
		for (int i=1; i<=N; i++) {
			for (int j=1; j<=N; j++) {
				cin >> D[i][j];
			}
		}
		for (int i=0; i<Q; i++) {
			cin >> U[i];
			cin >> V[i];
		}
		for (int i=N-2; i>=1; i--) {
			for (int j=i+2; j<=N; j++) {
				D[i][j] = D[i][j-1]+D[j-1][j];
			}
		}
		
		t[N]=0;
		for (int i=N-1; i>=1; i--) {
			t[i] = 10000000000000;
			for (int j=i+1; j<=N; j++) {
				if (D[i][j] <= E[i]) {
					double t1 = (double)D[i][j]/S[i];
					if (t1 + t[j] < t[i]) {
						t[i] = t1 + t[j];
					}
				} else {
					j=N;
				}
			}
		//	cout << t[i] << endl;
		}		

		printf("Case #%d: ", tc);
			printf("%f\n", t[1]);
		
		

	}
	return 0;
}
