#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t, n, r, o, y, g, b, v;

int main(void) {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		fscanf(fin, "%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		if (!o && !y && !b && !v && r == g) {
			for (int i = 0; i < g; i++)
				fprintf(fout, "RG");
			fprintf(fout, "\n");
		}
		else if (!r && !y && !g && !v && o == b) {
			for (int i = 0; i < o; i++)
				fprintf(fout, "BO");
			fprintf(fout, "\n");
		}
		else if (!r && !o && !g && !b && y == v) {
			for (int i = 0; i < v; i++)
				fprintf(fout, "YV");
			fprintf(fout, "\n");
		}
		else if (o && o >= b || g && g >= r || v && v >= y)
			fprintf(fout, "IMPOSSIBLE\n");
		else {
			b -= o; r -= g; y -= v;
			if (y + b < r || b + r < y || r + y < b)
				fprintf(fout, "IMPOSSIBLE\n");
			else {
				if (r >= b && r >= y) {
					for (int i = 0; i < g; i++)
						fprintf(fout, "RG");
					for (int i = 0; i < r; i++) {
						fprintf(fout, "R");
						if (i < y) {
							if (i == 0) {
								for (int j = 0; j < v; j++)
									fprintf(fout, "YV");
							}
							fprintf(fout, "Y");
						}
						if (i >= r - b) {
							if (i == r - 1) {
								for (int j = 0; j < o; j++)
									fprintf(fout, "BO");
							}
							fprintf(fout, "B");
						}
					}
				}
				else if (y >= r && y >= b) {
					for (int i = 0; i < v; i++)
						fprintf(fout, "YV");
					for (int i = 0; i < y; i++) {
						fprintf(fout, "Y");
						if (i < r) {
							if (i == 0) {
								for (int j = 0; j < g; j++)
									fprintf(fout, "RG");
							}
							fprintf(fout, "R");
						}
						if (i >= y - b) {
							if (i == y - 1) {
								for (int j = 0; j < o; j++)
									fprintf(fout, "BO");
							}
							fprintf(fout, "B");
						}
					}
				}
				else {
					for (int i = 0; i < o; i++)
						fprintf(fout, "BO");
					for (int i = 0; i < b; i++) {
						fprintf(fout, "B");
						if (i < r) {
							if (i == 0) {
								for (int j = 0; j < g; j++)
									fprintf(fout, "RG");
							}
							fprintf(fout, "R");
						}
						if (i >= b - y) {
							if (i == b - 1) {
								for (int j = 0; j < v; j++)
									fprintf(fout, "YV");
							}
							fprintf(fout, "Y");
						}
					}
				}
				fprintf(fout, "\n");
			}
		}
	}
	return 0;
}