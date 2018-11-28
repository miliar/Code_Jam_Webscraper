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

struct Segment
{
	double start, end;
	double speed;
	
	double time()
	{
		return (end - start) / speed;
	}
};

int d;
int n;
int k[1005], s[1005];

void read_input(int testCaseId) {
	scanf("%d%d", &d, &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", k + i, s + i);
	}
}

stack<Segment> pr;

void solve(int testCaseId)
{
	while (!pr.empty()) pr.pop();

	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n; j++)
		{
			if (k[i] > k[j])
			{
				int tmp = k[i]; k[i] = k[j]; k[j] = tmp;
				int tmps = s[i]; s[i] = s[j]; s[j] = tmps;
			}
		}
	}

	Segment lastSegment;
	lastSegment.start = k[n - 1];
	lastSegment.end = d;
	lastSegment.speed = s[n - 1];
	pr.push(lastSegment);

	for (int i = n - 2; i >= 0; i--)
	{
		double posI = k[i];

		while (true)
		{
			Segment top = pr.top();

			double t = (posI - top.start) / (top.speed - s[i]);
			double posIntersection = top.start + t * top.speed;

			if (posIntersection > top.start && posIntersection < top.end)
			{
				pr.pop();

				top.start = posIntersection;
				pr.push(top);

				Segment s1;
				s1.start = k[i];
				s1.end = posIntersection;
				s1.speed = s[i];
				pr.push(s1);

				break;
			}
			else
			{
				posI += s[i] * top.time();

				pr.pop();

				if (pr.empty())
				{
					Segment ns;
					ns.start = k[i];
					ns.end = d;
					ns.speed = s[i];
					pr.push(ns);
					break;
				}
			}
		}
	}

	double totalTime = 0;
	while (!pr.empty())
	{
		totalTime += pr.top().time();
		pr.pop();
	}
	double solution = d / totalTime;

	cerr << lastSegment.time() << endl;

	printf("Case #%d: %.6lf\n", testCaseId, solution);
}
