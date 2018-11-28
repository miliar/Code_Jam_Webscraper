#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t, d, n, k, s;

int main(void) {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%d%d", &d, &n);
		double ans = 1e15;
		for (int i = 0; i < n; i++) {
			fscanf(fin, "%d%d", &k, &s);
			ans = min(ans, ((double)d) * s / (d - k));
		}
		fprintf(fout, "%.10lf\n", ans);
	}
	return 0;
}