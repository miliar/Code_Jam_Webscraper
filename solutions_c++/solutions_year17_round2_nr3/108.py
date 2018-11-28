#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t, n, q;
int e[110], s[110];
long long d[110][110];
double weight[110][110];

int main(void) {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%d%d", &n, &q);
		for (int i = 1; i <= n; i++)
			fscanf(fin, "%d%d", e + i, s + i);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				fscanf(fin, "%lld", &d[i][j]);

		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++) {
					if (d[i][k] == -1 || d[k][j] == -1) continue;
					if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j])
						d[i][j] = d[i][k] + d[k][j];
				}

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				weight[i][j] = 1e18;
				if (d[i][j] == -1) continue;
				if (d[i][j] > e[i]) continue;
				weight[i][j] = 1.0 * d[i][j] / s[i];
			}
		
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					weight[i][j] = min(weight[i][j], weight[i][k] + weight[k][j]);

		for (int qq = 1; qq <= q; qq++) {
			int from, to; fscanf(fin, "%d%d", &from, &to);
			fprintf(fout, "%.10lf%c", weight[from][to], (qq == q ? '\n' : ' '));
		}
	}
	return 0;
}