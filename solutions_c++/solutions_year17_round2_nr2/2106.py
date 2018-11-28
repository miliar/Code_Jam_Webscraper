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

#define R (1)
#define Y (2)
#define O (3)
#define B (4)
#define V (5)
#define G (6)

char toChar(int n)
{
	if (n == R) return 'R';
	if (n == Y) return 'Y';
	if (n == O) return 'O'; 
	if (n == B) return 'B';
	if (n == V) return 'V';
	if (n == G) return 'G';
	while (1) cerr << "error\n";
}

int n;
int cnt[10];

void read_input(int testCaseId) {
	scanf("%d", &n);
	scanf("%d%d%d%d%d%d", &cnt[R], &cnt[O], &cnt[Y], &cnt[G], &cnt[B], &cnt[V]);
}

int path[1005];

bool findPath(int node, int i)
{
	if (i == n)
	{
		return (path[0] & path[n - 1]) == 0;
	}

	if (cnt[node] == 0) return false;

	path[i] = node;
	cnt[node]--;

	bool success = false;

	if (node == R)
	{
		if (cnt[G] > 0)
		{
			if (findPath(G, i + 1))
			{
				success = true;
			}
		}

		if (!success)
		{
			int next = (cnt[Y] >= cnt[B]) ? Y : B;
			success = findPath(next, i + 1);
		}
	}
	else if (node == Y)
	{
		if (cnt[V] > 0)
		{
			if (findPath(V, i + 1))
			{
				return true;
			}
		}

		if (!success)
		{
			int next = (cnt[B] >= cnt[R]) ? B : R;
			success = findPath(next, i + 1);
		}
	}
	else if (node == B)
	{
		if (cnt[O] > 0)
		{
			if (findPath(O, i + 1))
			{
				return true;
			}
		}

		if (!success)
		{
			int next = (cnt[R] >= cnt[Y]) ? R : Y;
			success = findPath(next, i + 1);
		}
	}
	else if (node == G)
	{
		success = findPath(R, i + 1);
	}
	else if (node == V)
	{
		success = findPath(Y, i + 1);
	}
	else if (node == O)
	{
		success = findPath(B, i + 1);
	}

	cnt[node]++;
	return success;
}

void printPath(int t)
{
	printf("Case #%d: ", t);
	for (int i = 0; i < n; i++)
	{
		printf("%c", toChar(path[i]));
	}
	printf("\n");
}

void printImpossible(int t)
{
	printf("Case #%d: %s\n", t, IMPOSSIBLE);
}

void solve(int testCaseId)
{
	for (int i = 1; i <= 6; i++)
	{
		bool succ = findPath(i, 0);
		if (succ) {
			printPath(testCaseId);
			return;
		}
	}

	printImpossible(testCaseId);
}
