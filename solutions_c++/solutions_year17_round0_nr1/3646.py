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
		read_input(__test + 1);
		solve(__test + 1);
	}
	clock_t __endtime = clock();
	fprintf(stderr, "execution time : %.3lf s\n", (double)(__endtime - __starttime) / CLOCKS_PER_SEC);
	return 0;
}


int n, k;
int a[1005];

void read_input(int testCaseId) {
	char s[1005];
	scanf("%s %d", s, &k);

	n = strlen(s);
	for (int i = 0; i < n; i++)
	{
		a[i] = (s[i] == '+') ? 1 : 0;
	}
}

void solve(int testCaseId) {
	int sol = 0;
	for (int i = 0; i < n - k + 1; i++)
	{
		if (a[i] == 0)
		{
			sol++;
			for (int j = 0; j < k; j++)
			{
				a[i + j] = 1 - a[i + j];
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		if (a[i] == 0)
		{
			sol = -1;
		}
	}

	printf("Case #%d: ", testCaseId);
	if (sol < 0)
	{
		printf("%s", IMPOSSIBLE);
	}
	else
	{
		printf("%d", sol);
	}
	printf("\n");
}
