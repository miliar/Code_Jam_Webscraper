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

long long n, k;

void read_input(int testCaseId) {
	scanf("%lld%lld", &n, &k);
}

struct Segment {
	long long start, end, length;

	Segment(long long _start, long long _end)
	{
		start = _start;
		end = _end;
		length = end - start + 1;
	}

	long long middle() { return (start + end) / 2; }
};

struct segment_compare {
	bool operator() (const Segment& lhs, const Segment& rhs) const {
		if (lhs.length != rhs.length)
		{
			return lhs.length < rhs.length;
		}
		else
		{
			return lhs.start > rhs.start;
		}
	}
};

priority_queue<Segment, vector<Segment>, segment_compare> s;

void solve(int testCaseId)
{
	while (!s.empty()) s.pop();
	s.push(Segment(1, n));

	Segment lastSegment(-1, -1);
	for (int i = 0; i < k; i++)
	{
		Segment top = s.top();
		s.pop();

		Segment leftSegment = Segment(top.start, top.middle() - 1);
		if (leftSegment.length > 0)
		{
			s.push(leftSegment);
		}
		Segment rightSegment = Segment(top.middle() + 1, top.end);
		if (rightSegment.length > 0)
		{
			s.push(rightSegment);
		}

		lastSegment = top;
	}

	printf("Case #%d: %lld %lld\n", testCaseId, lastSegment.end - lastSegment.middle(), lastSegment.middle() - lastSegment.start);
}
