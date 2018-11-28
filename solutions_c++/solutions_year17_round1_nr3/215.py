#include <bits/stdc++.h>

using namespace std;

const int inf = 1e9;

int main(int argc, const char *argv[]) {
  cin.sync_with_stdio(false);
  int n, k, d;
  cin >> n >> k >> d;
  vector<int> a(n + 1), dis(n + 1, inf);
  vector<vector<pair<int, int>>> g(n + 1);
  for (int i = 0; i < k; i++) {
    int t;
    cin >> t;
    a[t] = true;
  }
  for (int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back({v, i + 1});
    g[v].push_back({u, i + 1});
  }
  queue<int> q;
  for (int i = 1; i <= n; i++) {
    if (a[i]) {
      dis[i] = 0;
      q.push(i);
    }
  }
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (auto x : g[u]) {
      int v = x.first;
      if (dis[v] == inf) {
        dis[v] = dis[u] + 1;
        q.push(v);
      }
    }
  }
  set<int> se;
  for (int i = 1; i <= n; i++) {
    bool flag = false;
    for (auto x : g[i]) {
      int v = x.first, id = x.second;
      if (dis[v] <= dis[i]) {
        if (flag || dis[v] == dis[i]) {
          se.insert(id);
        } else {
          flag = true;
        }
      }
    }
  }
  cout << se.size() << endl;
  for (auto x : se) {
    cout << x << " ";
  }
  return 0;
}
