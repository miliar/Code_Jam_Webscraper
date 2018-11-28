#include <cstdio>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 1024;

long long smarty(long long num) {
    if (num < 10)
        return num;
    
    char a[32];
    sprintf(a, "%lld", num);
    int len = (int)strlen(a);

    long long ans = 0;
    for (int i = 0; i < len - 1; i++)
        ans = ans * 10 + 9;
    
    char smallest = '9';
    for (int i = len - 1; i >= 0; i--) {
        smallest = min(smallest, a[i]);
        if (a[i] > smallest) {
            a[i]--;
            smallest = a[i];
            for (int c = i + 1; c < len; c++)
                a[c] = '9';
        }
    }
    
    if (a[0] == '0' && len > 1)
        return ans;
    sscanf(a, "%lld", &ans);
    return ans;
}

long long dummy(long long num) {
    if (num < 10)
        return num;
    for (long long cand = num; cand > 0; cand--) {
        int last = 10;
        bool okay = true;
        for (long long tmp = cand; tmp > 0; tmp /= 10) {
            if (last < tmp % 10) {
                okay = false;
                break;
            }
            last = tmp % 10;
        }
        if (okay)
            return cand;
    }
    return -1;
}

void solveTest() {
    long long num;
    fscanf(in, "%lld", &num);
    fprintf(out, "%lld\n", smarty(num));
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("TidyNumbers.in", "rt");
	out = fopen("TidyNumbers.out", "wt");
	
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
