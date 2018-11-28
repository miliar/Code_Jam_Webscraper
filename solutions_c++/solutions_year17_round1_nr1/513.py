#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int R, C;
    cin >> R >> C;
    vector<string> g(R);
    for (int i=0;i<R;i++) {
      cin >> g[i];
      for (int j=1;j<C;j++) {
        if (g[i][j]=='?') g[i][j] = g[i][j-1];
      }
      for (int j=C-2;j>=0;j--) {
        if (g[i][j]=='?') g[i][j] = g[i][j+1];
      }
    }
    for (int i=1;i<R;i++) {
      if (g[i][0] == '?') g[i] = g[i-1];
    }
    for (int i=R-2;i>=0;i--) {
      if (g[i][0] == '?') g[i] = g[i+1];
    }
    printf("Case #%d:\n", t);
    for (int i=0;i<R;i++) {
      cout << g[i] << endl;
    }
  }

}
