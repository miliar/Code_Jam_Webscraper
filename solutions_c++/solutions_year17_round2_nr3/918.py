#include <bits/stdc++.h>
using namespace std;

int N, Q;
long long D[128][128];
long long S[128], E[128];
double F[128][128]; //, A[128][128];



void solve() {
	cin >> N  >> Q;
	for (int i = 1; i <= N; i++) {
		cin >> E[i] >> S[i];
		//cout << E[i] << ' ' << S[i] << endl;
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> D[i][j];
			//cout << D[i][j] << ' ';
			if (D[i][j] == -1) 
					D[i][j] = 1e10;
		}
		//cout << endl;
	}
    for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				D[i][j] = min(D[i][j], D[i][k]+D[k][j]);

    for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			if (D[i][j] <= E[i]) {
				F[i][j] = 1.0 * D[i][j] / S[i];
			}else {
				F[i][j] = 1e100;
			}
			
    for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				F[i][j] = min(F[i][j], F[i][k]+F[k][j]);


	for (int i = 1; i <= Q; i++) {
		int U, V;
		cin >> U >> V;
		printf("%.8f", F[U][V]);
		if (i != Q)
			cout << ' '; 
	}
		cout << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		//cout << endl;
		solve();
	}
	return 0;
}

