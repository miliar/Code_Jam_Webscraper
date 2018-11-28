//by tzupengwang™
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<iostream>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> ii;

ll n , k ;
vector< ii > v ;
map< ll , vector< ii > > mx ;

void init() {
  scanf( "%lld%lld" , &n , &k ) ;
  mx.clear() ;
}

void merge( vector< ii > &a , vector< ii > &b ) {
  for ( ii x : a ) b.push_back( x ) ;

  sort( b.begin() , b.end() ) ;
  a.clear() ;
  for ( ii x : b ) {
    if ( a.size() == 0 ) a.push_back( x ) ;
    else if ( a.back().first == x.first ) a.back().second += x.second ;
    else a.push_back( x ) ;
  }
}

vector< ii > d( ll x ) {
  if ( mx.count( x ) ) return mx[ x ] ;

  vector< ii > v1 , v2 ;
  if ( x <= 0 ) return v1 ;
  x -- ;
  v1 = d( x / 2 ) ;
  v2 = d( ( x + 1 ) / 2 ) ;
  v1.push_back( ii( x , 1 ) ) ;
  merge( v1 , v2 ) ;
  mx[ x + 1 ] = v1 ;
  return v1 ;
}

void process() {
  v = d( n ) ;

  reverse( v.begin() , v.end() ) ;
  ll lft = 0 ;
  for ( ii x : v ) {
    lft += x.second ;
    if ( lft >= k ) {
      printf( "%lld %lld\n" , ( x.first + 1 ) / 2 , ( x.first / 2 ) ) ;
      return ;
    }
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

