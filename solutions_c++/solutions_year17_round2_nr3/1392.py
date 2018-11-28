#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 200

long long e[MAXN], s[MAXN];
long long d[MAXN][MAXN];
double f[MAXN][MAXN];
double cost[MAXN];
bool seen[MAXN];

int main(void) {
  int T;
  scanf("%i", &T);
  
  for (int t = 1; t <= T; t++) {
    int n, q;
    scanf("%i %i", &n, &q);
    
    for (int i = 1; i <= n; i++) {
      scanf("%lld %lld", &e[i], &s[i]);
    }
    
    const long long oo = (long long)1e15;
    
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        scanf("%lld", &d[i][j]);
        if (d[i][j] == -1) {
          d[i][j] = oo;
        }
      }
    }
    
    for (int k = 1; k <= n; k++) {
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
      }
    }
    
    // for (int i = 1; i <= n; i++) {
 //      for (int j = 1; j <= n; j++) {
 //        printf("[%i][%i]-> %lld\n", i, j, d[i][j]);
 //      }
 //    }
 //
    for (int i = 1; i <= n; i++) {
      fill(cost, cost+MAXN, double(oo));
      fill(seen, seen+MAXN, false);
      
      int u = i;
      
      cost[u] = 0.0;
      while (!seen[u]) {
        //printf("NOW %i [%.6f]\n", u, cost[u]);
        seen[u] = true;
        for (int v = 1; v <= n; v++) {
          if (e[u] >= d[u][v]) {
            cost[v] = min(cost[v], cost[u] + double(d[u][v])/s[u]);
          }
        }
        
        double best = oo;
        for (int v = 1; v <= n; v++) {
          if (best > cost[v] && !seen[v]) {
            best = cost[v];
            u = v;
          }
        }
      }
      
      for (int v = 1; v <= n; v++) {
        f[i][v] = cost[v];
        //printf("[%i]->[%i]: %.6f\n", i, v, f[i][v]);
      }      
    }
    
    // f[1] = 0.0;
//     for (int i = 1; i < n; i++) {
//       long long dist = 0;
//       for (int j = i+1; j <= n; j++) {
//         dist += d[j-1][j];
//         if (dist > e[i]) {
//           break;
//         }
//         f[j] = min(f[j], f[i] + double(dist)/s[i]);
//       }
//     }
     
    printf("Case #%i:", t);
    while (q--) {
      int u, v;
      scanf("%i %i", &u, &v);
      printf(" %.6f", f[u][v]);
    }
    puts("");
  }
  
  return 0;
}