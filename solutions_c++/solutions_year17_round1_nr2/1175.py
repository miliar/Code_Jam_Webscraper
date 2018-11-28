#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

int meal[5];
int packages[5][10];

int upround(double a) {
  if (a - int(a) == 0)
    return a;
  else
    return a + 1;
}

int downround(double a) {
  return int(a);
}
double max(double a, double b) {
  if (a > b)
    return a;
  return b;
}
double min(double a, double b) {
  if (a < b)
    return a;
  return b;
}
int chosen[10];
bool visited[10];
int n, p;
int max_ans = 0;

void verify_ans() {
  // for (int i = 1; i <= p ; i++)
    // printf("%d : %d\n",i, chosen[i] );
  int cnt_ans = 0;
  for (int i = 1; i <= p; i ++) {
    int a = i;
    int b = chosen[i];
    int max_server = packages[1][a] / (0.9 * meal[1]);
    int min_server = packages[1][a] / (1.1 * meal[1]);
    max_server = min(max_server, packages[2][b] / (0.9 * meal[2]));
    min_server = max(min_server, packages[2][b] / (1.1 * meal[2]));
    for (int k = int(min_server); k <= int(max_server) + 1; k++ ) {
      if (packages[1][a] >= k * meal[1] * 0.9 && packages[1][a] <= k * meal[1] * 1.1 &&
          packages[2][b] >= k * meal[2] * 0.9 && packages[2][b] <= k * meal[2] * 1.1)
      {
        cnt_ans++;
        break;
      }
    }
  }
  if (cnt_ans > max_ans) max_ans = cnt_ans;
}

void gen_pair(int cur_p) {
  if (cur_p > p) {
    verify_ans();
    return;
  }
  for (int i = 1; i <= p; i++)
    if (visited[i] == false) {
      chosen[cur_p] = i;
      visited[i] = true;
      gen_pair(cur_p + 1);
      visited[i] = false;
      chosen[cur_p] = 0;
    }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin >> T;
  for (int _ = 1; _ <= T; _++) {
    cin >> n>> p;
    for (int i = 1; i <= n; i++)
      scanf("%d", &meal[i]);
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= p; j++)
        scanf("%d", &packages[i][j]);
    max_ans = 0;

    if (n == 1) {
      int max_server = 2147483647;
      int min_server = 0;
      int cur_ans = 0;
      for (int i = 1; i <= p; i++) {
        max_server = packages[1][i] / (0.9 * meal[1]);
        min_server = packages[1][i] / (1.1 * meal[1]);
        for (int k = int(min_server); k <= int(max_server) + 1; k++ ) {
          if (packages[1][i] >= k * meal[1] * 0.9 && packages[1][i] <= k * meal[1] * 1.1)
          {
            cur_ans++;
            break;
          }
        }
      }
      if (cur_ans > max_ans) max_ans = cur_ans;
    } else {
      memset(visited, 0, sizeof visited);
      memset(chosen, 0, sizeof chosen);
      gen_pair(1);
    }
    printf("Case #%d: %d\n", _, max_ans);
  }
}
