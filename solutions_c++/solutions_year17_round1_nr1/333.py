#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define pb(x) push_back(x)
#define sz(a) ((int)(a.size()))

#define MAX 28

char f[MAX][MAX];
int r, c;

int main() {
  ios ::sync_with_stdio(0);

  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> r >> c;
    for (int i = 0; i < r; ++i) {
      cin >> f[i];
    }

    for (int i = 0; i < r; ++i) {
      vector<char> seen;
      for (int j = c - 1; j >= 0; --j) {
        if (f[i][j] != '?') {
          seen.pb(f[i][j]);
        }
      }

      if (sz(seen) == 0) continue;

      for (int j = 0; j < c; ++j) {
        if (f[i][j] == '?') {
          f[i][j] = seen[sz(seen) - 1];
        } else {
          if (sz(seen) > 1) {
            seen.pop_back();
          }
        }
      }
    }

    vector<int> seen;
    for (int i = r - 1; i >= 0; --i) {
      if (f[i][0] != '?') {
        seen.pb(i);
      }
    }

    for (int i = 0; i < r; ++i) {
      if (f[i][0] == '?') {
        for (int j = 0; j < c; ++j) {
          f[i][j] = f[seen[sz(seen) - 1]][j];
        }
      } else {
        if (sz(seen) > 1) seen.pop_back();
      }
    }

    printf("Case #%d:\n", cn);
    for (int i = 0; i < r; ++i) {
      printf("%s\n", f[i]);
    }
  }
  return 0;
}
