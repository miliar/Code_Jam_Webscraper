#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t , l = 1 ;
    freopen( "input.txt","r",stdin);
    freopen("outputt.txt","w",stdout);

    scanf("%d",&t);
    while ( t-- ) {
      int n , k ;
      scanf("%d %d",&n,&k);
      priority_queue < pair < int , pair < int , int > >  > q ;
      q.push( make_pair( n  , make_pair( 0, n + 1  )) ) ;
      int in = 0 ,mn = 0 , mx = 0  ;
      for( int i = 1 ; i <= k ; i ++ ){
        pair < int , pair < int , int > > p = q.top();
        in = p.second .first + ( (  p.second.second - p.second.first  )  / 2 ) ;
        q.pop();
        int x = p.second.first ;
        int y = p.second.second ;
        q.push ( make_pair( in - x  , make_pair( x , in )) );
        q.push ( make_pair( y  - in   , make_pair( in , y )) );
        if ( i == k ){
         int a = in - x - 1  ;
         int b = y  - in - 1   ;
         mn = min( a, b );
         mx = max( a , b );
         //cout << in << endl;

        }

      }
      printf("Case #%d: %d %d\n",l++,mx,mn);




    }

    return 0;
}
