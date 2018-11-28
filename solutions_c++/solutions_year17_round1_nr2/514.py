//by tzupengwang™
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , p ;
int bs[ 55 ] ;
int wt[ 55 ][ 55 ] ;
vector< ii > in[ 55 ] ;
vector< int > ds ;

void init() {
  scanf( "%d%d" , &n , &p ) ;
  for ( int i = 0 ; i < n ; i ++ ) {
    scanf( "%d" , &bs[ i ] ) ;
    in[ i ].clear() ;
  }
  ds.clear() ;
  for ( int i = 0 ; i < n ; i ++ ) {
    for ( int j = 0 ; j < p ; j ++ ) {
      scanf( "%d" , &wt[ i ][ j ] ) ;
      int hb = (int)floor((double)wt[ i ][ j ] / 0.9 ) / bs[ i ] ;
      int lb = ( (int)ceil((double)wt[ i ][ j ] / 1.1 ) - 1 ) / bs[ i ] + 1 ;
      // printf( "%d %d\n" , lb , hb ) ;
      if ( lb > hb ) continue ;
      in[ i ].push_back( ii( lb , hb ) ) ;
      ds.push_back( lb ) ;
      ds.push_back( hb ) ;
    }
  }
  sort( ds.begin() , ds.end() ) ;
  ds.resize( unique( ds.begin() , ds.end() ) - ds.begin() ) ;
  for ( int i = 0 ; i < n ; i ++ ) {
    sort( in[ i ].begin() , in[ i ].end() ) ;
    reverse( in[ i ].begin() , in[ i ].end() ) ;
  }
}

void process() {
  int ans = 0 ;
  for ( int ps : ds ) {
    while ( true ) {
      bool ok = true ;
      for ( int i = 0 ; i < n ; i ++ ) {
        while ( in[ i ].size() && in[ i ].back().second < ps )
          in[ i ].pop_back() ;

        if ( in[ i ].size() == 0 || in[ i ].back().first > ps )
          ok = false ;
      }
      if ( !ok ) break ;
      else {
        for ( int i = 0 ; i < n ; i ++ )
          in[ i ].pop_back() ;
        ans ++ ;
      }
    }
  }
  printf( "%d\n" , ans ) ;
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

