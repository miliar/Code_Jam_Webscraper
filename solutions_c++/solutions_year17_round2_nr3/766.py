#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <numeric>
#include <algorithm>
#include <vector>
#include <map>
#include <random>
#include <cstdio>
#include <cmath>
using namespace std;


int main() {
	freopen("H:\\Projects\\Codejam2017\\c_large_in.txt", "r", stdin);
	freopen("H:\\Projects\\Codejam2017\\c_large_out.txt", "w", stdout);

	string s;
	const int MAXN = 4;
	char ch;
	int tests, test, n, m, x, y;
	double C, F, X;
	int D;
	int N, Q;

	scanf("%d", &tests);

	for (test = 1; test <= tests; ++test) {
		scanf("%d %d", &N, &Q);
		vector<pair<long long, long long>> horses = vector<pair<long long, long long>>(N, { 0, 0 });
		vector<vector<long long>> dist = vector<vector<long long>>(N, vector<long long>(N, 0));
		//vector<vector<long long>> d = vector<vector<long long>>(N, vector<long long>(N, 0));
		//vector<vector<double>> f = vector<vector<double>>(N, vector<double>(N, 0));
		vector<double> f = vector<double>(N, 0);

		for (int i = 0; i < N; ++i) {
			scanf("%ld %ld", &horses[i].first, &horses[i].second);
		}
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j) {
				scanf("%ld", &dist[i][j]);
			}

		for (int k = 0; k < N; ++k) {
			for (int i = 0; i < N; ++i) if (dist[i][k] > 0) {
				for (int j = 0; j < N; ++j) if (dist[k][j] > 0) {
					if (dist[i][j] == -1 || dist[i][j] > dist[i][k] + dist[k][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					}
				}
			}
		}


		//int src, dst;
		//scanf("%d %d", &src, &dst);

		//double ans = 0;
		//src -= 1;
		//dst -= 1;
		//f[src] = 0;
		//for (int i = src + 1; i <= dst; ++i) f[i] = 1e20;
		//for (int i = src + 1; i <= dst; ++i) {
		//	for (int j = src; j <= i - 1; ++j) {
		//		if (horses[j].first >= d[i] - d[j]) {
		//			f[i] = min(f[i], f[j] + (double)(d[i] - d[j]) / horses[j].second);
		//		}

		//		//if (d[i] < d[j]) {
		//		//	printf("%d %d %d %d\n", d[i], d[j], i, j); 
		//		//}
		//	}
		//}

		//printf("Case #%d: %.10f\n", test, f[dst]);


		printf("Case #%d:", test);
		for (int i = 0; i < Q; ++i) {
			int src, dst; 
			scanf("%d %d", &src, &dst);
			src -= 1;
			dst -= 1;
			double ans = 0;
			for (int i = 0; i < N; ++i) f[i] = 1e30;
			f[src] = 0;

			bool updated = true;
			while (updated) {
				updated = false; 
				for (int i = 0; i < N; ++i)
					for (int j = 0; j < N; ++j) if (f[j] < 1e29 && i != j) {
						if (horses[j].first >= dist[j][i]) {
							double newval = f[j] + (double)(dist[j][i]) / horses[j].second;
							if (newval < f[i]) {
								f[i] = newval; 
								updated = true; 
							}
						}
					}
			}

			printf(" %.8f", f[dst]); 
		}
		printf("\n"); 
	}

	return 0;
}
