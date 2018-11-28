#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;

const ll INF = numeric_limits<ll>::max();

class min_cost_flow {
	struct edge {
        int to;
        ll flow, cap, cost;
    };
	int n; vector<edge> edges; vvi g;
	vi pred, pred_edge;

	bool levit(int s, int t) {
		vi id(n, 0);
		vll dist(n, INF);  dist[s] = 0;
		deque<int> q;  q.push_back(s);
		while (!q.empty()) {
			int v = q.front(); q.pop_front();
			id[v] = 2;
			for (auto i : g[v]) {
				auto& e = edges[i];
				if (e.flow < e.cap && dist[v] + e.cost < dist[e.to]) {
					dist[e.to] = dist[v] + e.cost;
					if (id[e.to] == 0) q.push_back(e.to);
					else if (id[e.to] == 2) q.push_front(e.to);
					id[e.to] = 1;
					pred[e.to] = v;
					pred_edge[e.to] = i;
				}
			}
		}
		return dist[t] < INF;
	}

	pair<ll, ll> augment(int s, int t, ll cap) {
		ll flow = cap, cost = 0;
		for (int v = t; v != s; v = pred[v]) {
			int pe = pred_edge[v];
			flow = min(flow, edges[pe].cap - edges[pe].flow);
		}
		for (int v = t; v != s; v = pred[v]) {
			int pe = pred_edge[v], rev = pe ^ 1;
			edges[pe].flow += flow;
			edges[rev].flow -= flow;
			cost += edges[pe].cost * flow;
		}
		return {flow, cost};
	}

 public:
 	// Initialise a flow network with n nodes
 	min_cost_flow(int n) : n(n), g(n), pred(n), pred_edge(n) { }

	// Add a directed edge with capacity and cost from node u to node v
	// Returns the index of the edge.
    int add_edge(int u, int v, ll cap, ll cost) {
        g[u].push_back( (int) edges.size() );
        edges.push_back({v, 0, cap, cost});
        g[v].push_back( (int) edges.size() );
        edges.push_back({u, 0, 0, -cost});
		return (int)edges.size() - 2;
    }

	// Returns a reference to the given edge. Useful for modifying
	// capacities and costs or inspecting final flow values.
	edge& get_edge(int i) { return edges[i]; }

	// Find the minimum cost to send K units of flow from s to t
	pair<ll, ll> flow(int s, int t, ll K) {
		for (auto& e : edges) e.flow = 0;
		ll flow = 0, cost = 0;
		while (flow < K && levit(s, t)) {
			auto res = augment(s, t, K - flow);
			flow += res.first;
			cost += res.second;
		}
		return {flow, cost};
	}
};


#define debug(x) cerr << #x << " = " << (x) << endl;
template<typename T>
ostream& operator<<(ostream& o, vector<T>& v) {
    for (auto& x : v) o << x << ' ';
    return o;
}

int N, C, M;
bool vcmp(const vi& v1, const vi& v2){
    if (v1.size() != v2.size()) return v1.size() > v2.size();
    return v1 < v2;
}

int rides(vvi tix, int& s){
    s = 0;
    int ans = 0;
    int tot = M;
    while (tot) {
        ans++;
        sort(tix.begin(), tix.end(), vcmp);
        vi seats(N, 0);
        for (vi& v : tix){
            if (v.empty()) break;
            for (int i = 0; i < (int)v.size(); i++) {
                int ptr = v[i];
                while (ptr >= 0 && seats[ptr]) ptr--;
                if (ptr != -1) {
                    seats[ptr] = 1;
                    tot--;
                    if (ptr != v[i]) s++;
                    v.erase(v.begin() + i);
                    break;
                }
            }
        }
    }
    return ans;
}

void solve(){
    vvi tix(C);
    for (int i = 0; i < M; i++){
        int p, b; cin >> p >> b;
        p--; b--;
        tix[b].push_back(p);
    }
    for (int i = 0; i < C; i++) sort(tix[i].begin(), tix[i].end());
    int s;
    int R = rides(tix, s);

    cout << R << ' ' << s << endl;
}

void solve_small(){
    vi A, B;
    for (int i = 0; i < M; i++){
        int p, b; cin >> p >> b;
        p--; b--;
        if (b == 0) A.push_back(p);
        else B.push_back(p);
    }



    int n = A.size(), m = B.size();
    min_cost_flow mcf(n + m + 2);

    for (int i = 0; i < n; i++)
        mcf.add_edge(n+m, i, 1, 0);
    for (int j = 0; j < m; j++)
        mcf.add_edge(n+j, n+m+1, 1, 0);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (A[i] != B[j] || A[i] != 0)
                mcf.add_edge(i, n+j, 1, (A[i] == B[j]));
        }
    }
    int R, S;
    tie(R, S) = mcf.flow(n + m, n + m + 1, INF);

    R += (n + m) - 2*R;
    cout << R << ' ' << S << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        cin >> N >> C >> M;
        if (C == 2) solve_small();
        else solve();
    }

}
