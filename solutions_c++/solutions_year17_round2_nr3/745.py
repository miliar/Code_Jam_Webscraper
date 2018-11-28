#include <bits/stdc++.h>
using namespace std;

int main() {
  long long t; scanf("%lld", &t);
  for(long long _i=1; _i<=t; _i++) {
    printf("Case #%lld:", _i);
    long long n, q; scanf("%lld %lld", &n, &q);
    vector<pair<long long, long long>> horses;
    for(long long i=0; i<n; i++) {
      long long e, s; scanf("%lld %lld", &e, &s);
      horses.push_back({e, s});
    }
    vector<vector<long long>> adj(n, vector<long long>(n, -1));
    for(long long i=0; i<n; i++) {
      for(long long j=0; j<n; j++) {
        scanf("%lld", &adj[i][j]);
      }
    }
    for(long long i=0; i<n; i++) {
      priority_queue<pair<long long, long long>> q;
      q.push({0, i});
      vector<long long> dist(n, -1);
      dist[i] = 0;
      while(!q.empty()) {
        long long d = -q.top().first;
        long long x = q.top().second;
        q.pop();
        if(d != dist[x]) continue;
        for(long long j=0; j<n; j++) {
          if(adj[x][j] != -1) {
            long long cand_dist = d + adj[x][j];
            if(dist[j] < 0 or cand_dist < dist[j]) {
              q.push({-cand_dist, j});
              dist[j] = cand_dist;
            }
          }
        }
      }
      for(long long j=0; j<n; j++) {
        if(j != i) adj[i][j] = dist[j];
      }
    }
    for(long long i=0; i<q; i++) {
      long long u, v; scanf("%lld %lld", &u, &v); u--; v--;
      priority_queue<pair<double, long long>> q;
      vector<double> dist(n, -1);
      dist[u] = 0;
      q.push({0, u});
      while(!q.empty()) {
        double d = -q.top().first;
        long long x = q.top().second;
        q.pop();
        if(dist[x] != d) continue;
        if(x == v) break;
        for(long long j=0; j<n; j++) {
          // if horse x can get to town j, then push town j with the time it takes
          if(adj[x][j] != -1 and adj[x][j] <= horses[x].first) {
            double cand_dist = d + (double)adj[x][j]/(double)horses[x].second;
            if(dist[j] < 0 or cand_dist < dist[j]) {
              q.push({-cand_dist, j});
              dist[j] = cand_dist;
            }
          }
        }
      }
      printf(" %lf", dist[v]);
    }
    printf("\n");
  }
}
