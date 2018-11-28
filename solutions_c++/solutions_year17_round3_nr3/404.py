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
	int n, k;
	fscanf(f, "%d %d\n", &n, &k);
	double tmp;
	int u;
	vector<int> p(n);
	fscanf(f, "%lf", &tmp);
	u = tmp * 10000 + 0.5;
	for (int i = 0; i < n; i++) {
		fscanf(f, "%lf", &tmp);
		p[i] = tmp * 10000 + 0.5;
	}
	sort(p.begin(), p.end());
	while (u > 0) {
		int cnt = 1;
		while (cnt < n && p[cnt - 1] == p[cnt])
			cnt++;
		int spent = u;
		if (cnt < n)
			spent = MIN(spent, (p[cnt] - p[cnt - 1]) * cnt);
		int to_one = spent / cnt;
		int add = spent % cnt;
		for (int i = 0; i < cnt; i++) {
			p[i] += to_one;
			if (i >= (cnt - add))
				p[i]++;
		}
		u -= spent;
	}
	long double result = 1;
	for (int i = 0; i < n; i++) {
		result *= p[i];
		result /= 10000;
	}
	
	fprintf(g, "Case #%d: %.9lf", test + 1, result);
	fprintf(g, "\n");
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

