
#include <iostream>
#include <iomanip>
#include <vector>
#include <limits>

using namespace std;

void dfs(int u, double t, double *ti, long long **map, int *s, int n){
  if(t < ti[u]){
    ti[u] = t;
    for(int i = 1; i <= n; i++){
      if(map[u][i] != -1){
        dfs(i, t + ((double)map[u][i]) / (double)s[u], ti, map, s, n);
      }
    }
  }
}

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;

  for(int c = 1; c <= t; c++){
    int n, q;
    cin >> n >> q;

    int *e = new int[n + 1];
    int *s = new int[n + 1];
    for(int i = 1; i <= n; i++){
      cin >> e[i] >> s[i];
    }

    long long **map = new long long*[n + 1];
    for(int i = 0; i <= n; i++)
      map[i] = new long long[n + 1];

    for(int i = 1; i <= n; i++){
      for(int j = 1; j <= n; j++){
        cin >> map[i][j];
      }
    }

    for(int k = 1; k <= n; k++){
      for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
          if((map[i][j] == -1 || map[i][j] > map[i][k] + map[k][j]) && map[i][k] != -1 && map[k][j] != -1){
            map[i][j] = map[i][k] + map[k][j];
          }
        }
      }
    }

    for(int i = 1; i <= n; i++){
      for(int j = 1; j <= n; j++){
        if(map[i][j] > e[i])
          map[i][j] = -1;
      }
    }

    int u, v;
    cout << fixed << setprecision(7) << "Case #" << c << ":";
    for(int i = 0; i < q; i++){
      cin >> u >> v;

      double *ti = new double[n + 1];
      for(int i = 0; i <= n; i++)
        ti[i] = numeric_limits<double>::max();

      dfs(u, 0, ti, map, s, n);

      cout << " " << ti[v];
    }
    cout << endl;

  }

  return 0;
}
