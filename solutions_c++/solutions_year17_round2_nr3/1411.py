#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 105;

typedef long long ll;

int t , n , trash;
ll maxi[MAX_N] , speed[MAX_N] , dist[MAX_N];
double memo[MAX_N][MAX_N];

double dp ( int sta , int horse ) {

  double &curr = memo[sta][horse];

  if ( curr != -1.0 ) return curr;
  if ( sta == n ) return 0.0;
  curr = DBL_MAX;

  int currDist = dist[sta] - dist[horse];
  if ( horse and dist[sta+1] - dist[sta] + currDist <= maxi[horse] )
    curr = ( dist[sta+1] - dist[sta] ) / double ( speed[horse] ) + dp ( sta+1 , horse );

  curr = min ( curr , ( dist[sta+1] - dist[sta] ) / double ( speed[sta] ) + dp ( sta+1 , sta ) );

  return curr;

}

int main()  {

  freopen ( "C-small-attempt0.in" , "r" , stdin );
  freopen ( "out.txt" , "w" , stdout );

  scanf ( "%d" , &t );
  for ( int it = 0 ; it < t ; it++ ) {

    scanf ( "%d%d" , &n , &trash );
    for ( int i = 1 ; i <= n ; i++ )
      scanf ( "%d%d" , maxi + i , speed + i );

    for ( int i = 0 ; i <= n ; i++ )
      for ( int h = 0 ; h <= n ; h++ )
        memo[i][h] = -1.0;

    for ( int i = 1 ; i <= n ; i++ ) {
      for ( int h = 0 ; h < n ; h++ ) {
        scanf ( "%d" , &trash );
        if ( trash == -1 )
          continue;
        dist[i+1] = dist[i] + trash;
      }
    }

    scanf ( "%d%d\n" ,  &trash , &trash );

    printf ( "Case #%d: %.10f\n" , it+1 , dp ( 1 , 0 ) );


  }

  return 0;

}
