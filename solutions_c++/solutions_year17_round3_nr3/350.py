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

int n, k;
double u;
double p[105];

void read_input(int testCaseId) {
	scanf("%d%d", &n, &k);
	scanf("%lf", &u);
	for (int i = 0; i < n; i++)
	{
		scanf("%lf", p + i);
	}
}

double bins(double l, double h)
{
	if (h - l < 0.000000001) return l;

	double mid = (h + l) / 2;
	double sum = 0;
	for (int i = 0; i < n; i++)
	{
		if (p[i] < mid) sum += mid - p[i];
	}

	if (sum > u) return bins(l, mid);
	else return bins(mid, h);
}

double dp[105][105];

double calcProb()
{
	memset(dp, 0, sizeof(dp));

	dp[0][0] = p[0];
	dp[0][1] = 1 - p[0];

	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			dp[i][j] = p[i] * dp[i - 1][j];
			if (j > 0)
			{
				dp[i][j] += (1 - p[i]) * dp[i - 1][j - 1];
			}
		}
	}

	double sol = 0;
	for (int i = 0; i <= n - k; i++)
	{
		sol += dp[n - 1][i];
	}
	return sol;
}

void solve(int testCaseId)
{
	double t = bins(0, 1);
	for (int i = 0; i < n; i++)
	{
		if (p[i] < t) p[i] = t;
	}

	double sol = calcProb();
	printf("Case #%d: %.7lf\n", testCaseId, sol);
}
