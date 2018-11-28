#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define N 26

char s[N][N];

void Solve(){
  int n, m;
  scanf("%d%d", &n, &m);
  for(int i = 0; i < n; i++)
    scanf("%s", s[i]);
  for(int i = 0; i < n; i++){
    int cnt = 0, i1, i2 = n, ix;

    for(ix = i; ix < n; ix++){
      int j;
      for(j = 0; j < m && s[ix][j] == '?'; j++);
      if(j != m){
        cnt++;
        if(cnt == 1)
          i1 = ix;
        else if(cnt == 2){
          i2 = ix;
          break;
        }
      }
    }

    for(int j = 0; j < m; j++){
      int cnt = 0, j1, j2 = m, jx;

      for(int jx = j; jx < m; jx++){
        if(s[i1][jx] != '?'){
          cnt++;
          if(cnt == 1)
            j1 = jx;
          else if(cnt == 2){
            j2 = jx;
            break;
          }
        }
      }

      for(int x = i; x < i2; x++)
        for(int y = j; y < j2; y++)
          s[x][y] = s[i1][j1];
      j = j2 - 1;
    }
    i = i2 - 1;
  }

  for(int i = 0; i < n; i++)
    printf("%s\n", s[i]);
}

int main(){
  int t;
  scanf("%d", &t);
  for(int k = 1; k <= t; k++){
    printf("Case #%d: \n", k);
    Solve();
  }
  return 0;
}
