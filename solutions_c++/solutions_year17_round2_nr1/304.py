#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 1024;

int n;
double d;
double a[MAX][2];

void solveTest() {
    fscanf(in, "%lf %d", &d, &n);
    for (int i = 0; i < n; i++)
        fscanf(in, "%lf %lf", &a[i][0], &a[i][1]);

    double maxTime = 0;
    for (int i = 0; i < n; i++) {
        maxTime = max(maxTime, (d - a[i][0]) / a[i][1]);
    }
    fprintf(out, "%.9lf\n", d / maxTime);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("CruiseControl.in", "rt");
	out = fopen("CruiseControl.out", "wt");

	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest();
	}

	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
