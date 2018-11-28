// VSCF.cpp : Defines the entry point for the console application.
//
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define M_PI 3.14159265358979323846
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i)  decltype(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define st first
#define ND second
#define nd second
#define SZ(x) (int)x.size()
#define SIZE(x) SZ(x)
#define ALL(c) c.begin(),c.end()
#define MAXN 1000010
typedef long double LD;
typedef vector<int> VI;

template<class TH> void _dbg(const char *sdbg, TH h) { cerr << sdbg << "=" << h << "\n"; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
	while (*sdbg != ',')cerr << *sdbg++; cerr << "=" << h << ","; _dbg(sdbg + 1, a...);
}

template<class T> ostream &operator<<(ostream &os, vector<T> V) {
	os << "["; for (auto vv : V)os << vv << ","; return os << "]";
}

template<class L, class R> ostream &operator<<(ostream &os, pair<L, R> P) {
	return os << "(" << P.st << "," << P.nd << ")";
}

class MinCostFlow {
	struct MCEdge { int to, cost, flow; MCEdge* next; };
	const int Infty = 1e9 + 100;
	vector<vector<MCEdge*>> adjList;
	int N, Source, Sink;
	VI dist;
	vector<MCEdge*> prev, Edges;

	bool bellman_improve() {
		bool result = false;
		REP(v, N) {
			for (MCEdge* E : adjList[v]) {
				int s = E->to; if (!E->flow) { continue; }
				int newDist = dist[v] + E->cost;
				if (newDist < dist[s]) {
					dist[s] = newDist;
					prev[s] = E->next;
					result = true;
				}
			}
		}
		return result;
	}
	void bellman_shortest_path() {
		fill(ALL(dist), Infty); dist[Source] = 0;
		int maxImprove = N; while (bellman_improve() && maxImprove--);
	}
	int reduce_cost() {
		REP(v, N) { for (MCEdge* E : adjList[v]) { E->cost += dist[v] - dist[E->to]; } }
		return dist[Sink];
	}
	void dijkstra_shortest_path() {
		fill(ALL(dist), Infty); dist[Source] = 0;
		priority_queue<PII> Q; Q.push(make_pair(0, Source));

		while (!Q.empty()) {
			int dst = -Q.top().st, v = Q.top().nd; Q.pop();
			if (dst != dist[v]) { continue; }
			for (MCEdge* E : adjList[v]) {
				int s = E->to;
				if (!E->flow) { continue; }
				int newDist = dist[v] + E->cost;
				if (newDist < dist[s]) {
					dist[s] = newDist;
					prev[s] = E->next;
					Q.push({ -newDist, s });
				}
			}
		}
	}
public:
	MinCostFlow() {}
	MinCostFlow(int _N) : N(_N), dist(_N), prev(_N), adjList(_N) {}
	~MinCostFlow() { for (MCEdge* E : Edges) { delete E; } }
	int numEdges = 0;
	void add_edge(int u, int v, int flow, int cost) {
		numEdges++;
		MCEdge *E1 = new MCEdge{ v, cost, flow }, *E2 = new MCEdge{ u, -cost, 0 };
		Edges.PB(E1); Edges.PB(E2);
		E1->next = E2; E2->next = E1;
		adjList[u].PB(E1); adjList[v].PB(E2);
	}

	PII get_min_cost_flow(int s, int t) {
		Source = s; Sink = t;
		int cost = 0, flow = 0;
		bellman_shortest_path();
		if (dist[Sink] > Infty / 2) { return{ 0,0 }; }
		int sinkCost = reduce_cost();

		while (true) {
			dijkstra_shortest_path();
			if (dist[Sink] > Infty / 2) { break; }
			sinkCost += reduce_cost();

			int maxSend = Infty;
			for (int v = Sink; v != Source; v = prev[v]->to) {
				maxSend = min(maxSend, prev[v]->next->flow);
			}
			for (int v = Sink; v != Source; v = prev[v]->to) {
				MCEdge *E1 = prev[v], *E2 = E1->next;
				E1->flow += maxSend; E2->flow -= maxSend;
			}
			flow += maxSend;
			cost += maxSend * sinkCost;
		}
		return{ flow, cost };
	}
};


int32_t main(int argc, char ** argv) {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	REP(_, t) {
		cerr << _ + 1 << "\n";
		int n, c,m;
		cin >> n  >> c >> m;
		vector<PII> ticket(m);
		vector<map<int,int>> tickets(2);
		REP(i, m) {
			int p, b;
			cin >> p >> b;
			ticket[i] = { p, b };
			tickets[b - 1][p]++;
		}
		int zrodlo = 0;
		int ujscie = 1;
		int startTickets = 2;
		int sz = startTickets + m;
		MinCostFlow f(sz);
		
		REP(i, m) {
			FOR(j, i + 1, m - 1) {
				if (ticket[i].second != ticket[j].second) {
					int v1 = startTickets + i;
					int v2 = startTickets + j;
					if (ticket[i].second != 1) {
						swap(v1, v2);
					}
					if (ticket[i].first != ticket[j].first) {
						f.add_edge(v1, v2, 1, 0);
					}
					else if (ticket[i].first != 1) {
						f.add_edge(v1, v2, 1, 1);
					}
				}
			}
		}
		REP(i, m) {
			if (ticket[i].second == 2) {
				f.add_edge(startTickets + i, ujscie, 1, 0);
			}
			else {
				f.add_edge(zrodlo, startTickets + i, 1, 0);
			}
		}
		PII p = f.get_min_cost_flow(zrodlo, ujscie);
		int wagoniki = m - p.first * 2 + p.first;
		int koszt = p.second;
		cout << "Case #" << _ + 1 << ": " << wagoniki << " " << koszt << "\n";
		/*sort(ALL(ticket));
		vector<int> tickets1;
		sort(ALL(tickets[0]));
		sort(ALL(tickets[1]));*/
	}
	return 0;
}
