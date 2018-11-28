#include<bits/stdc++.h>
using namespace std;
const int MAXN = 105;
int n, q;
int e[MAXN], s[MAXN];

const long long INF = 100000000000000;
long long w[MAXN][MAXN];
double ww[MAXN][MAXN];

void solve() {

  for ( int k = 0 ; k < n ; k++ )
    for ( int i = 0 ; i < n ; i++ ) {
      for ( int j = 0 ; j < n ; j++ ) {
        w[i][j] = min(w[i][j], w[i][k] + w[k][j]);
        ww[i][j] = INF;
      }
      ww[i][i] = 0;
    }



  for ( int k = 0 ; k < n ; k++ )
    for ( int i = 0 ; i < n ; i++ )
      for ( int j = 0 ; j < n ; j++ ) {
        if ( i == j && j == k) continue;
        if ( e[i] >= w[i][k] + w[k][j] ) ww[i][j] = min(ww[i][j], (double)(w[i][k] + w[k][j])/s[i] );
      }
  for ( int k = 0 ; k < n ; k++ )
    for ( int i = 0 ; i < n ; i++ )
      for ( int j = 0 ; j < n ; j++ ) ww[i][j] = min(ww[i][j], ww[i][k] + ww[k][j]);
}

int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int T, kase = 0;
  cin >> T;
  while (T--) {
    cin >> n >> q;
    for ( int i = 0; i < n ; i++ ) {
      cin >> e[i] >> s[i];
    }
    for ( int i = 0 ; i < n ; i++ ) {
      for ( int j = 0 ; j < n ; j++ ) {
        cin >> w[i][j];
        if ( w[i][j] == -1) w[i][j] = INF;
      }
      w[i][i] = 0;
    }
    solve();
    printf("Case #%d:", ++kase);
    while (q--) {

      int a, b;
      cin >> a >> b;
      printf(" %.8lf", ww[a-1][b-1]);
    }
    cout << endl;

  }
}
