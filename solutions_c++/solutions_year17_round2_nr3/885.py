
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

void solve(int t, int N, int Q, const vector<pair<int,int>>& horses, 
           const vector<vector<int>>&dists) {
  vector<double> times(N, 1e99);
  vector<double> line_dist(N, 0);
  for(int i = 1; i < N; ++i) {
    line_dist[i] = line_dist[i-1] + dists[i-1][i];

    // cout << "dist: " << line_dist[i] << ' '     << dists[i-1][i] <<  endl;
  }

  times[0] = 0;
  for(int i = 0; i < N; ++i) {
    for(int j = 1; j < N; ++j) {
      double d = line_dist[j] - line_dist[i];
      if (d <= horses[i].first) {
        double t = times[i] + (double) d / horses[i].second;
        if (t < times[j]) { times[j] = t; }
      }
    }
  }
  printf("Case #%d: %f\n", t, times.back());
}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    int N, Q;
    cin >> N >> Q;
    vector<pair<int, int>> horses(N);
    for(int i = 0; i < N; ++i) {
      cin >> horses[i].first >> horses[i].second;
    }
    vector<vector<int>> dists(N, vector<int>(N, -1));
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        cin >> dists[i][j];
      }
    }
    int start, end;
    cin >> start >> end;
    solve(t, N, Q, horses, dists);
  }
}
