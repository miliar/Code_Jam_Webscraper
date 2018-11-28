// Used code from http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>
#include <climits>
#include <queue>

using namespace std;

int V, N, P;

/* Returns true if there is a path from source 's' to sink 't' in
   residual graph. Also fills parent[] to store the path */
bool bfs(vector<vector<int>> &rGraph, int s, int t, int parent[])
{
  // Create a visited array and mark all vertices as not visited
  vector<bool> visited(V, false);
 
  // Create a queue, enqueue source vertex and mark source vertex
  // as visited
  queue <int> q;
  q.push(s);
  visited[s] = true;
  parent[s] = -1;
 
  // Standard BFS Loop
  while (!q.empty())
    {
      int u = q.front();
      q.pop();
 
      for (int v=0; v<V; v++)
        {
          if (visited[v]==false && rGraph[u][v] > 0)
            {
              q.push(v);
              parent[v] = u;
              visited[v] = true;
            }
        }
    }
 
  // If we reached sink in BFS starting from source, then return
  // true, else false
  return (visited[t] == true);
}
 
// Returns the maximum flow from s to t in the given graph
vector<vector<int>> fordFulkerson(vector<vector<int>> &graph, int s, int t)
{
  int u, v;
 
  // Create a residual graph and fill the residual graph with
  // given capacities in the original graph as residual capacities
  // in residual graph
  vector<vector<int>> rGraph = graph;
 
  int parent[V];  // This array is filled by BFS and to store path
 
  int max_flow = 0;  // There is no flow initially
 
  // Augment the flow while tere is path from source to sink
  while (bfs(rGraph, s, t, parent))
    {
      // Find minimum residual capacity of the edges along the
      // path filled by BFS. Or we can say find the maximum flow
      // through the path found.
      int path_flow = INT_MAX;
      for (v=t; v!=s; v=parent[v])
        {
          u = parent[v];
          path_flow = min(path_flow, rGraph[u][v]);
        }
 
      // update residual capacities of the edges and reverse edges
      // along the path
      for (v=t; v != s; v=parent[v])
        {
          u = parent[v];
          rGraph[u][v] -= path_flow;
          rGraph[v][u] += path_flow;
        }
 
      // Add path flow to overall flow
      max_flow += path_flow;
    }
 
  for (int r = 0; r < V; ++r)
    for (int c = 0; c < V; ++c)
      rGraph[r][c] = graph[r][c] - rGraph[r][c];
  return rGraph;
}

int enc(int ni, int pi) {
  return ni * P + pi;
}

pair<int, int> dec(int v) { // (ing, pac)
  return make_pair<int, int>(v / P, v % P);
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    cin >> N >> P; // N: # ingredients, P: # packets per ingredient
    vector<int> serv(N, 0); // serv[i] = # grams of ingredient i
    for (int &i : serv) cin >> i;
    vector<vector<int>> t(N, vector<int>(P, 0));
    for (auto &row : t) for (auto &cell : row) cin >> cell;

    //cout << "N=" << N << ",P=" << P << endl;

    V = 2 + N * P;
    vector<vector<int>> g(V, vector<int>(V, 0));

    int S = V - 2, T = V - 1;

    vector<vector<int>> lbs(N, vector<int>(P, -1));
    vector<vector<int>> ubs(N, vector<int>(P, -1));

    for (int ni = 0; ni < N; ++ni) {
      for (int pi = 0; pi < P; ++pi) {
        int ub = 10 * t[ni][pi] / 9 / serv[ni];
        if (ub * 9 * serv[ni] > 10 * t[ni][pi]) --ub;
        int lb = 10 * t[ni][pi] / 11 / serv[ni];
        if (lb * 11 * serv[ni] < 10 * t[ni][pi]) ++lb; // unnec?
        if (lb > ub || ub <= 0) lb = ub = -1;
        lbs[ni][pi] = lb;
        ubs[ni][pi] = ub;
      }
    }

    /*
    cout << '\n';
    for (int ni = 0; ni < N; ++ni) {
      for (int pi = 0; pi < P; ++pi) {
        cout << lbs[ni][pi] << ' ';
      }
      cout << '\n';
    }
    cout << '\n';

    cout << '\n';
    for (int ni = 0; ni < N; ++ni) {
      for (int pi = 0; pi < P; ++pi) {
        cout << ubs[ni][pi] << ' ';
      }
      cout << '\n';
    }
    cout << '\n'; */

    pair<int, int> no(-1, -1);

    auto inter = [&](pair<int, int> a, pair<int, int> b) {
      auto m = make_pair(max(a.first, b.first), min(a.second, b.second));
      if (m.first > m.second) return no;
      return m;
    };

    for (int pi = 0; pi < P; ++pi) {
      if (lbs[0][pi] < 0) continue;
      map<int, pair<int, int>> cur;
      cur[pi] = make_pair(lbs[0][pi], ubs[0][pi]);
      for (int ni = 1; ni < N; ++ni) {
        map<int, pair<int, int>> next;
        for (auto &left : cur) {
          for (int pi2 = 0; pi2 < P; ++pi2) {
            auto i = inter(left.second, make_pair(lbs[ni][pi2], ubs[ni][pi2]));
            if (i == no) continue;
            g[enc(ni-1, left.first)][enc(ni, pi2)] = 1;
            next[pi2] = i;
          }
        }
      }
    }

    for (int pi = 0; pi < P; ++pi) {
      if (lbs[0][pi] != -1)
        g[S][enc(0, pi)] = 1;
      g[enc(N-1, pi)][T] = 1;
    }

    auto res = fordFulkerson(g, S, T);

    int n_res = 0;
    for (int pi = 0; pi < P; ++pi) {
      //cout << res[S][enc(0, pi)] << ' ';
      if (res[S][enc(0, pi)] > 0) ++n_res;
    }
    //cout << endl;

    cout << "Case #" << cas << ": " << n_res << endl;
  }
  return 0;
}
