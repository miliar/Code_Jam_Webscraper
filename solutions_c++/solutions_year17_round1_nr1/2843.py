#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>

using namespace std;

#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define fup(i, a, b) for (__typeof(a) i = (a); i <= (b); ++i)
#define fdown(i, a, b) for (__typeof(a) i = (a); i >= (b); --i)
#define all(x) (x).begin(),(x).end()
#define forall(i, x) fup(i, (x).begin(),(x).end())
#define debug(x) cout << #x << " = " << x << "\n"


int R, C;
char grid[30][30];
bool l[256];

void swp(int &a, int &b) { if (a > b) { int aux = a; a = b; b = aux; } }

char check(int i, int j, int ii, int jj) {
  swp(i,ii);
  swp(j,jj);
  char c = '?';
  fup (a,i,ii) fup(b,j,jj) {
    if (grid[a][b] != '?') {
      if (c != '?') return -1;
      c = grid[a][b];
    }
  }
  if (c == '?') return -1;
  return c;
}

void paint(int i, int j, int ii, int jj, char c) { swp(i,ii); swp(j,jj); fup (a,i,ii) fup(b,j,jj) grid[a][b] = c; } 
bool go() {
  int c = 0;
  char aux[30][30];
  memcpy(aux, grid, sizeof aux);
  rep(i,R) rep(j,C) if (grid[i][j] == '?') {
    ++c;
    rep(ii,R) rep(jj,C) {
      char c = check(i,j,ii,jj);
      if (c != -1 && l[(int)c] == false) {
        l[(int)c] = true;
        paint(i,j,ii,jj,c);
        if (go()) {
          //puts("---");
          //rep(i, R) puts(aux[i]);
          return true;
        }
        memcpy(grid, aux, sizeof grid);
        l[(int)c] = false;
      }
    }
  }
  if (c == 0) return true;
  return false;
}


int main() {
  int t, c = 0;

  for (scanf("%d", &t); t--;) {
    scanf("%d %d", &R, &C);

    rep(i, R) scanf("%s", grid[i]);

    memset(l,false,sizeof l);
    go();

    printf("Case #%d:\n", ++c);
    rep(i, R) puts(grid[i]);
  }

  return 0;
}
