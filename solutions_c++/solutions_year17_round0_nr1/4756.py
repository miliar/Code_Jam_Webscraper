#include<bits/stdc++.h>

using namespace std ;

int main(int argc, char const *argv[])
{

    int t , l = 1 ;
    freopen( "input.txt","r",stdin);
   freopen("outputt.txt","w",stdout);
    scanf("%d",&t);
    while ( t -- ){
         string str , ans;
         int n , ct = 0 , ko = 0 ;
         cin >> str ;
         scanf("%d",&n);
         int ln = str.size() ;
         ans = str ;
         while ( 1 ){
          int cnt = 0 , st = 0  , ok = 0 ;
             int in = 0 ;
             for( int i = 0 ; i < ln ; i ++ ){
              if ( str[ i ] =='-'){
                in = i ;
                ok = 1 ; break ;
              }
             }
             if ( ok == 0 ) break ;

              if ( in + n > ln ) {
             ko = 1 ;
             break;
             }


             for ( int i = in ; i < in + n ; i ++ ){
                  if ( str[ i ] =='+' ) str[ i ] = '-';
                  else str[ i ] = '+';
             }
             ct ++ ;
            // cout << str << endl;

         }
         if ( ko == 1  ) {
         printf("Case #%d: IMPOSSIBLE\n",l++);
         //cout << ans  <<" " << n <<  endl;
         }
         else  {
          printf("Case #%d: %d\n",l++,ct);
          //cout << ans << " " << n <<  endl;
         }





    }
    return 0;
}

