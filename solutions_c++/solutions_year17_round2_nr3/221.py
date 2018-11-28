#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int T, N, Q;
long long D[110][110];
double dis[110][110];
long long E[110], S[110];

int main() {
	int T0 = 0;
	scanf("%d", &T);
	for ( ; T; --T) {
		scanf("%d%d", &N, &Q);
		for (int i = 1; i <= N; ++i)
			cin >> E[i] >> S[i];
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				cin >> D[i][j];
		for (int k = 1; k <= N; ++k)
			for (int i = 1; i <= N; ++i)
				for (int j = 1; j <= N; ++j)
					if (D[i][k] != -1 && D[k][j] != -1) {
						if (D[i][j] == -1)
							D[i][j] = 1000000000000000ll;
						D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
					}
		for (int i = 1; i <= N; ++i)
			D[i][i] = 0;
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				if (D[i][j] <= E[i] && D[i][j] != -1) {
					dis[i][j] = (double)D[i][j] / S[i];
				}
				else {
					dis[i][j] = 1000000000000000ll;
				}
			}
		}
		for (int k = 1; k <= N; ++k) {
			for (int i = 1; i <= N; ++i) {
				for (int j = 1; j <= N; ++j)
					dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
			}
		}
		printf("Case #%d:", ++T0);
		for (int i = 1; i <= Q; ++i) {
			int x, y;
			cin >> x >> y;
			printf(" %.6lf", dis[x][y]);
		}
		puts("");

	}
}