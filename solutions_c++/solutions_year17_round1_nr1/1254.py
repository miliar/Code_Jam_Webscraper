#include <bits/stdc++.h>

using namespace std;

const int N = 100;

int n, m;
int done[N][N];
pair < int, int > slv[N];

int main(){
  #ifdef pts
    freopen("1.inp", "r", stdin);
  #endif // pts
  freopen("wat.out", "w", stdout);
  int nTest;
  scanf("%d", &nTest);
  for(int tt = 1; tt <= nTest; ++tt){
    scanf("%d%d", &n, &m);
    char a[N][N];
    char b[N][N];
    for(int i = 1; i <= n; ++i){
      scanf("%s", a[i] + 1);
    }
    vector < int > pos[N];
    for(int i = 1; i <= n; ++i){
      for(int j = 1; j <= m; ++j){
        if(a[i][j] != '?'){
          pos[i].push_back(j);
        }
      }
    }
    int cnt = 0;
    for(int i = 1; i <= n; ++i){
      pos[i].push_back(m + 1);
      if(pos[i].size() > 1){
        for(int x = 1; x < pos[i][0]; ++x){
          a[i][x] = a[i][pos[i][0]];
        }
      }
      for(int j = 0; j < pos[i].size() - 1; ++j){
        for(int x = pos[i][j]; x < pos[i][j + 1]; ++x){
          a[i][x] = a[i][pos[i][j]];
        }
      }
    }
    for(int i = 1; i <= n; ++i){
      for(int j = 1; j <= m; ++j){
        if(a[i][j] == '?' && a[i - 1][j] <= 'Z' && a[i - 1][j] >= 'A'){
          a[i][j] = a[i - 1][j];
        }
      }
    }
    for(int i = n; i >= 1; --i){
      for(int j = 1; j <= m; ++j){
        if(a[i][j] == '?' && a[i + 1][j] <= 'Z' && a[i + 1][j] >= 'A'){
          a[i][j] = a[i + 1][j];
        }
      }
    }
    cout << "Case #"<< tt << ":" << endl;
    for(int i = 1; i <= n; ++i){
      for(int j = 1; j <= m; ++j){
        cout << a[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
