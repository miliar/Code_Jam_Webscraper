#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 1024;

int n, k;
char a[MAX];

void solveTest() {
    fscanf(in, "%s %d", a, &k);
    n = (int)strlen(a);

    int ans = 0;
    for (int i = 0; i + k <= n; i++) {
        if (a[i] == '-') {
            ans++;
            for (int c = 0; c < k; c++)
                a[i + c] = (a[i + c] == '-' ? '+' : '-');
        }
    }
    for (int i = 0; i < n; i++) {
        if (a[i] != '+') {
            ans = -1;
        }
    }
    if (ans == -1) {
        fprintf(out, "IMPOSSIBLE\n");
    } else {
        fprintf(out, "%d\n", ans);
    }
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("OversizedPancakeFlipper.in", "rt");
	out = fopen("OversizedPancakeFlipper.out", "wt");
	
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
