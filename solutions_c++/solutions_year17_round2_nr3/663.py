#include <cassert>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
#define INF 1000000005
#define MAXN 105
using namespace std;

int T, n, Q;
int d[MAXN][MAXN], dist[MAXN][MAXN];
int duration[MAXN], speed[MAXN];
double values[MAXN][MAXN];
bool mark[MAXN];

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%d %d", &n, &Q);
		for (int i = 1; i <= n; i++) {
			scanf("%d %d", &duration[i], &speed[i]);
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				scanf("%d", &d[i][j]);
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (i == j) {
					dist[i][j] = 0;
				} else {
					dist[i][j] = (d[i][j] < 0) ? (INF + 1) : d[i][j];
				}
			}
		}

		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}

		for (int source = 1; source <= n; source++) {
			for (int i = 1; i <= n; i++) {
				values[source][i] = (source == i) ? 0 : (1.0 * INF * n);
			}
			memset(mark, true, sizeof mark);
			for (int iter = 1; iter <= n; iter++) {
				int u = -1;
				for (int i = 1; i <= n; i++) if (mark[i] && (u < 0 || values[source][i] < values[source][u])) {
					u = i;
				}

				mark[u] = false;
				for (int v = 1; v <= n; v++) if (dist[u][v] <= duration[u]) {
					double tmp = values[source][u] + 1.0 * dist[u][v] / speed[u];
					if (values[source][v] > tmp) {
						values[source][v] = tmp;
					}
				}
			}
		}

		printf("Case #%d:", it);
		while (Q--) {
			int x, y;
			scanf("%d %d", &x, &y);
			printf(" %.9lf", values[x][y]);
		}
		printf("\n");
	}
	return 0;
}