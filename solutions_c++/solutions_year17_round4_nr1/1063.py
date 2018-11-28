#include <cstdio>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 101;

int n, k;
int a[MAX];
char dyn[MAX][MAX][MAX][MAX][4];

char recurse(int r0, int r1, int r2, int r3, int left) {
    if (r0 == 0 && r1 == 0 && r2 == 0 && r3 == 0)
        return 0;
    char& ans = dyn[r0][r1][r2][r3][left];
    if (ans != -1)
        return ans;
    
    ans = !left;
    if (r0 > 0) ans = max((int)ans, recurse(r0 - 1, r1, r2, r3, (left - 0 + k) % k) + !left);
    if (r1 > 0) ans = max((int)ans, recurse(r0, r1 - 1, r2, r3, (left - 1 + k) % k) + !left);
    if (r2 > 0) ans = max((int)ans, recurse(r0, r1, r2 - 1, r3, (left - 2 + k) % k) + !left);
    if (r3 > 0) ans = max((int)ans, recurse(r0, r1, r2, r3 - 1, (left - 3 + k) % k) + !left);
    
    return ans;
}

void solveTest() {
    fscanf(in, "%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        fscanf(in, "%d", &a[i]);

    int cnt[4] = {0};
    for (int i = 0; i < n; i++)
        cnt[a[i] % k]++;
    memset(dyn, -1, sizeof(dyn));
    fprintf(out, "%d\n", (int)recurse(cnt[0], cnt[1], cnt[2], cnt[3], 0));
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("FreshChocolate.in", "rt");
	out = fopen("FreshChocolate.out", "wt");
	
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
