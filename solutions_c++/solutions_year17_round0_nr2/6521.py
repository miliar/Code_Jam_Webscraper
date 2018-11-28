#include <iostream>
#include <string>
#include <cstring>
using namespace std ;
void solve() ;
int main()
{
  // freopen("input.txt","r",stdin) ;
  //  freopen("output.txt","w",stdout) ;
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
bool legal_pt( string s , int pos){ 
    bool b ;
    if(pos==0 ){
        b = (s[0]!='1') ;
    }
    else{
        b = (s[pos-1]<=s[pos]-1) ;
    }                //     cout<<"legal pt of "<<s<<" at "<<pos<<" is "<<b<<endl ;
    return b ;
}
int break_pt( string s , int last ){
    while( last>=0 ){
        if( legal_pt(s,last) ){
            return last ;
        }
        last-- ;
    }
    return -1 ;
}
void solve(){
    string s ;
    cin >> s ;
    char prev='0' ;
    int target = -1 ;
    for( int i=0 ; i<s.size() ; i++){
        if( s[i]<prev ){
            target = i ;
            break ;
        }
        prev = s[i ] ;
    }                      //   cout<<"target = "<<target ;
    if( target == -1 ){
        cout<<s<<endl ;
        return ;
    }
    int x = break_pt(s,target-1) ;  //   cout<<" break_pt is "<<x<<endl ;
    if( x==-1 ){
        for( int i=1 ; i<int(s.size()) ; i++){
            cout<<9;
        }
    }
    else{
        s[x]--;
        for(int i=0 ; i<=x ; i++){
            cout<<s[i];
        }
        for( int i=x+1 ; i<s.size() ; i++){
            cout<<9;
        }
    }
    cout<<endl ;
}