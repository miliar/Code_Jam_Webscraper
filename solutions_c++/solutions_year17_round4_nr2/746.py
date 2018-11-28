#include <bits/stdc++.h>
using namespace std;
/***********************************************/
/* Dear online judge:
 * I've read the problem, and tried to solve it.
 * Even if you don't accept my solution, you should respect my effort.
 * I hope my code compiles and gets accepted.
 *  ___  __     _______    _______      
 * |\  \|\  \  |\  ___ \  |\  ___ \     
 * \ \  \/  /|_\ \   __/| \ \   __/|    
 *  \ \   ___  \\ \  \_|/__\ \  \_|/__  
 *   \ \  \\ \  \\ \  \_|\ \\ \  \_|\ \ 
 *    \ \__\\ \__\\ \_______\\ \_______\
 *     \|__| \|__| \|_______| \|_______|
 */
const long long mod = 1000000007;

const int mxN = 2010;
const int inf = 1000000010;
struct Edge {
	int to, cost, cap, flow, backEdge;
};

struct MCMF {
	int s, t, n;
	vector<Edge> g[mxN];

	MCMF(int _s, int _t, int _n) {
		s = _s;
		t = _t;
		n = _n;
	}

	void addEdge(int u, int v, int cost, int cap) {
		Edge e1 = {v, cost, cap, 0, (int)g[v].size()};
		Edge e2 = {u, -cost, 0, 0, (int)g[u].size()};
		g[u].push_back(e1);
		g[v].push_back(e2);
	}

	pair<int,int> minCostMaxFlow() {
		int flow,cost;
		flow = cost = 0;
		vector<int> from(n);
		vector<int> from_edge(n);
		vector<int> d(n);
		set<pair<int,int> > q;
		while (true) {
			for (int i = 0; i < n; i++)
				d[i] = inf, from[i] = -1;
			q.clear();
			d[s] = 0;
			q.insert({0,s});
			while (!q.empty()) {
				int v = q.begin()->second;
				q.erase(q.begin());
				for(int i = 0;i < (int)g[v].size();i++) {
					Edge e = g[v][i];
					if (e.flow >= e.cap || d[e.to] <= d[v] + e.cost)
						continue;
					int to = e.to;
					from[to] = v;
					from_edge[to] = i;
					q.erase({d[to],to});
					d[to] = d[v] + e.cost;
					q.insert({d[to],to});
				}
			}
			if (d[t] == inf)
				break;
			int it = t;
			int addflow = inf;
			while (it != s) {
				addflow = min(addflow, g[from[it]][from_edge[it]].cap - g[from[it]][from_edge[it]].flow);
				it = from[it];
			}
			it = t;
			while (it != s) {
				g[from[it]][from_edge[it]].flow += addflow;
				g[it][g[from[it]][from_edge[it]].backEdge].flow -= addflow;
				cost += g[from[it]][from_edge[it]].cost * addflow;
				it = from[it];
			}
			flow += addflow;
		}
		return {flow,cost};
	} 
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);


	int T,C = 1;
	cin>>T;
	while(T--) {

		cout<<"Case #"<<C++<<": ";

		int N,C,M;
		cin>>N>>C>>M;
		vector<pair<int,int> > t(M);
		vector<int> inC(C);
		for(int i = 0;i < M;i++) {
			cin>>t[i].first>>t[i].second;
			t[i].first--,t[i].second--;
			inC[t[i].second]++;
		}
		int lo = *max_element(inC.begin(),inC.end()),hi = M,res = -1,with = 0;
		while(lo <= hi) {
			int md = (lo + hi)>>1;
			MCMF mcmf = MCMF(N+C,N+C+1,N+C+2);
			for(int i = 0;i < C;i++)
				mcmf.addEdge(N+C,i,0,inC[i]);
			for(int i = 0;i < M;i++) {
				mcmf.addEdge(t[i].second,C + t[i].first,0,1);
				for(int p = 0;p < t[i].first;p++)
					mcmf.addEdge(t[i].second,C + p,1,1);
			}
			for(int i = 0;i < N;i++) {
				mcmf.addEdge(C + i,N + C + 1,0,md);
			}
			auto cur = mcmf.minCostMaxFlow();
			if(cur.first == M) {
				res = md,with = cur.second;
				hi = md - 1;
			} else {
				lo = md + 1;
			}
		}
		cout<<res<<' '<<with<<'\n';
	}

	return 0;
}
