#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <limits>
#include <queue>
#include <set>
using namespace std;

int n, c, m;
pair<int, int> ticket[1001];

#define pos first
#define user second

bool check(int ans){
	int cur_seat = 0, cnt = 0;
	for (int i = 0; i < m; i++){
		if (cur_seat <= ticket[i].pos){
			cnt++;
			if (cnt >= ans){
				cur_seat++;
				cnt = 0;
			}
		}
		else {
			return false;
		}
	}
	return true;
}

template<typename T>
struct NetworkFlow {
	struct Edge {
		int tar, inv;
		T cap, flow;
		Edge(int t, T c, int ii) : tar(t), cap(c), flow(0), inv(ii) {}
		T residual() const { return cap - flow; }
	};
	int V;
	vector<vector<Edge> > adj;
	vector<int> lev, edges;
	NetworkFlow(int V) : V(V), adj(V), lev(V), edges(V) {}
	void add_edge(int a, int b, T a2b, T b2a = 0) {
		int a2b_index = adj[a].size(), b2a_index = adj[b].size();
		adj[a].push_back(Edge(b, a2b, b2a_index));
		adj[b].push_back(Edge(a, b2a, a2b_index));
	}
	bool assign_lev(int source, int sink) {
		fill(lev.begin(), lev.end(), -1);
		queue<int> q; q.push(source);
		lev[source] = 0;
		while (!q.empty()) {
			int here = q.front(); q.pop();
			for (int i = 0; i < adj[here].size(); ++i) {
				const Edge& e = adj[here][i];
				if (lev[e.tar] == -1 && e.residual() > 0) {
					lev[e.tar] = lev[here] + 1;
					q.push(e.tar);
				}
			}
		}
		return lev[sink] != -1;
	}
	int push_flow(int here, int sink, T flow) {
		if (here == sink) return flow;
		for (int& i = edges[here]; i < adj[here].size(); ++i) {
			Edge& e = adj[here][i];
			if (e.residual() > 0 && lev[e.tar] == lev[here] + 1) {
				T amt = push_flow(e.tar, sink, min(flow, e.residual()));
				if (amt > 0) {
					Edge& e_inv = adj[e.tar][e.inv];
					e.flow += amt;
					e_inv.flow = -e.flow;
					return amt;
				}
			}
		}
		return 0;
	}
	T go(int source, int sink) {
		T total_flow = 0;
		while (assign_lev(source, sink)) {
			fill(edges.begin(), edges.end(), 0);
			while (true) {
				T pushed = push_flow(source, sink, numeric_limits<T>::max());
				if (pushed == 0) break;
				total_flow += pushed;
			}
		}
		return total_flow;
	}
};

int cnt[1001];
int tmp[1001][1001];
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		scanf("%d %d %d", &n,&c,&m);
		memset(cnt, 0, sizeof(cnt));
		memset(tmp, 0, sizeof(tmp));

		int low = 0, high = m, mid, ans;
		for (int i = 0; i < m; i++){
			scanf("%d %d", &ticket[i].pos, &ticket[i].user);
			ticket[i].user--; ticket[i].pos--;
			cnt[ticket[i].user]++;
			tmp[ticket[i].user][ticket[i].pos]++;
		}

		for (int i = 0; i < c; i++)
			low = max(low, cnt[i]);

		sort(ticket, ticket + m);
		
		while (low <= high){
			mid = (low + high) >> 1;
			if (check(mid)){
				ans = mid;
				high = mid - 1;
			}
			else{
				low = mid + 1;
			}
		}

		NetworkFlow<int> net(1 + c + n + 1);
		for (int i = 0; i < c; i++){
			net.add_edge(0, i + 1, cnt[i]);
		}
		for (int i = 0; i < n; i++){
			net.add_edge(1 + c + i, 1 + c + n, ans);
		}
		for (int i = 0; i < c; i++){
			for (int j = 0; j < n; j++){
				if (tmp[i][j] != 0)
					net.add_edge(1 + i, 1 + c + j, tmp[i][j]);
			}
		}

		int res = net.go(0, 1 + c + n);
		printf("Case #%d: %d %d\n", test, ans,m-res);
	}
	return 0;
}
