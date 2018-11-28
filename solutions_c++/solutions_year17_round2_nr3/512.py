#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<double, int> di;

int N, Q;
int E[123], S[123];
int adj[123][123];
int U[123], V[123];

const double INF = 1e20;

double dp(int node, int arriving_horse) {
  return 0;
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  for (int case_num = 1; case_num <= T; case_num++) {
    cin >> N >> Q;
    for (int i = 1; i <= N; i++) cin >> E[i] >> S[i];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        cin >> adj[i][j];
      }
    }
    for (int i = 1; i <= Q; i++) {
      cin >> U[i] >> V[i];
    }

    // Floyd-Warshall
    ll dist[123][123];
    ll INFLL = 100000000;
    INFLL = INFLL*INFLL;

    for (int i = 0; i < 123; i++) {
      for (int j = 0; j < 123; j++) {
        dist[i][j] = adj[i][j];
        if (dist[i][j] == -1) {
          dist[i][j] = INFLL;
        }
      }
    }
    for (int i = 0; i < 123; i++) dist[i][i] = 0;
    for (int k = 1; k <= N; k++) {
      for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
          if (dist[i][j] > dist[i][k] + dist[k][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
          }
        }
      }
    }

    /*
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        cout << dist[i][j] << " ";
      } 
      cout << endl;
    }
    */

    /*
    double dp[123];
    for (int i = 0; i < 123; i++) dp[i] = INF;
    dp[1] = 0;

    for (int i = 1; i <= N; i++) {
      //cout << i << endl;
      double dist = 0;
      for (int j = i+1; j <= N; j++) {
        dist += adj[j-1][j];
        if (dist <= E[i]) {
          double time_needed = dist/(double)S[i];
          //cout << "  " << j << ": " << dist << " -- " << time_needed << endl;
          dp[j] = min(dp[j], dp[i] + time_needed);
        } else {
          break;
        }
      }
    }

    double ans = dp[N];
    printf("Case #%d: %0.6lf\n", case_num, ans);
    */
    
    double AdjList[123][123];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        if (dist[i][j] <= E[i]) {
          AdjList[i][j] = dist[i][j]/(double)S[i];
        }
        else {
          AdjList[i][j] = INF;
        }
      }
    }

    vector<double> ans;
    for (int qq = 1; qq <= Q; qq++) {
      vector<double> distance(N+1, INF);
      distance[U[qq]] = 0;
      priority_queue< di, vector<di>, greater<di> > pq;
      pq.push(di(0, U[qq]));

      while (!pq.empty()) {
        di front = pq.top(); pq.pop();
        double d = front.first;
        int u = front.second;
        if (u == V[qq]) break;
        if (d > distance[u]) continue;
        for (int j = 1; j <= N; j++) {
          if (AdjList[u][j] == INF) continue;
          if (distance[u] + AdjList[u][j] < distance[j]) {
            distance[j] = distance[u] + AdjList[u][j];
            pq.push(di(distance[j], j));
          }
        }
      }

      //cout << distance[V[qq]] << endl;
      ans.push_back(distance[V[qq]]);
    }

    printf("Case #%d:", case_num);
    for (int i = 0; i < ans.size(); i++) {
      printf(" %0.6lf", ans[i]);
    }
    printf("\n");

  }
  return 0;
}
