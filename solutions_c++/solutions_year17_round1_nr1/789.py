#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

int fillcol(vector<vector<char>>& grid, int C, int rows) {
  char init = '-';
  for (int i = 0; i < rows; i++){
    if (grid[i][C] != '?') {
      init = grid[i][C];
      break;
    }
  }
  if (init == '-') return -1;
  for (int i = 0; i < rows; i++){
    if (grid[i][C] == '?') {
      grid[i][C] = init;
    } else {
      init = grid[i][C];
    }
  }
  return C;
}

void fillemptycol(vector<vector<char>>& grid, int C, int rows) {
  for (int i = 0; i < rows; i++){
    if (grid[i][C] != '?') {
      return;
    }
  }
  for (int i = 0; i < rows; i++) {
    grid[i][C] = grid[i][C-1];
  }
}

void copycol(vector<vector<char>>& grid, int C, int rows, int srcC){
  for (int i = 0; i < rows; i++) {
    grid[i][C] = grid[i][srcC];
  }
}

int main(){
  int T;
  int cases = 1;
  cin >> T;
  while(T--){
    int R, C;
    cin >> R >> C;

    vector<vector<char>> grid(R);
    for (int i = 0; i < R; i++){
      grid[i].resize(C);
      for (int j = 0; j < C; j++) {
        scanf(" %c", &grid[i][j]);
      }
    }
    int mincol = -1;
    for (int col = 0; col < C; col++) {
      int ax = fillcol(grid, col, R);
      if (ax != -1) {
        if (mincol == -1) mincol = ax;
      }
    }
    for (int col = 0; col < mincol; col++){
      copycol(grid, col, R, mincol);
    }
    for (int col = mincol+1; col < C; col++) {
      fillemptycol(grid, col, R);
    }

    printf("Case #%d:\n", cases++);
    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        printf("%c", grid[i][j]);
      }
      printf("\n");
    }
  }

  return 0;
}
