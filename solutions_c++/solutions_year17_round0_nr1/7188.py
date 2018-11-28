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


int main() {
     
     fi;
     int t;
     cin>>t;
     
     loop1(i,1,t+1) {
          
          char s[1005];
          int k,cnt = 0;
          cin>>s>>k;
          int sz = strlen(s);
          
          loop(i,sz) {
               
               while( s[i]=='+'&& i<sz ) i++;
               
               if(i+k-1<sz) {
                    cnt++;
                    loop(j,k) {
                         if(s[i+j]=='-')
                              s[i+j] = '+';
                         else 
                              s[i+j] = '-';
                    }
               }
               
               else 
                    break;
          }
          
          bool possible = true;
          
          loop(i,sz) {
               if(s[i]=='-') {
                    possible = false;
                    break;
               }     
          }
          
          if(!possible)
               cout<<"Case #"<<i<<": IMPOSSIBLE\n";
          else
               cout<<"Case #"<<i<<": "<<cnt<<"\n";
     }
     return 0;
}