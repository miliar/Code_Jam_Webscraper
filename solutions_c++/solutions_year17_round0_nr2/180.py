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

ll n ;

void init() {
  scanf( "%lld" , &n ) ;
}

bool check( ll x ) {
  int lst = 9 ;
  while ( x ) {
    if ( x % 10 > lst ) return false ;
    lst = x % 10 ;
    x /= 10 ;
  }
  return true ;
}

void process() {
  ll bs = 10 ;
  while ( !check( n ) ) {
    ll t = ( n % bs ) / ( bs / 10 ) ;
    n = n - bs + ( 9 - t ) * ( bs / 10 ) ;
    bs *= 10 ;
  }
  printf( "%lld\n" , n ) ;
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

