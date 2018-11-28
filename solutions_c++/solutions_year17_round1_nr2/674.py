#include <bits/stdc++.h>
#include <unistd.h>
#include <algorithm>
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

#define MAXN 52
#define MAXM 52
int n,m;
int r[MAXN];
int q[MAXN][MAXM];
int iter[MAXN];
vector<vector<PII> > interval;
int match(int i, int lower, int upper){
  if ( lower > upper ) return 0;
  if ( i >= n ){
    return lower <= upper;
  }
  int *j = &iter[i];
  while( *j < m ){
    if ( upper < interval[i][*j].first)
      break;
    int rc = match(i+1, max(interval[i][*j].first, lower), min(interval[i][*j].second, upper));
    ++(*j);
    if ( rc ){
      return 1;
    }
  }
  return 0;
}
void solve(){
  scanf("%d%d", &n, &m);
  for (int i=0; i<n; ++i){
    scanf("%d", &r[i]);
  }
  for (int i=0; i<n; ++i){
    for (int j=0; j<m; ++j){
      scanf("%d",&q[i][j]);
    }
  }
  interval.clear();
  for (int i=0; i<n; ++i){
    vector<PII> inv;
    for (int j=0; j<m; ++j){
      int lower = int( double(q[i][j] + 1.1*r[i]-1) / 1.1 / r[i] );
      int upper = int( double(q[i][j]) / 0.9 / r[i] );
      inv.push_back(MP(lower,upper));
    }
    sort(inv.begin(),inv.end());
    interval.push_back(inv);

    iter[i] = 0;
  }
  int count = 0;
  for (int j=0; j<m; ++j){
    count += match(1, interval[0][j].first, interval[0][j].second);
  }
  printf("%d\n", count);
}
int main(){
  int T;
  scanf("%d", &T);
  for (int i=0; i<T; ++i){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
