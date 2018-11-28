#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{

    int t , l = 1 ;
   freopen( "input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while ( t -- ){
         ll n , check = 0 ,ans = 0 ;
         scanf("%lld",&n);
         string str , ok ;
         ll p = n ;
         while ( true ) {
         check = 0 ;
         str.clear();
         ok.clear();
         while ( p ){
          int mod = p % 10 ;
          p /= 10 ;
          str += mod +'0' ;
         }
         reverse(str.begin() , str.end());
        // cout << str << endl;

         for( int i = 0 ; i < str.size() - 1 ; i ++ ){
         if ( str[ i + 1 ] < str[ i ]){
         check = 1 ;
         break ;
         }
         }
         if ( check == 0 ) {
         if ( ans == 0)ans = n ;
         break ;}
         str +='0';
         for( int i = 0 ;  i < str.size() - 1  ; i ++ ){
               if ( str [ i + 1 ] < str[ i ]){
               ok += str[ i ];
               break;
               }else ok += str[ i ];
         }
         int ln= str.size() - 1 - ok.size();
         for( int i = 0 ; i < ln ; i ++ ){
            ok +='0';
         }
          ll num = 0 ;
          stringstream ss ( ok );
          ss >> num ;

          //cout << num << endl;

          if ( ln != 0 )ans = num - 1 ;
          else ans = num ;
          p = ans ;
          }

          printf("Case #%d: %lld\n",l++,ans);





    }
}
