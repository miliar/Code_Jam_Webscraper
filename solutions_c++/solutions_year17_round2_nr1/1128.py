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
	int d, n;
	fscanf(f, "%d %d\n", &d, &n);
	long double max_time = 0;
	for (int i = 0; i < n; i++) {
		int k, s;
		fscanf(f, "%d %d\n", &k, &s);
		long double time = (long double)(d - k) / s;
		if (time > max_time)
			max_time = time;
	}
	long double speed = (long double)d / max_time;

	printf("%d\n", test + 1);
	fprintf(g, "Case #%d: %.9lf\n", test + 1, speed);
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

