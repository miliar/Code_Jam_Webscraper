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
const double EPS = 0.1;
const double INF = 1e100;

int n;
double a[MAX][2];
double d[MAX][MAX];
double ans[MAX][MAX];

void solve() {
    for (int i = 0; i < n; i++)
        d[i][i] = 0;
    for (int i = 0; i < n; i++)
        for (int c = 0; c < n; c++)
            if (d[i][c] == -1) d[i][c] = INF;
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int c = 0; c < n; c++)
                if (d[i][c] > d[i][k] + d[k][c])
                    d[i][c] = d[i][k] + d[k][c];

    for (int i = 0; i < n; i++)
        for (int c = 0; c < n; c++)
            ans[i][c] = INF;

    for (int i = 0; i < n; i++)
        for (int c = 0; c < n; c++)
            if (d[i][c] <= a[i][0] + EPS)
                ans[i][c] = min(ans[i][c], d[i][c] / a[i][1]);

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int c = 0; c < n; c++)
                if (ans[i][c] > ans[i][k] + ans[k][c])
                    ans[i][c] = ans[i][k] + ans[k][c];
}

void solveTest() {
    int q;
    fscanf(in, "%d %d", &n, &q);
    for (int i = 0; i < n; i++)
        fscanf(in, "%lf %lf", &a[i][0], &a[i][1]);
    for (int i = 0; i < n; i++)
        for (int c = 0; c < n; c++)
            fscanf(in, "%lf", &d[i][c]);

    solve();

    for (int i = 0; i < q; i++) {
        int node1, node2;
        fscanf(in, "%d %d", &node1, &node2);
        node1--, node2--;
        fprintf(out, "%.9lf%c", ans[node1][node2], i + 1 == q ? '\n' : ' ');
    }

}

int main(void) {
	unsigned sTime = clock();
	in = fopen("PonyExpress.in", "rt");
	out = fopen("PonyExpress.out", "wt");

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
