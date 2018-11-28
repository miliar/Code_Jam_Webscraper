#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <vector>
using namespace std;
void solve() ;
int t ;
int main(){
  //  freopen( "input.txt" , "r" , stdin ) ;
  //  freopen( "output.txt" , "w" , stdout ) ;
    t=1 ;
    cin >>t ;
    for(int i=1 ; i<=t ; i++){
        cout<<"Case #"<<i<<": "; 
        solve() ;
    }
    return 0 ;
}
void solve(){
    long long int d , n ; 
    cin >> d >> n ;
    double tmin=0;
    for( int i=0 ; i<n ; i++){
        int k ,  s ;
        cin >>k >> s ;
        tmin = max((d-k)/(1.0*s) , tmin) ;
    }
    printf("%.6f\n",d/tmin);
}
