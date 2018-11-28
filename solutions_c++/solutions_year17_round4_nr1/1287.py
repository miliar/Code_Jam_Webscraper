#define _USE_MATH_DEFINES
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

void execute_next(int test, FILE *f, FILE *g) {
	int n, p;
	fscanf(f, "%d %d\n", &n, &p);
	vector<int> r(p, 0);
	for (int i = 0; i < n; i++) {
		int gr;
		fscanf(f, "%d", &gr);
		r[gr % p]++;
	}
	
	int result = r[0];
	r[0] = 0;
	for (int i = 1; i <= p / 2; i++) {
		int cnt = (i == p - i) ? (r[i] / 2) : MIN(r[i], r[p - i]);
		r[i] -= cnt;
		r[p - i] -= cnt;
		result += cnt;
	}
	if (p == 4) {
		int cnt;
		cnt = MIN(r[1] / 2, r[2]);
		r[1] -= cnt * 2;
		r[2] -= cnt;
		result += cnt;
		cnt = MIN(r[3] / 2, r[2]);
		r[3] -= cnt * 2;
		r[2] -= cnt;
		result += cnt;
	}
	for (int i = 1; i < p; i++) {
		int cnt = r[i] / p;
		r[i] -= cnt * p;
		result += cnt;
	}

	for (int i = 0; i < p; i++) {
		if (r[i] > 0) {
			result++;
			break;
		}
	}
	
	fprintf(g, "Case #%d: %d\n", test + 1, result);
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

