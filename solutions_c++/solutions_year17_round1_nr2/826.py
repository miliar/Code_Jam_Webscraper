#include <iostream>
#include <vector>

#include <cmath>
#include <vector>
#include <iostream>
#include <queue>
#define MAX_N 55
#define pLL pair<long long, long long>
#define mp make_pair
#define INF 10000000

using namespace std;

typedef long long LL;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct PushRelabel {
  int N;
  vector<vector<Edge> > G;
  vector<LL> excess;
  vector<int> dist, active, count;
  queue<int> Q;

  PushRelabel(int N) : N(N), G(N), excess(N), dist(N), active(N), count(2*N) {}

  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  void Enqueue(int v) { 
    if (!active[v] && excess[v] > 0) { active[v] = true; Q.push(v); } 
  }

  void Push(Edge &e) {
    int amt = int(min(excess[e.from], LL(e.cap - e.flow)));
    if (dist[e.from] <= dist[e.to] || amt == 0) return;
    e.flow += amt;
    G[e.to][e.index].flow -= amt;
    excess[e.to] += amt;    
    excess[e.from] -= amt;
    Enqueue(e.to);
  }
  
  void Gap(int k) {
    for (int v = 0; v < N; v++) {
      if (dist[v] < k) continue;
      count[dist[v]]--;
      dist[v] = max(dist[v], N+1);
      count[dist[v]]++;
      Enqueue(v);
    }
  }

  void Relabel(int v) {
    count[dist[v]]--;
    dist[v] = 2*N;
    for (int i = 0; i < G[v].size(); i++) 
      if (G[v][i].cap - G[v][i].flow > 0)
    dist[v] = min(dist[v], dist[G[v][i].to] + 1);
    count[dist[v]]++;
    Enqueue(v);
  }

  void Discharge(int v) {
    for (int i = 0; excess[v] > 0 && i < G[v].size(); i++) Push(G[v][i]);
    if (excess[v] > 0) {
      if (count[dist[v]] == 1) 
    Gap(dist[v]); 
      else
    Relabel(v);
    }
  }

  LL GetMaxFlow(int s, int t) {
    count[0] = N-1;
    count[N] = 1;
    dist[s] = N;
    active[s] = active[t] = true;
    for (int i = 0; i < G[s].size(); i++) {
      excess[s] += G[s][i].cap;
      Push(G[s][i]);
    }
    
    while (!Q.empty()) {
      int v = Q.front();
      Q.pop();
      active[v] = false;
      Discharge(v);
    }
    
    LL totflow = 0;
    for (int i = 0; i < G[s].size(); i++) totflow += G[s][i].flow;
    return totflow;
  }
};

LL R[MAX_N];
pLL packs[MAX_N][MAX_N];
bool intersect(pLL one, pLL two) {
    return (one.first >= two.first && one.first <= two.second) || 
			(two.first >= one.first && two.first <= one.second);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for(int z = 1; z <= T; z++) {
        int N, P;
        cin >> N >> P;
        for(int i = 0; i < N; i++) {
            cin >> R[i];
        }
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < P; j++) {
                LL k;
                cin >> k;
                LL begin = (10*k) / (9 * R[i]);
                LL end = (10*k)/(11*R[i]);
                if((10*k) % (11 *R[i]) != 0) end++;
                if(10*(k - begin*R[i]) > begin * R[i]) {
                    end = -1;
                    begin = -1;
                }
                packs[i][j] = mp(end, begin);
                //cout << k << " " <<begin << " " << end << "\n"; 
            }
        }

        PushRelabel pr(2*N*P + 3);
        int s = 2*N*P + 1;
        int t = 2*N*P + 2;
        for(int i = 0; i < P; i++) {
            if(packs[0][i].first != -1) {
                pr.AddEdge(s, i, 1);
                pr.AddEdge(i, s, 1);
            }
        }
        for(int j = 0; j < N; j++) {
            for(int i = 0; i < P; i++) {
                pr.AddEdge(i + j*2*P, i + j * 2*P+P, 1);
                pr.AddEdge(i + j*2*P+P, i + j * 2*P, 1);
            }
        }
        for(int j = 0; j < N - 1; j++) {
            for(int i = 0; i < P; i++) {
                for(int k = 0; k < P; k++) {
                    if(intersect(packs[j][i], packs[j+1][k])) {
                        pr.AddEdge(i + j * 2*P + P, k + (j+1) * 2*P, 1);
                        pr.AddEdge(k + (j+1) * 2*P, i+ j * 2*P + P, 1);
                    }
                }
            }	
        }
        for(int i = 0; i < P; i++) {
            pr.AddEdge((N-1) * 2*P + P + i, t, 1);
            pr.AddEdge(t, (N-1) * 2*P + P + i, 1);
        }

        cout << "Case #" << z << ": " << pr.GetMaxFlow(s, t) << "\n";
    }


}
