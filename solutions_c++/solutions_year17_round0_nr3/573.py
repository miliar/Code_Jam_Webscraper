#include <cstdio>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 1048576;

long long n, k;

void smarty() {
    priority_queue <int> q;
    q.push(n);
    
    for (int i = 0; i < k; i++) {
        int size = q.top(); q.pop();
        q.push(size / 2);
        q.push(size / 2 - !(size % 2));
        if (i == k - 1) {
            fprintf(out, "%d %d\n", size / 2, size / 2 - !(size % 2));
        }
    }
}

void solve() {
    map <long long, long long> q;
    q[n] = 1;
    while (k > 0) {
        auto it = q.end();
        it--;
        
        long long size = it->first;
        long long count = it->second;
        if (k <= count) {
            fprintf(out, "%lld %lld\n", size / 2, size / 2 - !(size % 2));
            return;
        } else {
            k -= count;
            q.erase(it);
            q[size / 2] += count;
            q[size / 2 - !(size % 2)] += count;
        }
    }
}

void solveTest() {
    fscanf(in, "%lld %lld", &n, &k);
    solve();
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("BathroomStalls.in", "rt");
	out = fopen("BathroomStalls.out", "wt");
	
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
