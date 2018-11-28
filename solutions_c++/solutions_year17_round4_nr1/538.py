// eddy1021
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
typedef double D;
typedef long double LD;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
#define mod9 1000000009LL
#define mod7 1000000007LL
#define INF  1023456789LL
#define INF16 10000000000000000LL
#define eps 1e-9
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(), (x).end()
#ifndef ONLINE_JUDGE
#define debug(...) printf(__VA_ARGS__)
#else 
#define debug(...)
#endif
inline LL getint(){
  LL _x=0,_tmp=1; char _tc=getchar();    
  while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
  if( _tc == '-' ) _tc=getchar() , _tmp = -1;
  while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
  return _x*_tmp;
}
inline LL add( LL _x , LL _y , LL _mod = mod7 ){
  _x += _y;
  return _x >= _mod ? _x - _mod : _x;
}
inline LL sub( LL _x , LL _y , LL _mod = mod7 ){
  _x -= _y;
  return _x < 0 ? _x + _mod : _x;
}
inline LL mul( LL _x , LL _y , LL _mod = mod7 ){
  _x *= _y;
  return _x >= _mod ? _x % _mod : _x;
}
LL mypow( LL _a , LL _x , LL _mod ){
  if( _x == 0 ) return 1LL;
  LL _ret = mypow( mul( _a , _a , _mod ) , _x >> 1 , _mod );
  if( _x & 1 ) _ret = mul( _ret , _a , _mod );
  return _ret;
}
LL mymul( LL _a , LL _x , LL _mod ){
  if( _x == 0 ) return 0LL;
  LL _ret = mymul( add( _a , _a , _mod ) , _x >> 1 , _mod );
  if( _x & 1 ) _ret = add( _ret , _a , _mod );
  return _ret;
}
inline bool equal( D _x ,  D _y ){
  return _x > _y - eps && _x < _y + eps;
}
#define Bye exit(0)
int __ = 1 , _cs;
/*********default*********/
#define N 121
int dp1[ N ][ N ];
int dp2[ N ][ N ][ N ];
void build(){
  for( int i = 0 ; i < N ; i ++ )
    for( int j = 0 ; j < N ; j ++ ){
      if( i > 0 and j > 0 )
        dp1[ i ][ j ] = max( dp1[ i ][ j ] , dp1[ i - 1 ][ j - 1 ] + 1 );
      if( i > 2 )
        dp1[ i ][ j ] = max( dp1[ i ][ j ] , dp1[ i - 3 ][ j ] + 1 );
      if( j > 2 )
        dp1[ i ][ j ] = max( dp1[ i ][ j ] , dp1[ i ][ j - 3 ] + 1 );
      for( int k = 0 ; k < N ; k ++ ){
        if( i > 3 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i - 4 ][ j ][ k ] + 1 );
        if( k > 3 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i ][ j ][ k - 4 ] + 1 );
        if( j > 1 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i ][ j - 2 ][ k ] + 1 );
        if( i > 1 and j > 0 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i - 2 ][ j - 1 ][ k ] + 1 );
        if( j > 0 and k > 1 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i ][ j - 1 ][ k - 2 ] + 1 );
        if( i > 0 and k > 0 )
          dp2[ i ][ j ][ k ] = max( dp2[ i ][ j ][ k ] ,
                                    dp2[ i - 1 ][ j ][ k - 1 ] + 1 );
      }
    }
}
int n , p , g[ N ];
void init(){
  n = getint();
  p = getint();
  for( int i = 0 ; i < p ; i ++ )
    g[ i ] = 0;
  while( n -- ) g[ getint() % p ] ++;
}
void solve(){
  int ans = g[ 0 ];
  if( p == 2 ){
    ans += ( g[ 1 ] + 1 ) / 2;
  }else if( p == 3 ){
    int bns = 0;
    for( int i = 0 ; i <= g[ 1 ] ; i ++ )
      for( int j = 0 ; j <= g[ 2 ] ; j ++ ){
        if( i == g[ 1 ] and j == g[ 2 ] ) continue;
        bns = max( bns , dp1[ i ][ j ] + 1 );
      }
    ans += bns;
  }else{
    int bns = 0;
    for( int i = 0 ; i <= g[ 1 ] ; i ++ )
      for( int j = 0 ; j <= g[ 2 ] ; j ++ )
        for( int k = 0 ; k <= g[ 3 ] ; k ++ ){
          if( i == g[ 1 ] and j == g[ 2 ] and k == g[ 3 ] ) continue;
          bns = max( bns , dp2[ i ][ j ][ k ] + 1 );
        }
    ans += bns;
  }
  printf( "Case #%d: %d\n" , ++ _cs , ans );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    clock_t s = clock();
    init();
    solve();
    clock_t t = clock();
    fprintf( stderr , "Solved case #%d in %.6f\n" ,
             _cs , (double)(t - s)/CLOCKS_PER_SEC );
    fflush( stderr );
  }
}
