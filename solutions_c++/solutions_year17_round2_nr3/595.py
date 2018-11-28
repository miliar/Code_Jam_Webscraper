#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

using namespace std;

double el[110], sl[110];
double gra[110][110];

double wgra[110][110];
double fgra[110][110];

double cl[110];

bool cmp(const pair<int, double> &a, const pair<int, double> &b) {
  if (a.second > b.second) {
    return true;
  }
  return false;
}

int main() {
  int t, n, q;

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &el[i], &sl[i]);
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        scanf("%lf", &gra[i][j]);
        if (gra[i][j] == -1) {
          gra[i][j] = 1e13;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        wgra[i][j] = gra[i][j];
        fgra[i][j] = 1e13;
      }
    }
    for (int k = 0; k < n; k++) {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          wgra[i][j] = min(wgra[i][j], wgra[i][k] + wgra[k][j]);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (wgra[i][j] <= el[i]) {
          fgra[i][j] = wgra[i][j] / sl[i];
        }
      }
    }

    vector<double> ans;
    for (int l = 0; l < q; l++) {
      int start, end;
      scanf("%d %d", &start, &end);
      start -= 1;
      end -= 1;

      vector<pair<int, double>> qu;
      int done[110];

      for (int i = 0; i < n; i++) {
        cl[i] = 1e13;
        done[i] = 0;
      }

      cl[start] = 0;
      qu.emplace_back(start, cl[start]);
      make_heap(qu.begin(), qu.end(), cmp);

      while(!qu.empty()) {
        auto currp = qu.front();
        int curr = currp.first;
        pop_heap(qu.begin(), qu.end(), cmp);
        qu.pop_back();

        if (done[curr]) {
          continue;
        }
        done[curr] = 1;
        if (curr == end) {
          break;
        }

        for (int i = 0; i < n; i++) {
          double cost = fgra[curr][i] + cl[curr];
          if (cost < cl[i]) {
            cl[i] = cost;
            qu.emplace_back(i, cost);
            push_heap(qu.begin(), qu.end(), cmp);
          }
        }
      }
      ans.push_back(cl[end]);
    }
    printf("Case #%d:", o + 1);
    for (int i = 0; i < ans.size(); i++) {
      printf(" %.6f", ans[i]);
    }
    printf("\n");
  }

  return 0;
}
