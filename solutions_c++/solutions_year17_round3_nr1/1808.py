#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <vector>
using namespace std;
double pi = 3.141592653589793238;
void solve() ;
int t ;
int main(){
//  freopen( "input.txt" , "r" , stdin ) ;
  //  freopen( "output.txt" , "w" , stdout ) ;
    cin >>t ;
    for(int i=1 ; i<=t ; i++){
        cout<<"Case #"<<i<<": "; 
        solve() ;
    }
    return 0 ;
}
bool ktimes( int i , int k ){
    if( i==0 and k==0 ){
        return true ;
    }
    else if( (i==0 and k>0) or (i>0 and k==0) ){
        return false ;
    }
    if( i%2==0 ){
        return ktimes(i/2,k) ;
    }
    else{
        return ktimes(i/2,k-1) ;
    }
}
bool cmp ( pair< double , double > p1 , pair< double , double > p2 ){
    return p1.first >= p2.first ;
}
double find_ans( vector< pair< double , double > > v , double r , double h ){
    int n = v.size() ;
    if(n>0 and  r>=v[0].first ){
        double rr=v[0].first , hh = v[0].second ;
        return (2*pi*r*h)+(pi*r*r-pi*rr*rr) ;
    }
    else if( n==0 ){
        return (2*pi*r*h)+(pi*r*r) ;
    }
    else {
        return (2*pi*r*h) ;
    }
}
void solve(){
    int n , k ;
    cin >> n >> k ;
    vector< pair<double , double>  > v(n) ; 
    for( int i=0 ; i<n ; i++){
        cin >> v[i].first >> v[i].second ; 
    }   
   vector< bool > check(n , false ) ;
    vector< pair< double , double > > ans_set ;   
   while( k-- ){ 
        double maxm=-1 , pos =0 ;
        sort( ans_set.begin() , ans_set.end()  ) ;
   reverse( ans_set.begin() , ans_set.end()  ) ;
       for( int i=0 ; i<n ; i++){
           if( check[i]==false ){
                double curr = find_ans( ans_set , v[i].first , v[i].second ) ;  // cout<<" for i= "<<v[i].first<<" and " <<v[i].second<<" curr = "<<curr<<endl ;
                if( curr > maxm ){
                    maxm = curr ;
                    pos = i ;
                }
          }
        }
       check[pos] = true ;
        ans_set.push_back( v[pos] ) ; //  cout<<" inserted "<<v[pos].first<<" , "<<v[pos].second <<endl ;
    }     //   cout<<" hai " ;
   double ans=0 ;
   sort( ans_set.begin() , ans_set.end()  ) ;
   reverse( ans_set.begin() , ans_set.end()  ) ;
   for( int i=0 ; i<ans_set.size()-1 ; i++){
        double r = ans_set[i].first , h = ans_set[i].second , rn=ans_set[i+1].first ;
       // cout<<" r = "<<r<<" h = "<<h <<" rn = "<<rn<<endl ;
        ans +=( (2*pi*r*h) + (  (pi * r * r) - ( pi * rn * rn ) ) );
    }
    double r = ans_set[ans_set.size()-1].first , h = ans_set[ans_set.size()-1].second ;
    //cout<<" r = "<<r<<" h = "<<h<<endl ;
    double xx =( ( 2 * r * h ) + (  r * r ) ) ;  // cout<<xx<<endl ;
    ans += ( xx * pi ) ;
    printf("%.9f\n" , ans ) ;
}