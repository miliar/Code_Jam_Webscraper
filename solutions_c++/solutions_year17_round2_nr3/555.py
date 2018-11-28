#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

const int inf = (int)1.05e9;

int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int casenum = 1; casenum <= testcase; ++casenum) {

		int n, q;
		vector<pair<int,int>> es;
		vector<vector<int>> d;
		vector<pair<int,int>> uv;

		scanf("%d%d", &n, &q);
		es.resize(n);
		d.resize(n);
		uv.resize(q);
		for(auto& x : d)
			x.resize(n);
		for(int i = 0; i < n; ++i)
			scanf("%d%d", &es[i].first, &es[i].second);
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j)
				scanf("%d", &d[i][j]);
		}
		for(int i = 0; i < q; ++i) {
			scanf("%d%d", &uv[i].first, &uv[i].second);
			uv[i].first -= 1;
			uv[i].second -= 1;
		}

		vector<vector<int>> dists;

		dists.resize(n);
		for(auto& x : dists)
			x.resize(n, inf);
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				if(d[i][j] >= 0)
					dists[i][j] = d[i][j];
				if(i == j)
					dists[i][j] = 0;
			}
		}

		for(int k = 0; k < n; ++k) {
			for(int i = 0; i < n; ++i) {
				for(int j = 0; j < n; ++j)
					dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j]);
			}
		}

		vector<double> ans_list;

		for(int query = 0; query < q; ++query) {

			const int u = uv[query].first, v = uv[query].second;

			vector<double> cost(n, inf);
			vector<bool> visited(n, false);
			priority_queue<pair<double,int>> que;

			que.push({-0, u});

			while(!que.empty()) {

				const double c = -que.top().first;
				const int from = que.top().second;
				const int max_dist = es[from].first;
				const int speed = es[from].second;

				que.pop();

				if(visited[from])
					continue;
				visited[from] = true;
				cost[from] = c;

				for(int next = 0; next < n; ++next) {
					const int way = dists[from][next];
					if(way > max_dist || visited[next])
						continue;
					double x = way / (double)speed;
					que.push({-(x + c), next});
				}
			}

			double ans = cost[v];
			assert(visited[v]);

			ans_list.push_back(ans);
		}

		printf("Case #%d:", casenum);
		for(int i = 0; i < q; ++i)
			printf(" %.20lf", ans_list[i]);
		printf("\n");
	}

	return 0;
}
