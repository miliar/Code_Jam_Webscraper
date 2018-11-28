#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
using namespace std;

struct MinCostFlow
{
	typedef int cap_t;
	typedef int cost_t;

	bool iszerocap(cap_t cap) { return cap == 0; }

	struct edge {
		int target;
		cost_t cost;
		cap_t residual_capacity;
		cap_t orig_capacity;
		size_t revid;
	};

	int n;
	vector<vector<edge>> graph;
	vector<cost_t> pi;
	bool needNormalize, ranbefore;
	int lastStart;

	MinCostFlow(int n) : graph(n), n(n), pi(n, 0), needNormalize(false), ranbefore(false) {}
	void addEdge(int s, int e, cost_t cost, cap_t cap)
	{
		if (s == e) return;
		edge forward={e, cost, cap, cap, graph[e].size()};
		edge backward={s, -cost, 0, 0, graph[s].size()};
		if (cost < 0 || ranbefore) needNormalize = true;
		graph[s].emplace_back(forward);
		graph[e].emplace_back(backward);
	}
	bool normalize(int s) {
		auto infinite_cost = numeric_limits<cost_t>::max();
		vector<cost_t> dist(n, infinite_cost);
		dist[s] = 0;
		queue<int> q;
		vector<int> v(n), relax_count(n);
		v[s] = 1; q.push(s);
		while(!q.empty()) {
			int cur = q.front();
			v[cur] = 0; q.pop();
			if (++relax_count[cur] >= n) return false;
			for (const auto &e : graph[cur]) {
				if (iszerocap(e.residual_capacity)) continue;
				auto next = e.target;
				auto ncost = dist[cur] + e.cost;
				if (dist[next] > ncost) {
					dist[next] = ncost;
					if (v[next]) continue;
					v[next] = 1; q.push(next);
				}
			}
		}
		for (int i = 0; i < n; i++) pi[i] = dist[i];
		return true;
	}

	pair<cost_t, cap_t> AugmentShortest(int s, int e, cap_t flow_limit) {
		auto infinite_cost = numeric_limits<cost_t>::max();
		auto infinite_flow = numeric_limits<cap_t>::max();
		typedef pair<cost_t, int> pq_t;
		priority_queue<pq_t, vector<pq_t>, greater<pq_t>> pq;
		vector<pair<cost_t, cap_t>> dist(n, make_pair(infinite_cost, 0));
		vector<int> from(n, -1), v(n);

		if (needNormalize || (ranbefore && lastStart != s))
			normalize(s);
		ranbefore = true;
		lastStart = s;

		dist[s] = pair<cost_t, cap_t>(0, infinite_flow);
		pq.emplace(dist[s].first, s);
		while(!pq.empty()) {
			auto cur = pq.top().second; pq.pop();
			if (v[cur]) continue;
			v[cur] = 1;
			if (cur == e) continue;
			for (const auto &e : graph[cur]) {
				auto next = e.target;
				if (v[next]) continue;
				if (iszerocap(e.residual_capacity)) continue;
				auto ncost = dist[cur].first + e.cost - pi[next] + pi[cur];
				auto nflow = min(dist[cur].second, e.residual_capacity);
				if (dist[next].first <= ncost) continue;
				dist[next] = make_pair(ncost, nflow);
				from[next] = e.revid;
				pq.emplace(dist[next].first, next);
			}
		}
		/** augment the shortest path **/
		auto p = e;
		auto pathcost = dist[p].first + pi[p] - pi[s];
		auto flow = dist[p].second;
		if (iszerocap(flow)|| (flow_limit <= 0 && pathcost >= 0)) return pair<cost_t, cap_t>(0, 0);
		if (flow_limit > 0) flow = min(flow, flow_limit);
		/* update potential */
		for (int i = 0; i < n; i++) {
			if (iszerocap(dist[i].second)) continue;
			pi[i] += dist[i].first;
		}
		while (from[p] != -1) {
			auto nedge = from[p];
			auto np = graph[p][nedge].target;
			auto fedge = graph[p][nedge].revid;
			graph[p][nedge].residual_capacity += flow;
			graph[np][fedge].residual_capacity -= flow;
			p = np;
		}
		return make_pair(pathcost * flow, flow);
	}

	pair<cost_t,cap_t> solve(int s, int e, cap_t flow_minimum = numeric_limits<cap_t>::max()) {
		cost_t total_cost = 0;
		cap_t total_flow = 0;
		for(;;) {
			auto res = AugmentShortest(s, e, flow_minimum - total_flow);
			if (res.second <= 0) break;
			total_cost += res.first;
			total_flow += res.second;
		}
		return make_pair(total_cost, total_flow);
	}
};

