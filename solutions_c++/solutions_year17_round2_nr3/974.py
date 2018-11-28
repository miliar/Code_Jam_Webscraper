#include <bits/stdc++.h>
using namespace std;

struct Node {
	int u;
	int cour;
	long long dist;
	
	Node(int node, int cour, long long dist): u(node), cour(cour), dist(dist) {}
	
	bool operator < (const Node &other) const {
		return u < other.u;
	}
};

int main() {
	int t;
	scanf ("%d", &t);
	
	for (int tc = 1; tc <= t; tc++) {
		int n, q;
		scanf ("%d %d", &n, &q);
		
		vector <int> energy(n), speed(n);
		for (int i = 0; i < n; i++) 
			scanf ("%d %d", &energy[i], &speed[i]);
		
		vector <long long> d[105];
		vector < pair <int, long long> > graph[105];
		for (int i = 0; i < n; i++) {
			d[i].resize(n);
			for (int j = 0; j < n; j++) {
				scanf ("%lld", &d[i][j]);
				if (d[i][j] > 0) {
					graph[i].push_back(make_pair(j, d[i][j]));
				}
			}
		}
		
		printf ("Case #%d:", tc);
		
		while (q--) {
			int u, vv;
			scanf ("%d %d", &u, &vv);
			u--; vv--;
			// node = u, courrier
			priority_queue < pair <double, Node> > pq;
			vector < vector <bool> > vis(n, vector <bool> (n, false));
			vector < vector <double> > dist(n, vector <double> (n, -11111111));
			
			pq.push(make_pair(0, Node(u, u, 0)));
			double ans = 1e18;
			while (!pq.empty()) {
				double cost = pq.top().first;
				Node now = pq.top().second;
				pq.pop();
				// cerr << cost << " " << now.u << " " << now.cour << endl;
				if (vis[now.u][now.cour]) continue;
				dist[now.u][now.cour] = cost;
				vis[now.u][now.cour] = true;
				
				if (now.u == vv) {
					ans = min (ans, -cost);
					break;
					//cerr << ans << " asdfsdafasd" << endl;
				}
				
				for (pair <int, long long> v: graph[now.u]) {
					if (!vis[v.first][now.cour] && now.dist + v.second <= energy[now.cour]) {
						double time = 1.0 * v.second / speed[now.cour];
						pq.push(make_pair(cost - time, Node(v.first, now.cour, now.dist + v.second)));
					}
					
					if (now.u != now.cour && !vis[v.first][now.u] && v.second <= energy[now.u]) {
						double time = 1.0 * v.second / speed[now.u];
						pq.push(make_pair(cost - time, Node(v.first, now.u, v.second)));
					}
				}
			}
			
			cout << setprecision(15) << fixed << " " << ans;
		}
		
		cout << endl;
	}
	
	
	return 0;
}