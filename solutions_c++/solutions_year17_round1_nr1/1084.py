#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
#include <ext/numeric>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <bitset>
#include <tuple>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef complex<double> Point;
#define X(p) real(p)
#define Y(p) imag(p)

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)
#define FOR(v, it) for (auto it = v.begin(); it != v.end(); ++it)

int r; int c;
char mat[128][128];
int main() {
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    cin >> r >> c;
    for (int i = 0; i < r; ++i) {
      cin >> mat[i];
    }

    for (int x = 0; x < c; ++x) {
      for (int y = 0; y < r; ++y) {
        if (mat[y][x] != '?' && isupper(mat[y][x])) {
          char ch = tolower(mat[y][x]);
          #ifdef DEBUG
          cout << "propagating " << ch << endl;
          #endif
          int top = y;
          int bot = y;
          int left = x;
          int right = x;
          for (int dy = -1; y + dy  >= 0; --dy) {
            if (mat[y + dy][x] == '?') {
              top = y + dy;
              mat[y + dy][x] = ch;
            } else {
              break;
            }
          }
          #ifdef DEBUG
          cout << "t: " << top << " b: " << bot << " l: " << left << " r: " << right << endl;
          #endif

          for (int dy = 1; y + dy < r; ++dy) {
            if (mat[y + dy][x] == '?') {
              bot = y + dy;
              mat[y + dy][x] = ch;
            } else {
              break;
            }
          }
          #ifdef DEBUG
          cout << "t: " << top << " b: " << bot << " l: " << left << " r: " << right << endl;
          #endif

          for (int dx = -1; x + dx >= 0; --dx) {
            int nx = x + dx;
            if (mat[y][nx] == '?') {
              bool ok = true;
              for (int ny = top; ny <= bot; ++ny) {
                if (mat[ny][nx] != '?') {
                  ok = false;
                  break;
                }
              }
              if (ok) {
                for (int ny = top; ny <= bot; ++ny) {
                  mat[ny][nx] = ch;
                }
                left = nx;
              } else {
                break;
              }
            } else {
              break;
            }
          }
          #ifdef DEBUG
          cout << "t: " << top << " b: " << bot << " l: " << left << " r: " << right << endl;
          #endif


          for (int dx = 1; x + dx < c; ++dx) {
            int nx = x + dx;
            if (mat[y][nx] == '?') {
              bool ok = true;
              for (int ny = top; ny <= bot; ++ny) {
                if (mat[ny][nx] != '?') {
                  ok = false;
                  break;
                }
              }
              if (ok) {
                for (int ny = top; ny <= bot; ++ny) {
                  mat[ny][nx] = ch;
                }
                right = nx;
              } else {
                break;
              }
            } else {
              break;
            }
          }
          #ifdef DEBUG
          cout << "t: " << top << " b: " << bot << " l: " << left << " r: " << right << endl;
          #endif
        }
      }
    }
    cout << "Case #" << ctr + 1 << ":" << endl;
    for (int y = 0; y < r; ++y) {
      for (int x = 0; x < c; ++x) {
        cout << char(toupper(mat[y][x]));
      }
      cout << endl;
    }
  }

  return 0;
}
