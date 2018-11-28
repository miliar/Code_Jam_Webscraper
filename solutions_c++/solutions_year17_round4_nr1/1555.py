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

int n , p ;
int s[ 10 ] ;

void init() {
  memset( s , 0 , sizeof s ) ;
  scanf( "%d%d" , &n , &p ) ;
  for ( int i = 0 ; i < n ; i ++ ) {
    int x ;
    scanf( "%d" , &x ) ;
    s[ x % p ] ++ ;
  }
}

void process() {
  if ( p == 2 ) {
    int ans = s[ 0 ] ;
    if ( s[ 1 ] ) ans += ( s[ 1 ] - 1 ) / 2 + 1 ;
    printf( "%d\n" , ans ) ;
  } else if ( p == 3 ) {
    int ans = s[ 0 ] ;
    int tmp = min( s[ 1 ] , s[ 2 ] ) ;
    s[ 1 ] -= tmp , s[ 2 ] -= tmp ;
    ans += tmp ;
    if ( s[ 1 ] ) ans += ( s[ 1 ] - 1 ) / 3 + 1 ;
    else if ( s[ 2 ] ) ans += ( s[ 2 ] - 1 ) / 3 + 1 ;
    printf( "%d\n" , ans ) ;
  }
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

