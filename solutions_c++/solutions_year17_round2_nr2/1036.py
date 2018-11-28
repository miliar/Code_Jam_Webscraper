#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a < b ? b : a)

void execute_next(int test, FILE *f, FILE *gg) {
	int n, r, o, y, g, b, v;
	fscanf(f, "%d %d %d %d %d %d %d\n", &n, &r, &o, &y, &g, &b, &v);
	int m[3] = { r, b, y };
	char c[3] = { 'R', 'B', 'Y' };
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2 - i; j++) {
			if (m[j] < m[j + 1]) {
				int mm = m[j];
				m[j] = m[j + 1];
				m[j + 1] = mm;
				char cc = c[j];
				c[j] = c[j + 1];
				c[j + 1] = cc;
			}
		}
	}

	if (m[0] > m[1] + m[2])
		fprintf(gg, "Case #%d: IMPOSSIBLE\n", test + 1);
	else {
		std::string out(n, 'R');
		int pos = 0;
		for (int i = 0; i < n; i++) {
			char cc;
			if (m[0] > 0) {
				m[0]--;
				cc = c[0];
			} else if (m[1] > 0) {
				m[1]--;
				cc = c[1];
			} else {
				cc = c[2];
			}
			out[pos] = cc;
			pos += 2;
			if (pos >= n)
				pos = 1;
		}
		fprintf(gg, "Case #%d: %s\n", test + 1, out.c_str());
	}
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

