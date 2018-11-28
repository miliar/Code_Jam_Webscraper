#include"stdio.h"
#include"algorithm"
using namespace std;
int T, Q, N, E[105], S[105], M[105][105], U, V;
double AdjM[105][105], INF = 1000000000000009;
double Ans, MaxT;
int main() {
	//freopen("C-small-attempt1.in", "r", stdin);
	//freopen("C-small-attempt1.txt", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &N, &Q);
		for (int i = 1; i <= N; i++)
			scanf("%d%d", &E[i], &S[i]);
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				scanf("%d", &M[i][j]);
				
				
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				AdjM[i][j] = (M[i][j] == -1)? INF: M[i][j];
		for (int k = 1; k <= N; k++)
			for (int i = 1; i <= N; i++)
				for (int j = 1; j <= N; j++)
					AdjM[i][j] = min(AdjM[i][j], AdjM[i][k] + AdjM[k][j]);
				
		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= N; j++)
				if (AdjM[i][j] <= E[i])
					AdjM[i][j] /= S[i];
		
		for (int k = 1; k <= N; k++)
			for (int i = 1; i <= N; i++)
				for (int j = 1; j <= N; j++)
					AdjM[i][j] = min(AdjM[i][j], AdjM[i][k] + AdjM[k][j]);
		
		printf("Case #%d:", t);
		
		for (int i = 0; i < Q; i++) {
			scanf("%d%d", &U, &V);
			printf(" %.9lf", AdjM[U][V]);
		}
		printf("\n");
	}
}
