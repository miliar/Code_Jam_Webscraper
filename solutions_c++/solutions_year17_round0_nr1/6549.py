#include <iostream>
#include <string>
#include <cstring>
using namespace std ;
void solve() ;
int main()
{
  // freopen("input.txt","r",stdin) ;
    //freopen("output.txt","w",stdout) ;
    int t ;
    cin >> t ;
    int x=1 ;
    while( t-- ){
        cout<<"Case #"<<x<<": ";
        x++ ;
        solve() ;
    }
    return 0;
}
void solve(){
    string s ;
    int k ;
    cin >> s >> k ;
    int cnt = 0 ;
    for ( int i=0 ; i<=int(s.size())-k ; i++){
        if( s[i]=='-' ){
            for( int j=0 ; j<k ; j++){
                if( s[i+j]=='-' ){
                    s[i+j] = '+' ;
                }
                else{
                    s[i+j] = '-' ;
                }
            }
            cnt++ ;
        }
    }
    bool flag = true ;
    for( int i=0 ; i<int(s.size()) ; i++){
        if( s[i]=='-' ){
            cout<<"IMPOSSIBLE"<<endl;
            return ;
        }
    }
    cout<<cnt<<endl ;
}