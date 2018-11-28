//by tzupengwang™
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int r , c ;
char s[ 30 ][ 30 ] ;
char t[ 30 ][ 30 ] ;

void init() {
  scanf( "%d%d" , &r , &c ) ;
  for ( int i = 0 ; i < r ; i ++ ) {
    scanf( "%s" , s[ i ] ) ;
    for ( int j = 0 ; j <= c ; j ++ )
      t[ i ][ j ] = s[ i ][ j ] ;
  }
}

void cp( int x , int y ) {
  for ( int i = 0 ; i < c ; i ++ )
    s[ y ][ i ] = s[ x ][ i ] ;
}

bool mfill( int rr ) {
  bool ok = false ;
  for ( int i = 0 ; i < c ; i ++ )
    if ( s[ rr ][ i ] != '?' ) ok = true ;
  if ( !ok ) return false ;

  int lst = 0 ;
  for ( int i = 0 ; i < c ; i ++ ) {
    if ( s[ rr ][ i ] != '?' ) {
      for ( int j = lst ; j < i ; j ++ )
        s[ rr ][ j ] = s[ rr ][ i ] ;
      lst = i + 1;
    }
  }
  for ( int i = lst ; i < c ; i ++ ) {
    s[ rr ][ i ] = s[ rr ][ lst - 1 ] ;
  }
  int rw = rr - 1 ;
  while ( rw >= 0 && s[ rw ][ 0 ] == '?' )
    cp( rr , rw ) , rw -- ;
  return true ;
}

void process() {
  int lst = 0 ;
  for ( int i = 0 ; i < r ; i ++ ) {
    if ( mfill( i ) ) lst = i ;
  }
  for ( int i = lst + 1 ; i < r ; i ++ )
    cp( lst , i ) ;
  for ( int i = 0 ; i < r ; i ++ ) {
    puts( s[ i ] ) ;
  }
  // for ( int i = 0 ; i < r ; i ++ ) {
    // for ( int j = 0 ; j < c ; j ++ ) {
      // if ( s[ i ][ j ] != t[ i ][ j ] && t[ i ][ j ] != '?' ) {
        // puts( "FUCK" ) ;
        // for ( int ii = 0 ; ii < r ; ii ++ ) {
          // for ( int jj = 0 ; jj < c ; jj ++ ) {
            // printf( "%c" , t[ i ][ j ] ) ;
          // } puts( "" ) ;
        // }
      // }
    // }
  // }
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
    printf( "Case #%d:\n" , cases ) ;
    process() ;
  }
/*
*/
  return 0 ;
}

