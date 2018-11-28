#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 1024;

int n;
int r, o, y, g, b, v;

void solveTest() {
    fscanf(in, "%d", &n);
    fscanf(in, "%d %d %d %d %d %d", &r, &o, &y, &g, &b, &v);
    fprintf(stderr, "R = %d, O = %d, Y = %d, G = %d, B = %d, V = %d\n", r, o, y, g, b, v);

    priority_queue < pair <float, char> > q;
    if (r != 0) q.push(make_pair(r, 'R'));
    if (o != 0) q.push(make_pair(o, 'O'));
    if (y != 0) q.push(make_pair(y, 'Y'));
    if (g != 0) q.push(make_pair(g, 'G'));
    if (b != 0) q.push(make_pair(b, 'B'));
    if (v != 0) q.push(make_pair(v, 'V'));

    string ans;
    while (!q.empty()) {
        pair <float, char> t = q.top(); q.pop();
        if (ans.empty() || ans.back() != t.second) {
            // Offset the first character
            if (ans.size() == 0)
                t.first += 0.5;

            ans += t.second;
            t.first -= 1.0;
            if (t.first > 0.6)
                q.push(t);
        } else {
            if (q.empty()) {
                ans = "IMPOSSIBLE";
                break;
            } else {
                pair <float, char> w = q.top(); q.pop();
                ans += w.second;
                w.first -= 1.0;
                if (w.first > 0.6)
                    q.push(w);
                ans += t.second;
                t.first -= 1.0;
                if (t.first > 0.6)
                    q.push(t);
            }
        }
    }
    if (ans[0] == ans.back()) {
        ans = "IMPOSSIBLE";
    }
    fprintf(out, "%s\n", ans.c_str());
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("StableNeighbors.in", "rt");
	out = fopen("StableNeighbors.out", "wt");

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
