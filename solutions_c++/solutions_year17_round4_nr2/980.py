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

int n , c , m ;
int s[ 1005 ] ;
int cnt[ 1005 ] ;

void init() {
  memset( s , 0 , sizeof s ) ;
  memset( cnt , 0 , sizeof cnt ) ;
  scanf( "%d%d%d" , &n , &c , &m ) ;
  for ( int i = 0 ; i < m ; i ++ ) {
    int x , y ;
    scanf( "%d%d" , &x , &y ) ;
    cnt[ y ] ++ ;
    s[ x ] ++ ;
  }
}

int ok( int x ) {
  int av = 0 , promo = 0 ;
  for ( int i = 1 ; i <= n ; i ++ ) {
    if ( x > s[ i ] ) {
      av += x - s[ i ] ;
    } else {
      if ( av < s[ i ] - x )
        return -1 ;
      promo += s[ i ] - x ;
      av -= s[ i ] - x ;
    }
  }
  return promo ;
}

void process() {
  int low = *max_element( cnt + 1 , cnt + n + 1 ) , high = m ;
  int mn = 0 ;
  while ( low < high ) {
    int md = ( low + high ) / 2 ;
    int ls = ok( md ) ;
    if ( ls != -1 ) {
      high = md ;
      mn = ls ;
    } else low = md + 1 ;
  }
  printf( "%d %d\n" , low , mn ) ;
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

