#include<bits/stdc++.h>
using namespace std;

int n, q;
long long S[105], E[105];
long long C[105][105];

double V[105][105];

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/fiewojfe/C-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/fiewojfe/C-large.out", "w", stdout);
	int t; cin >> t;
	int id = 1;
	while (t--) {
		cin >> n >> q;
		for (int i = 0; i < n; i++)
			cin >> E[i] >> S[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				cin >> C[i][j];
				if (C[i][j] == -1)
					C[i][j] = 1e18;
			}
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					C[i][j] = min(C[i][j], C[i][k] + C[k][j]);


		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				// start with horse i to reach j
				if (E[i] < C[i][j])
					V[i][j] = 1e18;
				else
					V[i][j] = C[i][j] * 1.0 / S[i];
			}
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					V[i][j] = min(V[i][j], V[i][k] + V[k][j]);


		printf("Case #%d: ", id++);
		for (int i = 0; i < q; i++) {
			int a, b; cin >> a >> b; --a; --b;
			printf("%.13lf%c", V[a][b], i == q - 1 ? '\n' : ' ');
		}

	}

	return 0;
}
