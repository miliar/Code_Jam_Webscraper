#include "stdafx.h"

ll E[110];
ll S[110];
ll D[110][110];
int U[200];
int V[200];
double ans[110][110];

int main() {
	ios_base::sync_with_stdio(0); cout.tie(NULL);
	int _cases; cin >> _cases;
	for (int _case = 1; _case <= _cases; _case++) {
		int N; int Q;
		cin >> N >> Q;
		for (int i = 0; i < N; i++)cin >> E[i] >> S[i];
		for (int i = 0; i < N; i++)for (int j = 0; j < N; j++) { cin >> D[i][j]; if (D[i][j] == -1)D[i][j] = 1e15; }
		for (int i = 0; i < Q; i++)cin >> U[i] >> V[i];
		/*
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << D[i][j] << " ";
			}
			cout << endl;
		}cout << endl;
		*/
		for (int k = 0; k < N; k++)
			for (int i = 0; i < N; i++)
				for (int j = 0; j < N; j++){
					// If vertex k is on the shortest path from
					// i to j, then update the value of dist[i][j]
					if (D[i][k] + D[k][j] < D[i][j])
						D[i][j] = D[i][k] + D[k][j];
				}
		/*
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << D[i][j] << "\t";
			}
			cout << endl;
		}cout << endl;
		*/
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++){
				if (D[i][j] <= E[i])ans[i][j] = D[i][j] / double(S[i]);
				else ans[i][j] = 1e15;
			}

		for (int k = 0; k < N; k++)
			for (int i = 0; i < N; i++)
				for (int j = 0; j < N; j++) {
					// If vertex k is on the shortest path from
					// i to j, then update the value of dist[i][j]
					if (ans[i][k] + ans[k][j] < ans[i][j])
						ans[i][j] = ans[i][k] + ans[k][j];
				}
		/*
		for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
		cout << ans[i][j] << "\t";
		}
		cout << endl;
		}cout << endl;
		*/
		cout << "Case #" << _case << ": " ;
		for (int i = 0; i < Q; i++)cout <<fixed<<setprecision(10) <<ans[U[i]-1][V[i]-1] << " ";
		cout << endl;
	}

}
