#include <bits/stdc++.h>
using namespace std;
#define N 1021
char c[ N ];
int n , k;
void init(){
  scanf( "%s%d" , c + 1 , &k );
  n = strlen( c + 1 );
}
void solve(){
  queue<int> Q;
  int ans = 0;
  for( int i = 1 ; i <= n ; i ++ ){
    int vl = ( c[ i ] == '+' ? 0 : 1 );
    while( Q.size() and Q.front() <= i - k ) Q.pop();
    vl = ( vl + (int)Q.size() ) % 2;
    if( vl == 0 ) continue;
    if( i + k - 1 <= n ){
      Q.push( i );
      ans ++;
    }else{
      puts( "IMPOSSIBLE" );
      return;
    }
  }
  printf( "%d\n" , ans );
}
int main(){
  int _; scanf( "%d" , &_ );
  for( int cs = 1 ; cs <= _ ; cs ++ ){
    init();
    printf( "Case #%d: " , cs );
    solve();
  }
}
