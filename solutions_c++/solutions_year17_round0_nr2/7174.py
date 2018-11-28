#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <math.h>
 
#define loop(i,n)    for( int i=0; i<n; i++ )
#define loop1(i,a,n) for( int i=a; i<n; i++ )
#define vloop(i,a)   for( vector<int>::iterator i=a.begin(); i!=a.end(); i++ )
#define dloop(i,a)   for( deque<ll>::iterator i=a.begin(); i!=a.end(); i++ )
#define PI 3.14159265
#define bc __builtin_popcountl
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pb push_back
#define pf push_front
#define rf pop_front
#define rb pop_back
#define mp make_pair
#define fs first
#define sc second
#define fi ios_base::sync_with_stdio(false); cin.tie(NULL)
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
const ll M=1e9+7;
const int INF=1e9;
 
inline ll pwr(ll base,ll n){ll ans=1;while(n>0){if(n%2==1)ans=(ans*base)%M;base=(base*base)%M;n/=2;}return ans;}

bool valid( ll n1 ) {
     ll last = n1%10;
     ll n = n1;
     n/=10;
     while(n>0) {
          if(n%10>last)
               return false;
          last = n%10;
          n/=10;
     }
     return true;
}

int main() {
     fi;
     int t;
     cin>>t;
     loop1(i,1,t+1) {
          ll num;
          deque<ll>ans;
          cin>>num;
          
          if( valid(num) ) {
               cout<<"Case #"<<i<<": "<<num<<"\n";
               continue;
          }
          
          while( !valid(num) ) {
               ans.pf(9);
               num/=10;
          }
          if( num>10 && num%10 == (num/10)%10 )
          while( num>10 && num%10 == (num/10)%10 ) {
               ans.pf(9);
               num/=10;
          }     
          if( num - 1 > 0 )
               ans.pf(num-1);
          cout<<"Case #"<<i<<": ";
          dloop(i,ans)cout<<(*i);
          cout<<"\n";
     }
     return 0;
}