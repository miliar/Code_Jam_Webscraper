#include <bits/stdc++.h>

using namespace std;

const int N = 110;

int c[N];
int a[N][N];
int perm[N];

int main(){
  #ifdef pts
    freopen("1.inp", "r", stdin);
  #endif // pts
  freopen("1.out", "w", stdout);
  int ntt;
  scanf("%d", &ntt);
  for(int tt = 1; tt <= ntt; ++tt){
    cout << "Case #" << tt << ": ";
    int n, p;
    scanf("%d%d", &n, &p);
    for(int i = 1; i <= n; ++i){
      scanf("%d", c + i);
    }
    for(int i = 1; i <= n; ++i){
      for(int j = 1; j <= p; ++j){
        scanf("%d", &a[i][j]);
      }
    }
    if(n == 1){
      int answer = 0;
      for(int i = 1; i <= p; ++i){
        int x = a[1][i] / c[1];
        for(int u = (9 * a[1][i]) / (11 * c[1]); c[1] * u * 9 <= a[1][i] * 10; ++u){
          if(u < 1){
            continue;
          }
          if(a[1][i] * 10 >= c[1] * u * 9 && a[1][i] * 10 <= c[1] * 11 * u){
            ++answer;
            break;
          }
        }
      }
      cout << answer << endl;
      continue;
    }
    for(int i = 1; i <= p; ++i){
      perm[i] = i;
    }
    cerr << tt << endl;
    int result = 0;
    do{
      int ans = 0;
      for(int i = 1; i <= p; ++i){
        int x = a[1][i] / c[1];
        for(int u = (10 * a[1][i]) / (11 * c[1]); c[1] * u * 9 <= a[1][i] * 10; ++u){
          if(u < 1){
            continue;
          }
          if(a[1][i] * 10 >= c[1] * u * 9 && a[1][i] * 10 <= c[1] * 11 * u){
            if(a[2][perm[i]] * 10 >= c[2] * u * 9 && a[2][perm[i]] * 10 <= c[2] * 11 * u){
              ++ans;
              break;
            }
          }
        }
      }
      result = max(result, ans);
    } while(next_permutation(perm + 1, perm + p + 1));
    cout << result << endl;
  }
  return 0;
}
