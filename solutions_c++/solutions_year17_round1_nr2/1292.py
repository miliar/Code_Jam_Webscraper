#include <algorithm>
#include <vector>
#include <climits>
#include <iostream>
using namespace std;

const long long maxnodes = 50000;

long long nodes = maxnodes, src, dest;
long long dist[maxnodes], q[maxnodes], work[maxnodes];

struct Edge {
  long long to, rev;
  long long f, cap;
};

vector<Edge> g[maxnodes];

// Adds bidirectional edge
void addEdge(long long s, long long t, long long cap){
  Edge a = {t, g[t].size(), 0, cap};
  Edge b = {s, g[s].size(), 0, cap};
  g[s].push_back(a);
  g[t].push_back(b);
}

bool dinic_bfs() {
  fill(dist, dist + nodes, -1);
  dist[src] = 0;
  long long qt = 0;
  q[qt++] = src;
  for (long long qh = 0; qh < qt; qh++) {
    long long u = q[qh];
    for (long long j = 0; j < (long long) g[u].size(); j++) {
      Edge &e = g[u][j];
      long long v = e.to;
      if (dist[v] < 0 && e.f < e.cap) {
        dist[v] = dist[u] + 1;
        q[qt++] = v;
      }
    }
  }
  return dist[dest] >= 0;
}

long long dinic_dfs(long long u, long long f) {
  if (u == dest)
    return f;
  for (long long &i = work[u]; i < (long long) g[u].size(); i++) {
    Edge &e = g[u][i];
    if (e.cap <= e.f) continue;
    long long v = e.to;
    if (dist[v] == dist[u] + 1) {
      long long df = dinic_dfs(v, min(f, e.cap - e.f));
      if (df > 0) {
        e.f += df;
        g[v][e.rev].f -= df;
        return df;
      }
    }
  }
  return 0;
}

long long maxFlow(long long _src, long long _dest) {
  src = _src;
  dest = _dest;
  long long result = 0;
  while (dinic_bfs()) {
    fill(work, work + nodes, 0);
    while (long long delta = dinic_dfs(src, INT_MAX))
      result += delta;
  }
  return result;
}

long long findPupper(long long x, long long y) {
    long long mn = 1;
    long long mx = 1000000;
    while(mn < mx) {
        long long med = (mn+mx)/2;
        if (90ll*y*med > 100ll*x) mx = med;
        else if (110ll*y*med < 100ll*x) mn = med+1;
        else mn = med+1;
    }
    mn--;
    if (90*y*mn <= 100*x && 100*x <= 110*y*mn) return mn;
    else return 0;
}

long long findPlower(long long x, long long y) {
    long long mn = 1;
    long long mx = 1000000;
    while(mn < mx) {
        long long med = (mn+mx)/2;
        if (90*y*med > 100*x) mx = med;
        else if (110*y*med < 100*x) mn = med+1;
        else mx = med;
    }
    if (90*y*mn <= 100*x && 100*x <= 110*y*mn) return mn;
    else return 0;
}

bool inter(long long x1, long long y1, long long x2, long long y2) {
    if (x2 >= x1 && x2 <= y1) return true;
    if (y2 >= x1 && y2 <= y1) return true;
    return false;
}

int main() {
    long long t;
    scanf("%lld", &t);
    long long te = 1;
    while(t--) {
        vector<long long> ingri;
        long long n, p;
        scanf("%lld %lld", &n, &p);
        for(long long i=0;i<n*p+50;i++) {
            g[i].clear();
        }
        for(long long i=0;i<n;i++) {
            long long a;
            scanf("%lld", &a);
            ingri.push_back(a);
        }
        vector<vector<pair<long long, long long> > > resp;
        vector<vector<vector<pair<long long, long long> > > > valid;
        for(long long i=0;i<n;i++) {
            vector<pair<long long, long long> >temp;
            vector<vector<pair<long long, long long> > > temp2;
            valid.push_back(temp2);
            for(long long j=0;j<p;j++) {
                long long a;
                scanf("%lld", &a);
                temp.push_back(make_pair(findPlower(a, ingri[i]), findPupper(a, ingri[i])));
                //printf("%lld %lld\n", temp[j].first, temp[j].second);
            }
            resp.push_back(temp);
            if (i == 0) {
                for(long long j=0;j<p;j++) {
                    vector<pair<long long, long long> > tete;
                    tete.push_back(temp[j]);
                    valid[i].push_back(tete);
                }
            }
            if (i != 0) {
                for(long long j=0;j<p;j++) {
                    for(long long l=0;l<valid[i-1][j].size();l++) {
                        for(long long k=0;k<p;k++) {
                            vector<pair<long long, long long> > tete;
                            valid[i].push_back(tete);
                            if (resp[i-1][j].first != 0 && inter(valid[i-1][j][l].first, valid[i-1][j][l].second, resp[i][k].first, resp[i][k].second)) {
//                                printf("oi1\n");
                                valid[i][k].push_back(make_pair(max(valid[i-1][j][l].first, resp[i][k].first), min(valid[i-1][j][l].second, resp[i][k].second)));
                                addEdge(p*(i-1)+j+1, p*i+k+1, 1);            
//                                printf("oi2\n");
                            }
                        }
                    }
                }
            }
        }
        for(long long j=0;j<p;j++) {
            if (resp[0][j].first != 0) addEdge(0, j+1, 1);
            if (resp[n-1][j].first != 0) addEdge(n*p+1, (n-1)*p+j+1, 1);
        }
        printf("Case #%lld: %lld\n", te++, maxFlow(0, n*p+1));
    }
}