template <typename flow_t>
struct MaxFlowDinic {
  struct Edge {
    int next; // next vertex index
    size_t inv; // inverse edge index
    flow_t res;
  };
  int n;
  vector<vector<Edge>> graph;
  vector<int> l; // assigned level. if l[i] == 0, i is unreachable. use this if you need minimum cut.
  vector<int> q, start;
  void init(int _n) {
    n = _n;
    graph.clear();
    graph.resize(n);
  }
  void add_edge(int s, int e, flow_t cap, flow_t caprev = 0) {
    Edge forward{ e, graph[e].size(), cap };
    Edge reverse{ s, graph[s].size(), caprev };
    graph[s].push_back(forward);
    graph[e].push_back(reverse);
  }
  bool assign_level(int source, int sink) {
    memset(&l[0], 0, l.size() * sizeof(int));
    l[source] = 1;
    int t = 0;
    q[t++] = source;
    for (int h = 0; h < t && !l[sink]; ++h) {
      int cur = q[h];
      for (const auto& e : graph[cur]) {
        if (l[e.next] || e.res == 0) continue;
        l[e.next] = l[cur] + 1;
        q[t++] = e.next;
      }
    }
    return l[sink] != 0;
  }
  flow_t block_flow(int cur, int sink, flow_t current) {
    if (cur == sink) return current;
    for (int& i = start[cur]; i < (int)graph[cur].size(); ++i) {
      auto& e = graph[cur][i];
      if (e.res == 0 || l[e.next] != l[cur] + 1) continue;
      if (flow_t res = block_flow(e.next, sink, min(e.res, current))) {
        e.res -= res;
        graph[e.next][e.inv].res += res;
        return res;
      }
    }
    return 0;
  }
  flow_t solve(int source, int sink) {
    q.resize(n);  l.resize(n);  start.resize(n);
    flow_t ans = 0;
    while (assign_level(source, sink)) {
      memset(&start[0], 0, start.size() * sizeof(int));
      while (flow_t flow = block_flow(source, sink, numeric_limits<flow_t>::max()))
        ans += flow;
    }
    return ans;
  }
};

int n, c, m;
int buy[1001][2];
int tcnt[1001];

bool chk(int limit) {
	MaxFlowDinic<int> mf;
	mf.init(2 + c + n);
	for (int i = 0; i < c; ++i) {
		mf.add_edge(0, 1 + i, tcnt[i]);
		if (tcnt[i] > 0 && tcnt[i] > limit) return false;
	}
	for (int i = 0; i < m; ++i) {
		mf.add_edge(1 + buy[i][1], 1 + c + buy[i][0], 1);
	}

	for (int i = 0; i < n - 1; ++i) {
	//	for (int j = i + 1; j < n; ++j) {
		int j = i + 1;
			mf.add_edge(1 + c + j, 1 + c + i, 100000);
	//	}
	}
	for (int i = n - 1; i >= 0; --i) {
		mf.add_edge(1 + c + i, 1 + c + n, limit);
	}

	auto res = mf.solve(0, 1 + c + n);
	if (res != m) return false;
	return true;
}

pair<bool, int> chk2(int limit) {
	MinCostFlow mcf(2 + c + n);
	for (int i = 0; i < c; ++i) {
		mcf.addEdge(0, 1 + i, 0, tcnt[i]);
		if (tcnt[i] > 0 && tcnt[i] > limit) return  {false,0};
	}
	for (int i = 0; i < m; ++i) {
		mcf.addEdge(1 + buy[i][1], 1 + c + buy[i][0], 0, 1);
	}

	for (int i = 0; i < n - 1; ++i) {
		for (int j = i + 1; j < n; ++j) {
			mcf.addEdge(1 + c + j, 1 + c + i, 100, 1000000);
		}
	}
	for (int i = n - 1; i >= 0; --i) {
		mcf.addEdge(1 + c + i, 1 + c + n, 0, limit);
	}

	auto res = mcf.solve(0, 1 + c + n);
	if (res.second != m) return { false, 0 };
	return { true, res.first };
}

void proc(int caseidx) {
	scanf("%d %d %d", &n, &c, &m);
	for (int i = 0; i < c; ++i) {
		tcnt[i] = 0;
	}
	for (int i = 0; i < m; ++i) {
		scanf("%d %d", &buy[i][0], &buy[i][1]);
		buy[i][0] -= 1;
		buy[i][1] -= 1;
		tcnt[buy[i][1]] += 1;
	}

	int left = 1, right = m;
	while (left <= right) {
		int mid = (left + right) / 2;
		auto res = chk(mid);
		if (res) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	auto rr = chk2(left);
	printf("Case #%d: %d %d\n", caseidx, left, rr.second / 100);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(stderr, "%d ", i);
		proc(i);
	}
	return 0;
}