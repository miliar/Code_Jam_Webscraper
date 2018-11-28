#include <bits/stdc++.h>
using namespace std;

int i, j, test, tests, n, m;
bool viz[100][100];
string a[100];

int isEmpty(int x, int y, int z, int w) {
  int cnt = 0;
  for(int i = x; i <= z; ++i)
    for(int j = y; j <= w; ++j)
      if(a[i][j] != '?') ++cnt;

  return cnt < 2;
}

void color(int x, int y, int z, int w, char col) {
  for(int i = x; i <= z; ++i)
    for(int j = y; j <= w; ++j)
      a[i][j] = col;
}

int main() {
  ifstream cin("test1.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    memset(viz, 0, sizeof(viz));
    cout << "Case #" << test << ":\n";

    cin >> n >> m;
    for(i = 0; i < n; ++i) a[i].clear();
    for(i = 0; i < n; ++i) cin >> a[i];

    for(i = 0; i < n; ++i)
      for(j = 0; j < m; ++j)
        if(a[i][j] != '?') viz[i][j] = 1;

    for(i = 0; i < n; ++i)
      for(j = 0; j < m; ++j) {
        if(!viz[i][j]) continue;

        int x = i, y = j, z = i, w = j;
        int expand = -1;

        while(x > 0 && y > 0 && isEmpty(x - 1, y - 1, z, w)) --x, --y, expand = 0;
        while(z < n - 1 && w < m - 1 && isEmpty(x, y, z + 1, w + 1)) ++z, ++w, expand = 0;
        while(x > 0 && w < m - 1 && isEmpty(x - 1, y, z, w + 1)) ++w, --x, expand = 0;
        while(z < n - 1 && y > 0 && isEmpty(x, y - 1, z + 1, w)) ++z, --y, expand = 0;

        while(y > 0 && isEmpty(x, y - 1, z, w)) --y, expand = 1;
        while(w < m - 1 && isEmpty(x, y, z, w + 1)) ++w, expand = 1;

        while(x > 0 && isEmpty(x - 1, y, z, w)) --x;
        while(z < n - 1 && isEmpty(x, y, z + 1, w)) ++z;

        color(x, y, z, w, a[i][j]);
      }

    for(i = 0; i < n; ++i) cout << a[i] << '\n';
  }

  return 0;
}