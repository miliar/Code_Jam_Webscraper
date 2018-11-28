#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int casenum = 1; casenum <= testcase; ++casenum) {

		int d, n;
		vector<pair<int,int>> ks;

		scanf("%d%d", &d, &n);
		ks.resize(n);
		for(int i = 0; i < n; ++i)
			scanf("%d%d", &ks[i].first, &ks[i].second);

		double slowest = 0;

		for(int i = 0; i < n; ++i) {
			int k = ks[i].first, s = ks[i].second;
			int dist = d - k;
			double goal = dist / (double)s;
			slowest = max(slowest, goal);
		}

		double ans = d / slowest;

		printf("Case #%d: %.20lf\n", casenum, ans);
	}

	return 0;
}
