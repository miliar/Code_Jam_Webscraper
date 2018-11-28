#include <bits/stdc++.h>
using namespace std;


typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long L;
typedef vector<L> VL;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const L INF = numeric_limits<L>::max() / 4;

struct MinCostMaxFlow {
  int N;
  VVL cap, flow, cost;
  VI found;
  VL dist, pi, width;
  VPII dad;

  MinCostMaxFlow(int N) : 
    N(N), cap(N, VL(N)), flow(N, VL(N)), cost(N, VL(N)), 
    found(N), dist(N), pi(N), width(N), dad(N) {}
  
  void AddEdge(int from, int to, L cap, L cost) {
    this->cap[from][to] = cap;
    this->cost[from][to] = cost;
  }
  
  void Relax(int s, int k, L cap, L cost, int dir) {
    L val = dist[s] + pi[s] - pi[k] + cost;
    if (cap && val < dist[k]) {
      dist[k] = val;
      dad[k] = make_pair(s, dir);
      width[k] = min(cap, width[s]);
    }
  }

  L Dijkstra(int s, int t) {
    fill(found.begin(), found.end(), false);
    fill(dist.begin(), dist.end(), INF);
    fill(width.begin(), width.end(), 0);
    dist[s] = 0;
    width[s] = INF;
    
    while (s != -1) {
      int best = -1;
      found[s] = true;
      for (int k = 0; k < N; k++) {
        if (found[k]) continue;
        Relax(s, k, cap[s][k] - flow[s][k], cost[s][k], 1);
        Relax(s, k, flow[k][s], -cost[k][s], -1);
        if (best == -1 || dist[k] < dist[best]) best = k;
      }
      s = best;
    }

    for (int k = 0; k < N; k++)
      pi[k] = min(pi[k] + dist[k], INF);
    return width[t];
  }

  pair<L, L> GetMaxFlow(int s, int t) {
    L totflow = 0, totcost = 0;
    while (L amt = Dijkstra(s, t)) {
      totflow += amt;
      for (int x = t; x != s; x = dad[x].first) {
        if (dad[x].second == 1) {
          flow[dad[x].first][x] += amt;
          totcost += amt * cost[dad[x].first][x];
        } else {
          flow[x][dad[x].first] -= amt;
          totcost -= amt * cost[x][dad[x].first];
        }
      }
    }
    return make_pair(totflow, totcost);
  }
};

void code() {
	int N, C, M;
	cin >> N >> C >> M;

	vector<int> P(M);
	vector<int> B(M);
	vector<int> count(C, 0);
	vector<int> poscount(N, 0);

	int minrides = 1;
	for(int i = 0; i < M; i++) {
		cin >> P[i] >> B[i];
		P[i]--;
		B[i]--;
		poscount[P[i]]++;
		count[B[i]]++;
		minrides = max(minrides, count[B[i]]);
	}

	int lo = minrides;
	int hi = 1001;
	int bestrides = INT_MAX;
	int best = INT_MAX;
	while (lo + 1 < hi) {
		int mid = (lo+hi)/2;
		// construct graph

		int totalverts = 2 + N;
		MinCostMaxFlow mcmf(totalverts);

		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				mcmf.AddEdge(j, i, 1000, 1);
			}
		}

		for (int i = 0; i < N; i++) {
			mcmf.AddEdge(N, i, poscount[i], 0);
			mcmf.AddEdge(i, N+1, mid, 0);
		}

		pair<L, L> res = mcmf.GetMaxFlow(N, N+1);
		//fprintf(stderr, "%d %d %d %d %d\n", lo, hi, mid, res.first, res.second);
		if (res.first != M) {
			lo = mid+1;
		} else {
			hi = mid;
		}
	}
		int totalverts = 2 + N;
		MinCostMaxFlow mcmf(totalverts);

		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				mcmf.AddEdge(j, i, 1000, 1);
				//printf("%d %d %d %d\n", j, i, 1000, 1);
			}
		}

		for (int i = 0; i < N; i++) {
			mcmf.AddEdge(N, i, poscount[i], 0);
			//printf("%d %d %d %d\n", N, i, poscount[i], 0);
			mcmf.AddEdge(i, N+1, lo, 0);
			//printf("%d %d %d %d\n", i, N+1, lo, 0);
		}

		pair<L, L> res = mcmf.GetMaxFlow(N, N+1);
		//fprintf(stderr, "%d\n", res.first);
		if (res.first == M)  {
			cout << lo << " " << res.second << endl;
			return;
		}
		{
			lo = hi;
		int totalverts = 2 + N;
		MinCostMaxFlow mcmf(totalverts);

		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				mcmf.AddEdge(j, i, 1000, 1);
				//printf("%d %d %d %d\n", j, i, 1000, 1);
			}
		}

		for (int i = 0; i < N; i++) {
			mcmf.AddEdge(N, i, poscount[i], 0);
			//printf("%d %d %d %d\n", N, i, poscount[i], 0);
			mcmf.AddEdge(i, N+1, lo, 0);
			//printf("%d %d %d %d\n", i, N+1, lo, 0);
		}

		pair<L, L> res = mcmf.GetMaxFlow(N, N+1);
		//fprintf(stderr, "%d\n", res.first);
		if (res.first == M)  {
			cout << lo << " " << res.second << endl;
			return;
		}
		abort();
		}
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		code();
	}
}
