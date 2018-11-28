#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

int R[55];
int Q[55][55];
pii interval[55][55];
set<pii> heap[55];
int ordx[5555];
bool used[55][55];
vector<int> link[5555];

int main(void) {

  int cases; scanf("%d", &cases);
  
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);

    int N, P; scanf("%d %d", &N, &P);
    for (int i = 0; i < N; ++i) {
      scanf("%d", &R[i]);
      heap[i].clear();
    }
    memset(used, false, sizeof used);
    int total = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < P; ++j) {
        scanf("%d", &Q[i][j]);
        int upper_bound = Q[i][j] * 10 / (9 * R[i]);
        int lower_bound = Q[i][j] * 10 / (11 * R[i]);
        if (Q[i][j] * 10 % (11 * R[i]) != 0) {
          ++lower_bound;
        }
        lower_bound = max(lower_bound, 1);
        // printf("interval %d %d\n", lower_bound, upper_bound);
        interval[i][j] = pii(lower_bound, upper_bound);
        ordx[total++] = lower_bound;
        ordx[total++] = upper_bound;
      }
    }

    sort(ordx, ordx + total);
    total = unique(ordx, ordx + total) - ordx;
    
    int ans = 0;
    for (int i = 0; i < total; ) {
      vector<int> to_used;
      for (int x = 0; x < N; ++x) {
        int best = -1;
        for (int y = 0; y < P; ++y) if (!used[x][y]) {
          if (interval[x][y].first <= ordx[i] && ordx[i] <= interval[x][y].second) {
            // printf("x = %d, y = %d, ordx[i] = %d\n", x, y, ordx[i]);
            if (best == -1 || interval[x][y].second < interval[x][best].second) {
              best = y;
            }
          }
        }
        if (best == -1) {
          break;
        }
        to_used.push_back(best);
      }
      if (to_used.size() != N) {
        ++i;
        continue;
      }
      ++ans;
      for (int x = 0; x < N; ++x) {
        used[x][to_used[x]] = true;
      }
    }
    printf("%d\n", ans);
  }

  return 0;
}