#include <stdio.h>
#include <queue>

struct Node {
  int index;
  long long distance;

  bool operator <(const Node &other) const {
    return this->distance > other.distance;
  }
};

int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int n, q;
    scanf("%d%d", &n, &q);
    int energy[1 + n];
    int speed[1 + n];
    int distance[1 + n][1 + n];
    double time[1 + n][1 + n];
    for(int i = 1; i <= n; i++)
      scanf("%d%d", &energy[i], &speed[i]);
    for(int i = 1; i <= n; i++)
      for(int j = 1; j <= n; j++) {
        scanf("%d", &distance[i][j]);
        time[i][j] = 1e20;
      }
    for(int i = 1; i <= n; i++) {
      long long minDist[1 + n];
      for(int j = 1; j <= n; j++)
        minDist[j] = 0x3fffffffffffffff;
      std::priority_queue<Node> dijkstra;
      dijkstra.push(Node{i, 0});
      minDist[i] = 0;
      while(!dijkstra.empty()) {
        int u = dijkstra.top().index;
        if (minDist[u] == dijkstra.top().distance) {
          for (int v = 1; v <= n; v++) {
            if (distance[u][v] != -1
                && minDist[v] > minDist[u] + distance[u][v]) {
              minDist[v] = minDist[u] + distance[u][v];
              dijkstra.push(Node{v, minDist[v]});
            }
          }
        }
        dijkstra.pop();
      }
      for(int j = 1; j <= n; j++)
        if (minDist[j] <= energy[i])
          time[i][j] = std::min(time[i][j], (double)minDist[j] / speed[i]);
    }
    /*
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n; j++) {
        printf("%.8lf ", time[i][j]);
      }
      printf("\n");
    }
    printf("\n");//*/
    for(int k = 1; k <= n; k++)
      for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
          if (time[i][j] > time[i][k] + time[k][j])
            time[i][j] = time[i][k] + time[k][j];
    /*
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n; j++) {
        printf("%.8lf ", time[i][j]);
      }
      printf("\n");
    }//*/
    printf("Case #%d: ", t);
    for(int i = 1; i <= q; i++) {
      int u, v;
      scanf("%d%d", &u, &v);
      printf("%.8lf ", time[u][v]);
    }
    printf("\n");
  }
  return 0;
}
