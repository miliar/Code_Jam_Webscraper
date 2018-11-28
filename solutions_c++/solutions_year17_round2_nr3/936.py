#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

const int N = 100 + 10;

int e[N], s[N], n, q;
long long dist[N][N];
bool visited[N];
double reach[N][N], temp[N];

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    memset(dist, 0, sizeof(dist));

    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; ++ i) {
      scanf("%d%d", e + i, s + i);
    }
    for (int i = 1; i <= n; ++ i) {
      for (int j = 1; j <= n; ++ j) {
        scanf("%lld", &dist[i][j]);
      }
    }

  //   if (t == 29) {
  //     printf("%d %d\n", n, q);
  // for (int i = 1; i <= n; ++ i) {
  //     for (int j = 1; j <= n; ++ j) {
  //       printf("%lld ", dist[i][j]);
  //     } puts("");
  //   }      
  //   }

    for (int k = 1; k <= n; ++ k) {
      for (int i = 1; i <= n; ++ i) {
        if (i != k && dist[i][k] != -1) {
          for (int j = 1; j <= n; ++ j) {
            if (j != k && dist[k][j] != -1 && i != j) {
              long long d = dist[i][k] + dist[k][j];
              if (dist[i][j] == -1 || d < dist[i][j]) {
                dist[i][j] = d;
              }
            }
          }
        }
      }
    }

    std::vector<double> answers;
    while (q --) {
      int start, end;
      scanf("%d%d", &start, &end);

      for (int i = 1; i <= n; ++ i) {
        visited[i] = false;
        temp[i] = 1e30;
      }
      std::queue<int> queue;
      queue.push(start);
      visited[start] = true;
      temp[start] = 0;
      while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        visited[u] = false;
        for (int i = 1; i <= n; ++ i) {
          if (u == i || dist[u][i] > e[u] || dist[u][i] == -1) continue;
          double t = (double)dist[u][i] / s[u];
          if (temp[u] + t < temp[i]) {
            temp[i] = temp[u] + t;
            if (!visited[i]) {
              queue.push(i);
              visited[i] = true;
            }
          }
        }
      }
      answers.push_back(temp[end]);
    }
    printf("Case #%d:", t);
    for (int i = 0; i < answers.size(); ++ i) {
      printf(" %.7f", answers[i]);
    } puts("");
  }
  return 0;
}