#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

using namespace std;

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a)      for(int i=0;i<a;i++)
#define rep2(i,a,b)      for(int i=a;i<b;i++)
using namespace std;
int test = 1;
void solve() {
  cout << "Case #" << test++ << ": " << endl;
  int r, c;
  char g[25][25];
  cin >> r >> c;
  rep (i, r) {
    rep (j, c) {
      cin >> g[i][j];
    }
  }

  rep (i, r) {
    rep (j, c) {
      char x = g[i][j];
      if (x != '?') {
        int line = i - 1;
        while(line >= 0 && g[line][j] == '?') {
          g[line][j] = x;
          line--;
        }
        
        line = i + 1;
        while(line < r && g[line][j] == '?') {
          g[line][j] = x;
          line++;
        }
      }
    }
  }

  rep (i, r) {
    rep (j, c) {
      char x = g[i][j];
      if (x != '?') {
        int col = j - 1;
        while(col >= 0 && g[i][col] == '?') {
          g[i][col] = x;
          col--;
        }

        col = j + 1;
        while(col < c && g[i][col] == '?') {
          g[i][col] = x;
          col++;
        }
      }
    }
  }

  
  rep (i, r) {
    rep (j, c) { 
      cout << g[i][j];
    }
    cout << endl;
  }
}

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
