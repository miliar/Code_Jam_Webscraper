#include <bits/stdc++.h>

#define SZ(a) (int)a.size()
#define PB push_back

using namespace std;

typedef long long ll;

ll Dist[110][110];
double Time[110][110];

ll E[110];
int S[110];

struct node {
	int v;
	ll d;
	
	node() {}
	node(int v, ll d): v(v), d(d) {}
	
	bool operator<(const node& oth) const {
		return d>oth.d;
	}
};

struct dij_node {
	int v;
	double d;
	
	dij_node() {}
	dij_node(int v, double d): v(v), d(d) {}
	
	bool operator<(const dij_node& oth) const {
		return d>oth.d;
	}
};

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d:", tt);
		
		int N,Q;
		scanf("%d%d", &N, &Q);
		
		for(int i = 0; i < N; i++) {
			scanf("%lld %d", E+i, S+i);
		}
		
		vector<vector<node> > V(N);
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				ll inp;
				scanf("%lld", &inp);
				if(inp >= 0) V[i].PB(node(j,inp));
				if(i==j) Dist[i][j] = 0;
				else Dist[i][j] = 1000000000000LL;
			}
		}
		
		bool change = true;
		while(change) {
			change = false;
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					for(node edge : V[j]) {
						if(Dist[i][edge.v] > Dist[i][j]+edge.d) {
							Dist[i][edge.v] = Dist[i][j]+edge.d;
							change = true;
						}
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(Dist[i][j] <= E[i]) {
					Time[i][j] = static_cast<double>(Dist[i][j])/S[i];
				} else {
					Time[i][j] = -10.0;
				}
			}
		}
		
		while(Q--) {
			int a,b;
			scanf("%d %d", &a, &b);
			a--; b--;
			
			vector<bool> vis(N,false);
			priority_queue<dij_node> pq;
			pq.push(dij_node(a,0.0));
			
			while(!pq.empty()) {
				dij_node cur = pq.top();
				pq.pop();
				if(cur.v == b) {
					printf(" %.7lf", cur.d);
					break;
				}
				if(vis[cur.v]) continue;
				vis[cur.v] = true;
				
				for(int j = 0; j < N; j++) {
					if(!vis[j] && Time[cur.v][j] >= -0.1) {
						pq.push(dij_node(j, cur.d + Time[cur.v][j]));
					}
				}
			}
		}
		printf("\n");
	}
	
	return 0;
}
