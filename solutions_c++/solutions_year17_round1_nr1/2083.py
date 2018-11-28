#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

int main(int argc, char *argv[])
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int tc;
  cin >> tc;
  while (tc--) {
    int h, w;
    cin >> h >> w;
    char g[h][w];
    for (int i = 0; i < h; ++i) {
      for (int j = 0; j < w; ++j) {
        cin >> g[i][j];
      }
    }

    for (int i = 0; i < h; ++i) {
      int head = -1;
      for (int j = 0; j < w; ++j) {
        if (g[i][j] != '?') {
          head = j;
          break;
        }
      }
      if (head == -1) continue;
      for (int j = 0; j < w; ++j) {
        if (g[i][j] != '?') break;
        g[i][j] = g[i][head];
      }
      char last = g[i][head];
      for (int j = head + 1; j < w; ++j) {
        if (g[i][j] == '?') g[i][j] = last;
        else last = g[i][j];
      }
    }

    for (int j = 0; j < w; ++j) {
      char last = '?';
      for (int i = 0; i < h; ++i) {
        if (g[i][j] == '?') g[i][j] = last;
        else last = g[i][j];
      }
      last = '?';
      for (int i = h - 1; 0 <= i; --i) {
        if (g[i][j] == '?') g[i][j] = last;
        else last = g[i][j];
      }      
    }
    
    static int tc = 0;
    cout << "Case #" << ++tc << ":" << endl;
    for (int i = 0; i < h; ++i) {
      for (int j = 0; j < w; ++j) {
        cout << g[i][j];
      }
      cout << endl;
    }
  }
  
  return 0;
}
