#include <bits/stdc++.h>
using namespace std;
#define N 514
char c[ N ];
int n;
bool go( int now , int pre ){
  if( now == n ){
    puts( c );
    return true;
  }
  int cur = c[ now ] - '0';
  if( cur >= pre ){
    if( go( now + 1 , cur ) )
      return true;
  }
  if( cur and cur - 1 >= pre ){
    cur --;
    if( cur ){
      for( int i = 0 ; i < now ; i ++ )
        putchar( c[ i ] );
      printf( "%d" , cur );
    }
    for( int i = now + 1 ; i < n ; i ++ )
      putchar( '9' );
    puts( "" );
    return true;
  }
  return false;
}
void solve(){
  n = strlen( c );
  assert( go( 0 , 0 ) );
}
int main(){
  int _; scanf( "%d" , &_ );
  for( int cs = 1 ; cs <= _ ; cs ++ ){
    scanf( "%s" , c );
    printf( "Case #%d: " , cs );
    solve();
  }
}
