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

struct interval
{
	int start, end;
	int owner;

	bool isDirty;

	int duration() {
		int dd = end - start;
		if (dd < 0) dd += 24 * 60;
		return dd;
	}
};

int n, m;

int total;
interval t[300];

void read_input(int testCaseId) {
	scanf("%d%d", &n, &m);
	total = n + m;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &t[i].start, &t[i].end);
		t[i].owner = 0;
		t[i].isDirty = false;
	}
	for (int i = n; i < n + m; i++)
	{
		scanf("%d%d", &t[i].start, &t[i].end);
		t[i].owner = 1;
		t[i].isDirty = false;
	}
}

void removeDirty()
{
	int p = 0;
	for (int i = 0; i < total; i++)
	{
		if (!t[i].isDirty)
		{
			t[p++] = t[i];
		}
	}

	total = p;
}

int dist(interval a, interval b)
{
	int dist = b.start - a.end;
	if (dist < 0) dist += 24 * 60;
	return dist;
}

void solve(int testCaseId)
{
	for (int i = 0; i < total; i++)
	{
		for (int j = i + 1; j < total; j++)
		{
			if (t[i].start > t[j].start)
			{
				interval tmp = t[i]; t[i] = t[j]; t[j] = tmp;
			}
		}
	}

	int free[2];
	free[0] = free[1] = 12 * 60;
	for (int i = 0; i < total; i++)
	{
		free[t[i].owner] -= t[i].duration();
	}

	int nextMerge = -1;
	while (true)
	{
		int minDist = 999999;

		for (int i = 0; i < total; i++)
		{
			int j = (i + 1) % total;
			if (t[i].owner == t[j].owner)
			{
				int dd = dist(t[i], t[j]);
				if (dd <= free[t[i].owner] && (nextMerge < 0 || dd < minDist))
				{
					nextMerge = i;
					minDist = dd;
				}
			}
		}

		if (nextMerge >= 0)
		{
			int i = nextMerge;
			int j = (i + 1) % total;
			t[i].end = t[j].end;
			t[j].isDirty = true;
			free[t[i].owner] -= minDist;

			removeDirty();

			nextMerge = -1;
		}
		else
		{
			break;
		}
	}

	int sol = 0;

	for (int i = 0; i < total; i++)
	{
		int j = (i + 1) % total;
		if (t[i].owner == t[j].owner) {
			sol += 2;
		}
		else
		{
			sol += 1;
		}
	}

	printf("Case #%d: %d\n", testCaseId, sol);
}
