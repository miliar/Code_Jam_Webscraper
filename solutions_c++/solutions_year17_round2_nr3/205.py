#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>

using namespace std;
const int Mn = 100 + 10;
int N, E[Mn], S[Mn];
int dis[Mn][Mn];
double tim[Mn][Mn];
int Q;
int main() {
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		cin >> N >> Q;
		for(int i = 1; i <= N; ++i) {
			cin >> E[i] >> S[i];
		}
		for(int i = 1; i <= N; ++i) {
			for(int j = 1; j <= N; ++j) {
				dis[i][j] = 0x3fffffff;
				tim[i][j] = 1e20;
			}
		}
		for(int i = 1; i <= N; ++i) {
			for(int j = 1; j <= N; ++j) {
				int tmp;
				cin >> tmp;
				if(tmp != -1)
					dis[i][j] = tmp;
			}
		}
		for(int i = 1; i <= N; ++i) {
			dis[i][i] = 0;
		}
		for(int k = 1; k <= N; ++k) {
			for(int i = 1; i <= N; ++i) {
				for(int j = 1; j <= N; ++j) {
					dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
				}
			}
		}
		for(int i = 1; i <= N; ++i) {
			tim[i][i] = 0;
		}
		for(int i = 1; i <= N; ++i) {
			for(int j = 1; j <= N; ++j) {
				if(dis[i][j] <= E[i])
					tim[i][j] = 1. * dis[i][j] / S[i];
			}
		}
		for(int k = 1; k <= N; ++k) {
			for(int i = 1; i <= N; ++i) {
				for(int j = 1; j <= N; ++j) {
					if(tim[i][k] < 1e20 && tim[k][j] < 1e20) {
						tim[i][j] = min(tim[i][j], tim[i][k] + tim[k][j]);

					}
				}
			}
		}
		printf("Case #%d: ", cas);
		for(int i = 1; i <= Q; ++i) {
			int u,v;
			cin >> u >> v;
			printf("%.10f ", tim[u][v]);
		}
		printf("\n");


	}
	return 0;
}