#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int> p1, pair<int, int> p2)
{
	return p1.first > p2.first;
}

double solve(vector< pair<int, int> > horses, int d)
{
	double maxTime = 0.0;
	for (int i = 0; i < horses.size(); i++) {
		maxTime = max(maxTime, 1.0 * (d - horses[i].first) / horses[i].second);
	}
	return d / maxTime;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int d, n;
		scanf("%d %d", &d, &n);
		vector< pair<int, int> > horses;
		for (int j = 0; j < n; j++) {
			int k, s;
			scanf("%d %d", &k, &s);
			horses.push_back(make_pair(k, s));
		}
		sort(horses.begin(), horses.end(), cmp);
		double result = solve(horses, d);
		printf("Case #%d: %lf\n", i, result);
	}
	return 0;
}
