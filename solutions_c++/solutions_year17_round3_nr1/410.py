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
	int n, k;
	fscanf(f, "%d %d\n", &n, &k);
	vector<pair<long double, int>> p(n);
	for (int i = 0; i < n; i++) {
		int r, h;
		fscanf(f, "%d %d\n", &r, &h);
		p[i].second = r;
		p[i].first = (long double)h * r * 2 * M_PI;
	}
	
	long double max = 0;
	sort(p.begin(), p.end());
	for (int i = 0; i < n; i++) {
		long double a = p[i].first;
		int cnt = 1;
		for (int j = n - 1; j >= 0 && cnt < k; j--) {
			if (i != j && p[j].second <= p[i].second) {
				cnt += 1;
				a += p[j].first;
			}
		}
		if (cnt < k)
			continue;
		a += (long double)p[i].second * p[i].second * M_PI;
		if (a > max)
			max = a;
	}

	printf("%d\n", test + 1);
	fprintf(g, "Case #%d: %.9lf\n", test + 1, max);
}

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
	}
	fclose(f);
	fclose(g);
	return 0;
}

