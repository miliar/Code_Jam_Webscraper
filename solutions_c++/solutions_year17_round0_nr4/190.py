//by tzupengwang™
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
#include<cassert>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , m ;

void init() {
  scanf( "%d%d" , &n , &m ) ;
}

int p[ 2 ][ 105 ][ 105 ] ;
char ori[ 105 ][ 105 ] ;
char ans[ 105 ][ 105 ] ;

void seth( int x , int y ) {
  p[ 1 ][ x ][ y ] = 2 ;
  for ( int i = 1 ; i <= n ; i ++ ) {
    if ( i != x ) p[ 1 ][ i ][ y ] = 0 ;
    if ( i != y ) p[ 1 ][ x ][ i ] = 0 ;
  }
}
void setd( int x , int y ) {
  p[ 0 ][ x ][ y ] = 2 ;
  for ( int i = 1 ; i <= n ; i ++ )
    for ( int j = 1 ; j <= n ; j ++ )
      if ( ( i != x || j != y ) && ( i + j == x + y || i - j == x - y ) )
        p[ 0 ][ i ][ j ] = 0 ;
}

void process() {
  for ( int i = 1 ; i <= n ; i ++ )
    for ( int j = 1 ; j <= n ; j ++ ) {
      for ( int k = 0 ; k < 2 ; k ++ )
        p[ k ][ i ][ j ] = 1 ;
      ori[ i ][ j ] = '.' ;
    }

  for ( int i = 0 ; i < m ; i ++ ) {
    char buf[ 5 ] ; int x , y ;
    scanf( "%s%d%d" , buf , &x , &y ) ;
    if ( buf[ 0 ] == '+' ) {
      setd( x , y ) ;
    } else if ( buf[ 0 ] == 'x' ) {
      seth( x , y ) ;
    } else if ( buf[ 0 ] == 'o' ) {
      setd( x , y ) ;
      seth( x , y ) ;
    }
    ori[ x ][ y ] = buf[ 0 ] ;
  }

  for ( int i = 1 ; i <= n ; i ++ ) {
    for ( int j = 1 ; j <= n ; j ++ ) {
      if ( p[ 1 ][ i ][ j ] == 1 ) seth( i , j ) ;
    }
  }

  vector< ii > vv ;
  for ( int i = 1 ; i <= n ; i ++ )
    for ( int j = 1 ; j <= n ; j ++ )
      vv.push_back( ii( i , j ) ) ;

  sort( vv.begin() , vv.end() , []( ii x , ii y ) { return abs( x.first - x.second ) > abs( y.first - y.second ) ; } ) ;

  for ( ii x : vv ) {
    int i = x.first , j = x.second ;
    if ( p[ 0 ][ i ][ j ] == 1 ) setd( i , j ) ;
  }

  int cnt1 = 0 , cnt2 = 0 ;
  for ( int i = 1 ; i <= n ; i ++ ) {
    for ( int j = 1 ; j <= n ; j ++ ) {
      if ( p[ 0 ][ i ][ j ] == 2 && p[ 1 ][ i ][ j ] == 2 ) ans[ i ][ j ] = 'o' , cnt1 += 2 ;
      else if ( p[ 0 ][ i ][ j ] == 2 ) ans[ i ][ j ] = '+' , cnt1 ++ ;
      else if ( p[ 1 ][ i ][ j ] == 2 ) ans[ i ][ j ] = 'x' , cnt1 ++ ;
      else ans[ i ][ j ] = '.' ;

      if ( ans[ i ][ j ] != ori[ i ][ j ] ) cnt2 ++ ;
    }
  }

  printf( "%d %d\n" , cnt1 , cnt2 ) ;
  for ( int i = 1 ; i <= n ; i ++ )
    for ( int j = 1 ; j <= n ; j ++ )
      if ( ans[ i ][ j ] != ori[ i ][ j ] )
        printf( "%c %d %d\n" , ans[ i ][ j ] , i , j ) ;
}

int main() {
/*
#ifdef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
#endif
*/
  int Cases;
  scanf( "%d" , &Cases ) ;
  for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
    init() ;
    printf( "Case #%d: " , cases ) ;
    process() ;
  }
/*
*/
  return 0 ;
}

