#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int tn;
double G[101][101];
double T[101][101];
double E[101], S[101];
double res[101][101];
int n, Q;

bool visited[101];

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d", &n, &Q);
		for(int i = 0; i < n; i++)
			scanf("%lf %lf", &E[i], &S[i]);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				scanf("%lf", &(G[i][j]));

		// compute minimum distance
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				T[i][j] = G[i][j];
		for(int i = 0; i < n; i++)
			T[i][i] = 0;
		for(int k = 0; k < n; k++)
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
					if (T[i][k] >= -0.1 && T[k][j] >= -0.1 && (T[i][j] < -0.5 || T[i][k] + T[k][j] < T[i][j]))
						T[i][j] = T[i][k] + T[k][j];

		/*for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++)
				printf("%lf ", T[i][j]);
			printf("\n");
		}*/

		for(int start = 0; start < n; start ++) {
			memset(visited, 0, sizeof(visited));
			for(int i = 0; i < n; i++)
				res[start][i] = -1;
			res[start][start] = 0;
			for(int i = 0; i < n; i++) {
				double min_d = 1e200;
				int min_i = -1;
				for(int j = 0; j < n; j++)
					if (!visited[j] && res[start][j] >= -0.1 && res[start][j] < min_d) {
						min_d = res[start][j];
						min_i = j;
					}
				if (min_i == -1) break;
				visited[min_i] = true;
				//printf("min_i = %d, start = %d, res[start][min_i] = %lf\n", min_i, start, res[start][min_i]);
				for(int j = 0; j < n; j++) {
					if (!visited[j] && T[min_i][j] >= -0.1 && T[min_i][j] <= E[min_i]) {
						double new_t = res[start][min_i] + (double)T[min_i][j] / S[min_i];
						if (res[start][j] == -1 || new_t < res[start][j]) res[start][j] = new_t;
					} 				
				}
			}
		}

		fprintf(stderr, "%d\n", ctn+1);
		printf("Case #%d:", ctn+1);
		for(int i = 0; i < Q; i++) {
			int t1, t2;
			scanf("%d %d", &t1, &t2);
			printf(" %0.7lf", res[t1-1][t2-1]);
		}
		printf("\n");

	}

	return 0;

}