#include <bits/stdc++.h>
#include <unistd.h>
#define SZ(x) ((int)(x).size())
#define ALL(x) begin(x),end(x)
#define REP(i,n) for ( int i=0; i<int(n); i++ )
#define REP1(i,a,b) for ( int i=(a); i<=int(b); i++ )
#define FOR(it,c) for ( auto it=(c).begin(); it!=(c).end(); it++ )
#define MP make_pair
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define MAXN 30
char cake[MAXN][MAXN];
void solve(){
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i=0; i<n; ++i){
    scanf("%s", cake[i]);
  }
  for (int i=0; i<n; ++i){
    for (int j=0; j<m; ++j){
      if (cake[i][j]!='?'){
        // extend
        for (int jj=j-1; jj>=0 && cake[i][jj]=='?'; --jj)
          cake[i][jj] = cake[i][j];
        for (int jj=j+1; jj<m && cake[i][jj]=='?'; ++jj)
          cake[i][jj] = cake[i][j];
      }
    }
  }
  for (int i=0; i<n; ++i){
    for (int j=0; j<m; ++j){
      if (cake[i][j]!='?'){
        // extend
        for (int ii=i-1; ii>=0 && cake[ii][j]=='?'; --ii)
          cake[ii][j] = cake[i][j];
        for (int ii=i+1; ii<n && cake[ii][j]=='?'; ++ii)
          cake[ii][j] = cake[i][j];
      }
    }
  }
  for (int i=0; i<n; ++i){
    printf("%s\n", cake[i]);
  }
}
int main(){
  int T;
  scanf("%d", &T);
  for (int i=0; i<T; ++i){
    printf("Case #%d:\n",i+1);
    solve();
  }
  return 0;
}
