#include <bits/stdc++.h>

using namespace std;

#define int long long

int G[1000][1000];
int D[1000][1000];
int Max[1000], Speed[1000];
long double DP[1000][1000];
int n;

struct PNode {
	int node, from;
	long double dist;

	PNode(int node, int from, long double dist) :
		node(node), from(from), dist(dist) {}

	bool operator<(const PNode &oth) const {
		return dist > oth.dist;
	} 
};

long double Solve(int u, int v) {
	--u; --v;
	priority_queue<PNode> pq;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j)
			DP[i][j] = -1;
	DP[u][u] = 0;

	pq.emplace(u, u, 0);
	while(!pq.empty()) {
		auto top = pq.top();
		pq.pop();

		int node = top.node, from = top.from;


		if(abs(top.dist - DP[node][from]) > 1e-12) continue;
		if(top.node == v) return top.dist;

		// Change horse
		if(DP[node][node] == -1 || DP[node][node] > DP[node][from] + 1e-12) {
			DP[node][node] = DP[node][from];
			pq.emplace(node, node, DP[node][node]);
		}

		// Go to neigh
		int rem = Max[from] - D[from][node];
		for(int vec = 0; vec < n; ++vec) {
			if(D[node][vec] == -1 || D[node][vec] > rem)
				continue;
			if(vec == node) continue;

			long double have = DP[node][from] + 1.0 * D[node][vec] / Speed[from];
			if(DP[vec][from] == -1 || DP[vec][from] > have + 1e-12) {
				DP[vec][from] = have;
				pq.emplace(vec, from, have);
			} 
		}
	}

	assert(false);
}

void Solve() {
	int q;
	cin >> n >> q;

	for(int i = 0; i < n; ++i)
		cin >> Max[i] >> Speed[i];

	memset(D, -1, sizeof(D));
	for(int i = 0; i < n; ++i)
	for(int j = 0; j < n; ++j) {
		cin >> G[i][j];
		D[i][j] = G[i][j];
	}

	for(int i = 0; i < n; ++i)
		D[i][i] = 0;

	for(int k = 0; k < n; ++k)
	for(int i = 0; i < n; ++i)
	for(int j = 0; j < n; ++j) {
		if(D[i][k] == -1 || D[k][j] == -1) continue;
		if(D[i][j] == -1 || D[i][j] > D[i][k] + D[k][j])
			D[i][j] = D[i][k] + D[k][j];
	}
/*
	for(int i = 0; i < n; ++i, cerr << endl)
		for(int j = 0; j < n; ++j)
			cerr << D[i][j] << " ";*/

	while(q--) {
		int u, v;
		cin >> u >> v;
		cout << Solve(u, v) << " ";
	}
	cout << endl;

}

int32_t main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(15);
	for(int tt = 1; tt <= t; ++tt) {
		cout << "Case #" << tt << ": ";
		Solve();
		cerr << "Done case #" << tt << endl;
	}
	return 0;
}