#include <cstdio>
#include <iostream>
#include <ctime>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <cassert>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define endl ('\n')
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define CLEAR(a, n) memset(a, 0, n * sizeof(a[0]))

#define IMPOSSIBLE ("IMPOSSIBLE")

clock_t __starttime = clock();

template<class T> inline void read_vector(vector<T> &a, int n) { a.clear(); a.reserve(n); T x; FOR(i, 0, n) { fastin.readInt(x); a.push_back(x); } }

void prepare_io() {
	freopen("sample.in", "r", stdin);
	freopen("sample.out", "w", stdout);
}

int get_test_count() {
	int T;
	scanf("%d", &T);
	return T;
}

void read_input(int);
void solve(int);

int main() {
	prepare_io();
	FOR(__test, 0, get_test_count()) {
		clog << "Reading test case #" << __test + 1 << endl;
		read_input(__test + 1);
		clog << "Solving test case #" << __test + 1 << endl;
		solve(__test + 1);
	}
	clock_t __endtime = clock();
	fprintf(stderr, "execution time : %.3lf s\n", (double)(__endtime - __starttime) / CLOCKS_PER_SEC);
	return 0;
}

#define PI (3.1415926535897)

struct pancake
{
	double r;
	double h;

	double top() { return r * r * PI; }
	double omot() { return 2 * PI * r  *h; }
};

int n, k;
pancake p[2000];

void read_input(int testCaseId) {
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
	{
		scanf("%lf%lf", &p[i].r, &p[i].h);
	}

	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
		{
			if (p[i].r < p[j].r)
			{
				pancake tmp = p[i]; p[i] = p[j]; p[j] = tmp;
			}
		}
}

double dp[1005][1005];

void solve(int testCaseId)
{
	memset(dp, 0, sizeof(dp));


	for (int i = 0; i < n; i++)
	{
		dp[i][1] = p[i].top() + p[i].omot();
	}

	for (int j = 2; j <= k; j++)
	{
		double maxx = -99999999999.99;
		for (int i = 0; i < n; i++)
		{
			dp[i][j] = maxx + p[i].omot();
			maxx = max(maxx, dp[i][j - 1]);
		}
	}

	double sol = 0;
	for (int i = 0; i < n; i++)
	{
		sol = max(sol, dp[i][k]);
	}

	printf("Case #%d: %.9lf\n", testCaseId, sol);
}
