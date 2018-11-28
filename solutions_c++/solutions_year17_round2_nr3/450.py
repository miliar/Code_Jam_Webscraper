#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

typedef long double ld;

void dfs(vector<vector<int64_t>> &D, int64_t E, int64_t S, ld t, vector<ld> &to, int64_t i) {
  if (t < to[i]) {
    to[i] = t;
  } else {
    return;
  }
  vector<int64_t> nxts;
  for (int64_t nxt = 0; nxt < D.size(); ++nxt) {
    if (D[i][nxt] != -1) {
      if (D[i][nxt] <= E) {
        nxts.push_back(nxt);
      }
    }
  }
  random_shuffle(nxts.begin(), nxts.end());
  for (auto nxt: nxts) {
    dfs(D, E - D[i][nxt], S, t + (ld)D[i][nxt]/(ld)S, to, nxt);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;

  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int64_t N, Q;
    cin >> N >> Q;
    vector<int64_t> E(N), S(N);
    for (int64_t i = 0; i < N; ++i) {
      cin >> E[i] >> S[i];
    }
    vector<vector<int64_t>> D(N, vector<int64_t>(N));
    for (int64_t i = 0; i < N; ++i) {
      for (int64_t j = 0; j < N; ++j) {
        cin >> D[i][j];
      }
    }
    vector<vector<ld>> nbsraw(N, vector<ld>(N, 1e20));
    for (int64_t i = 0; i < N; ++i) {
      dfs(D, E[i], S[i], 0, nbsraw[i], i);
    }
    vector<vector<pair<int64_t,ld>>> nbs(N);
    for (int64_t i = 0; i < N; ++i) {
      for (int64_t j = 0; j < N; ++j) {
        if (i == j) continue;
        if (nbsraw[i][j] != 1e20) {
          nbs[i].push_back({j,nbsraw[i][j]});
        }
      }
    }
    for (int64_t i = 0; i < Q; ++i) {
      int64_t U, V;
      cin >> U >> V;
      U--;
      V--;
      vector<ld> dp(N, 1e20);
      dp[V] = 0;
      bool changes = true;
      while (changes) {
        changes = false;
        for (int64_t j = 0; j < N; ++j) {
          for (auto nxt: nbs[j]) {
            if (dp[nxt.first] + nxt.second < dp[j]) {
              changes = true;
              dp[j] = dp[nxt.first] + nxt.second;
            }
          }
        }
      }
      cout << dp[U];
      if (i < Q - 1) cout << ' ';
    }
    cout << '\n';
  }

  return 0;
}
