#include <bits/stdc++.h>

using namespace std;

int a[1005][1005], b[1005][1005], vis[1005], sum[1005];

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    memset(vis, 0, sizeof(vis)); 
    memset(sum, 0, sizeof(sum));
    int n, c, m;
    cin >> n >> c >> m;
    vector<pair<int, int>> vec(m);
    for (int i = 0; i < m; i++) {
      cin >> vec[i].first >> vec[i].second;
    }
    sort(vec.begin(), vec.end());
    int s1 = 0, s2 = 0;
    for (int i = 1; i <= m; i++) {
      int p = vec[i - 1].first, c = vec[i - 1].second;
      bool flag = false;
      for (int j = 0; j < s1; j++) {
        if (!b[c][j] && !a[j][p]) {
          sum[j]++;
          a[j][p] = i;
          b[c][j] = i;
          vis[i] = false;
          flag = true;
          break;
        }
      }
      if (flag) continue;
      for (int j = 0; j < s1; j++) {
        if (!b[c][j] && sum[j] < p) {
          vis[i] = true;
          b[c][j] = i;
          flag = true;
          sum[j]++;
          s2++;
          break;
        }
      }
      if (flag) continue;
      int minn = 2000, zz = -1;
      for (int j = 0; j < s1; j++) {
        if (b[c][j] && !a[j][p] && vis[b[c][j]]) {
          if (b[c][j] < minn) {
            minn = b[c][j];
            zz = j;
          }
        }
      }
      if (minn < 2000) {
        b[c][s1] = b[c][zz];
        b[c][zz] = i;
        a[s1][vec[minn].first] = 1;
        a[zz][p] = 1;
        s1++;
        s2--;
        continue;
      }
      for (int j = 0; j < s1; j++) {
        if (b[c][j] && !a[j][p] && !vis[b[c][j]]) {
          if (b[c][j] < minn) {
            minn = b[c][j];
            zz = j;
          }
        }
      }
    }
  }
  return 0;
}

