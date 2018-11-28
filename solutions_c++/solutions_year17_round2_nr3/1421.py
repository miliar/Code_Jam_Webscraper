#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
typedef pair<ii, double> iid;
const int MAXN = 100, MAXL = 1000010;
const lli INF = 2000000000000;

class mycomparison
{
	public:
	mycomparison() {}
	bool operator() (const iid& lhs, const iid& rhs) const {
		return lhs.second > rhs.second;
	}
};

int n, q;
ii horses[MAXN]; // distance, speed
lli adj[MAXN][MAXN];

void floyd();
lli dist[MAXN][MAXN];

void clean_visi();
double dijkstra(int start, int end);
double visi[MAXN][MAXN];

int main() {
	// freopen("C-small-attempt0.in", "r", stdin);
	// freopen("output-small.txt", "w", stdout); 

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		printf("Case #%d: ", test);

		scanf("%d %d", &n, &q);
		for(int i=0; i<n; i++) {
			scanf("%lld %lld", &horses[i].first, &horses[i].second);
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				scanf("%lld", &adj[i][j]);
			}
		}
		floyd();

		for(int i=0; i<q; i++) {
			int start, end;
			scanf("%d %d", &start, &end);

			clean_visi();
			printf("%.6lf%c", dijkstra(start-1, end-1), i == q-1 ? '\n' : ' ');
		}
	}
}

double dijkstra(int start, int end) {
	priority_queue<iid, vector<iid>, mycomparison> q;
	q.push(iid(ii(start, start), 0.0f));

	while(!q.empty()) {
		iid u = q.top(); q.pop();
		int city = u.first.first;
		int horse = u.first.second;
		double time = u.second;

		if(city == end) {
			return time;
		}

		if(visi[city][horse] != -1.0f) {
			continue;
		}
		visi[city][horse] = time;

		lli can_run = horses[horse].first - dist[horse][city];
		for(int i=0; i<n; i++) if(i != city and adj[city][i] != -1) {
			q.push(iid(ii(i, city), time + double(adj[city][i]) / double(horses[city].second)));

			if(can_run >= adj[city][i]) {
				q.push(iid(ii(i, horse), time + double(adj[city][i]) / double(horses[horse].second)));
			}
		}
	}

	return 0.0;
}

void floyd() {
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			dist[i][j] = adj[i][j];

			if(dist[i][j] == -1) {
				dist[i][j] = INF;
			}
		}
		dist[i][i] = 0;
	}

	for(int k=0; k<n; k++) {
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(dist[i][k] + dist[k][j] < dist[i][j]) {
					dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}
	}

	// for(int i=0; i<n; i++) {
	// 	for(int j=0; j<n; j++) {
	// 		printf("%lld%c", dist[i][j], j == n-1 ? '\n' : ' ');
	// 	}
	// }
}

void clean_visi() {
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			visi[i][j] = -1.0f;
		}
	}
}
