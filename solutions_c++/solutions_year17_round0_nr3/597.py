#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL n , k;
void solve(){
  map<LL,LL> M;
  M[ n ] = 1;
  while( k ){
    auto it = --M.end();
    LL r = it->first , c = it->second;
    M.erase( it );
    k -= c;
    r -= 1;
    LL lft = r / 2;
    LL rgt = r - lft;
    if( lft ) M[ lft ] += c;
    if( rgt ) M[ rgt ] += c;
    if( k <= 0 ){
      printf( "%lld %lld\n" , rgt , lft );
      return;
    }
  }
}
int main(){
  int _; scanf( "%d" , &_ );
  for( int cs = 1 ; cs <= _ ; cs ++ ){
    clock_t s = clock();
    scanf( "%lld%lld" , &n , &k );
    printf( "Case #%d: " , cs );
    solve();
    clock_t t = clock();
    fprintf( stderr , "Solved #%d in %.6f seconds\n" , 
             cs , (double)( t - s ) / CLOCKS_PER_SEC );
  }
}
