#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

typedef pair<int, int> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

int T;
int H, W;
char X[25][25];

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, T) {
    cin >> H >> W;
    rep(i, H) {
      rep(j, W) {
        cin >> X[j][i];
      }
    }
    rep(x, W) {
      for (int y=1; y<H; y++) {
        if (X[x][y] == '?') X[x][y] = X[x][y-1];
      }
      for (int y=H-2; y>=0; y--) {
        if (X[x][y] == '?') X[x][y] = X[x][y+1];
      }
    }
    rep(y, H) {
      for (int x=1; x<W; x++) {
        if (X[x][y] == '?') X[x][y] = X[x-1][y];
      }
      for (int x=W-2; x>=0; x--) {
        if (X[x][y] == '?') X[x][y] = X[x+1][y];
      }
    }

    cout << "Case #" << i+1 << ":\n";
    rep(i, H) {
      rep(j, W) {
        cout << X[j][i];
      }
      cout << "\n";
    }
  }
  return 0;
}
