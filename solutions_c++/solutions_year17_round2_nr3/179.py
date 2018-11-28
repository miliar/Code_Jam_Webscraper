#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

using ll = long long;

template <class T> struct Dijkstra {
    int n;
    bool directed;
    vector <int> parent;
    vector<T> dist;
    vector <vector <pair <T, int>>> adj;

    Dijkstra (int n, bool directed = false): n(n), adj(n), directed(directed) {}

    void addEdge (int a, int b, T d) {
        adj[a].push_back(make_pair(d, b));
        if (!directed) {
            adj[b].push_back(make_pair(d, a));
        }
    }

    void BuildTree (int s) {
        dist = vector <T>(n, numeric_limits<double>::max());
        parent = vector <int>(n, -1);
        // priority_queue <pair <T, vector<pair <T, int>>>, vector<pair <T, int>>, greater<pair <T, int>>> q;
        priority_queue <T, vector<pair <T, int>>, greater<pair <T, int>>> q;

        dist[s] = 0;
        q.push(make_pair(dist[s], s));
        do {
            auto u = q.top();
            q.pop();
            for (auto& e: adj[u.y]) {
                if (u.x < dist[e.y] - e.x) {
                    dist[e.y] = u.x + e.x;
                    parent[e.y] = u.y;
                    q.push(make_pair(dist[e.y], e.y));
                }
            }
        } while (!q.empty());
    }
};


int main() {
  ios::sync_with_stdio(false);

  // cout << numeric_limits<double>::max() << endl;

  int t;
  cin >> t;

  for (int cs = 0; cs < t; cs++) {
    int n, q;
    cin >> n >> q;

    vector <double> E(n), S(n);
    for (int i = 0; i < n; i++)
      cin >> E[i] >> S[i];

    vector <vector <double>> dist(n, vector <double>(n));
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        cin >> dist[i][j];

    for (int k = 0; k < n; k++)
      for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
          if(dist[i][k] >= 0 && dist[k][j] >= 0)
            if (dist[i][j] < 0 || dist[i][k] + dist[k][j] < dist[i][j])
              dist[i][j] = dist[i][k] + dist[k][j];

    Dijkstra<double> D(n * n, true);

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) if (i != j) {
        // (i, i) -> (i, j)
        if (dist[i][j] >= 0 && dist[i][j] <= E[i])
          D.addEdge(i * n + i, i * n + j, dist[i][j] / S[i]);

        // (i, j) -> (j, j)
        D.addEdge(i * n + j, j * n + j, 0);
      }

    cout << "Case #" << cs + 1 << ":";
    for (int i = 0; i < q; i++) {
      int a, b; cin >> a >> b;
      D.BuildTree((a - 1) * (n + 1));
      cout << ' ' << fixed << setprecision(9) << D.dist[(b - 1) * (n + 1)];
    }
    cout << endl;
  }

  return 0;
}
