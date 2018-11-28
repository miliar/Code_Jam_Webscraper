#include <bits/stdc++.h>
using namespace std;

int T;
int N, Q;
vector<long long> E, S;
vector<vector<long long>> v;
vector<vector<double>> d;
vector<pair<int, int>> q;

void solve() {
  E.clear();
  S.clear();
  v.clear();
  q.clear();
  d.clear();

  cin >> N >> Q;
  E.resize(N);
  S.resize(N);
  for (int i = 0; i < N; ++i) {
    cin >> E[i] >> S[i];
  }
  v.resize(N, vector<long long>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> v[i][j];
    }
  }
  q.resize(Q);
  for (int i = 0; i < Q; ++i) {
    cin >> q[i].first >> q[i].second;
    --q[i].first, --q[i].second;
  }

  for (int k = 0; k < N; ++k) {
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (v[i][k] < 0 || v[k][j] < 0) {
          continue;
        }
        if (v[i][j] < 0) {
          v[i][j] = v[i][k] + v[k][j];
        } else {
          v[i][j] = min(v[i][j], v[i][k] + v[k][j]);
        }
      }
    }
  }

  d.resize(N, vector<double>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (v[i][j] == -1 || v[i][j] > E[i]) {
        d[i][j] = -1;
      } else {
        d[i][j] = v[i][j] * 1.0 / S[i];
      }
    }
  }

  for (int k = 0; k < N; ++k) {
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (d[i][k] < 0 || d[k][j] < 0) {
          continue;
        }
        if (d[i][j] < 0) {
          d[i][j] = d[i][k] + d[k][j];
        } else {
          d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
      }
    }
  }

  for (int i = 0; i < Q; ++i) {
    printf("%.10lf ", d[q[i].first][q[i].second]);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    solve();
    printf("\n");
  }
}
