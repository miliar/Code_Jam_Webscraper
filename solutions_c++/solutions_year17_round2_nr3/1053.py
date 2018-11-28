#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a < b ? b : a)

void execute_next(int test, FILE *f, FILE *g) {
	int n, q;
	fscanf(f, "%d %d\n", &n, &q);
	vector<int> e(n), s(n);
	for (int i = 0; i < n; i++) {
		fscanf(f, "%d %d\n", &e[i], &s[i]);
	}
	vector<vector<int>> d(n, vector<int>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			fscanf(f, "%d", &d[i][j]);
		}
	}
	vector<int> u(q), v(q);
	for (int i = 0; i < q; i++) {
		fscanf(f, "%d %d\n", &u[i], &v[i]);
	}

	vector<vector<pair<long double, int>>> ht(n, vector<pair<long double, int>>(n));
	ht[0][0].first = 0;
	ht[0][0].second = e[0];
	for (int i = 1; i < n; i++) {
		long double best_time = -1;
		for (int j = 0; j < i; j++) {
			if (ht[i-1][j].second >= d[i - 1][i]) {
				ht[i][j].second = ht[i - 1][j].second - d[i - 1][i];
				ht[i][j].first = ht[i - 1][j].first + (long double)d[i-1][i] / s[j];
				if (best_time < 0 || ht[i][j].first < best_time)
					best_time = ht[i][j].first;
			} else {
				ht[i][j].second = -1;
			}
		}
		ht[i][i].first = best_time;
		ht[i][i].second = e[i];
	}
	fprintf(g, "Case #%d: %.9lf\n", test + 1, ht[n - 1][n - 1]);
}

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
		printf("%d\n", test + 1);
	}
	fclose(f);
	fclose(g);
	return 0;
}

