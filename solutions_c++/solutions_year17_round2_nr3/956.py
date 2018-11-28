#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

const int MAX_N = 100;

typedef long long ll;

int T;
int N, Q, E[MAX_N], S[MAX_N], D[MAX_N][MAX_N];
bool visited[MAX_N];
int stamina[MAX_N];
double time_[MAX_N][MAX_N], minTime[MAX_N];

int main()
{
	// freopen("r1b_c.in", "r", stdin);
	// freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("r1b_c.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		printf("Case #%d: ", t);
		
		scanf("%d %d", &N, &Q);
		FOR(i, 0, N) {
			scanf("%d %d", &E[i], &S[i]);
		}
		FOR(i, 0, N) {
			FOR(j, 0, N) {
				scanf("%d", &D[i][j]);
				time_[i][j] = -1;
			}
		}
		
		FOR(i, 0, N) {
			// calculate time_[i][j] for all j
			int cur = i;
			memset(visited, 0, sizeof(visited));
			FOR(j, 0, N) {
				stamina[j] = -1;
			}
			time_[i][i] = 0;
			stamina[i] = E[i];

			while (true) {
				FOR(j, 0, N) {
					if (j == cur || visited[j] || D[cur][j] < 0) continue;
					int newStamina = stamina[cur] - D[cur][j];
					if (newStamina < 0) continue;
					double newT = time_[i][cur] + (D[cur][j]) / (double)(S[i]);
					if (time_[i][j] < 0 || newT < time_[i][j]) {
						time_[i][j] = newT;
						stamina[j] = newStamina;
					}
				}
				
				visited[cur] = true;
				
				double nextMinT = -1;
				int nextMinTNode = -1;
				FOR(j, 0, N) {
					if (!visited[j]) {
						if (nextMinT < 0 || (time_[i][j] >= 0 && time_[i][j] < nextMinT)) {
							nextMinT = time_[i][j];
							nextMinTNode = j;
						}
					}
				}
				
				if (nextMinTNode >= 0) {
					cur = nextMinTNode;
				}
				else break;
			}
			
			// FOR(j, 0, N) {
				// printf("%lf |", time_[i][j]);
				// printf("%d s: ", stamina[j]);
			// }
			// printf("\n");
		}
		
		FOR(q, 0, Q) {
			int U, V;
			scanf("%d %d", &U, &V);
			U--; V--;
			int cur = U;
			memset(visited, 0, sizeof(visited));
			FOR(i, 0, N) {
				minTime[i] = -1;
			}
			minTime[U] = 0;
			
			while (true) {
				FOR(i, 0, N) {
					if (i == cur || visited[i] || time_[cur][i] < 0) continue;
					double newT = minTime[cur] + time_[cur][i];
					if (minTime[i] < 0 || newT < minTime[i]) {
						minTime[i] = newT;
					}
				}
				
				visited[cur] = true;
				
				double nextMinT = -1;
				int nextMinTNode = -1;
				FOR(i, 0, N) {
					if (!visited[i]) {
						if (nextMinT < 0 || (minTime[i] >= 0 && minTime[i] < nextMinT)) {
							nextMinT = minTime[i];
							nextMinTNode = i;
						}
					}
				}
				
				if (nextMinTNode >= 0) {
					cur = nextMinTNode;
				}
				else break;
			}
			
			printf("%lf ", minTime[V]);
		}
		
		printf("\n");
	}
	return 0;
}
