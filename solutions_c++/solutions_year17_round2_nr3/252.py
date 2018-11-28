#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX = 105;
int tc, Start, End, N, Q;
ll A[MAX], D[MAX], S[MAX];
double adj[MAX][MAX];

int main() {
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		printf("Case #%d:",tt);

		scanf("%d%d", &N, &Q);
		for (int i=0; i<N; ++i)
			scanf("%lld%lld", &D[i], &S[i]);

		for (int i=0; i<N; ++i) for (int j=0; j<N; ++j) {
			scanf("%lf", &adj[i][j]);
			if (adj[i][j] == -1) adj[i][j] = 1e15;
			if (i == j) adj[i][j] = 0;
		}

		for (int k=0; k<N; ++k) for (int i=0; i<N; ++i) for (int j=0; j<N; ++j)
			adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);

		for (int i=0; i<N; ++i) {
			for (int j=0; j<N; ++j) {
				if (adj[i][j] > D[i] || adj[i][j] == 0) adj[i][j] = 1e15;
				else adj[i][j] = (double)adj[i][j]/S[i];
			}
		}

		for (int k=0; k<N; ++k) for (int i=0; i<N; ++i) for (int j=0; j<N; ++j)
			adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);


		for (int q=0; q<Q; ++q) {
			scanf("%d%d", &Start, &End);
			--Start, --End;

			printf(" %.10lf", adj[Start][End]);
		}

		printf("\n");
	}

	return 0;
}
