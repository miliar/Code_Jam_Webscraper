#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
#define okf(x) ((x) >= 0 && (x) < n)
#define okc(x) ((x) >= 0 && (x) < m)
const int MAXN = 1005;

int tc, n, m, TC;
string grid[MAXN];

void expand(int f, int c){
  forn(i, m){
    int x = f;
    int y = c + i;
    if(!okc(y)) break;
    if(grid[x][y] != '?' && 
       grid[x][y] != grid[f][c]) break;
    grid[x][y] = grid[f][c];
  }
  forn(i, m){
    int x = f;
    int y = c - i;
    if(!okc(y)) break;
    if(grid[x][y] != '?' &&
       grid[x][y] != grid[f][c]) break;
    grid[x][y] = grid[f][c];
  }
}

void expandVertical(int f, int c){
  forn(i, n){
    int x = f + i;
    int y = c;
    if(!okf(x)) break;
    if(grid[x][y] != '?' &&
       grid[x][y] != grid[f][c]) break;
    grid[x][y] = grid[f][c];
  }
  forn(i, n){
    int x = f - i;
    int y = c;
    if(!okf(x)) break;
    if(grid[x][y] != '?' &&
       grid[x][y] != grid[f][c]) break;
    grid[x][y] = grid[f][c];
  }
}

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    scanf("%d %d", &n, &m);
    forn(i, n){
      cin >> grid[i];
    }
    forn(i, n){
      forn(j, m){
        if(grid[i][j] != '?'){
          expand(i, j);
        }
      }
    }
    forn(i, n){
      forn(j, m){
        if(grid[i][j] != '?'){
          expandVertical(i, j);
        }
      }
    }
    printf("Case #%d:\n", ++TC);
    forn(i, n){
      cout << grid[i] << '\n';
    }
  }
  return 0;
}
