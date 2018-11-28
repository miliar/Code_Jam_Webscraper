#include <bits/stdc++.h>
 
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
 
inline ll pwr(ll base,ll n){ll ans=1;while(n>0){if(n%2==1)ans=(ans*base);base=(base*base);n/=2;}return ans;}
 
struct horse { 
    int d,s;
};

int main() {
    
    fi;
    int t,n,dis;
    cin>>t;
    
    loop(j,t) {
        
        cin>>dis>>n;
        horse h[n];
        
        loop(i,n)
            cin>>h[i].d>>h[i].s;
            
        sort(h,h+n,[](horse h1,horse h2 ) {return h1.d<h2.d;}); 
        long double ts[n];
        if(dis>h[n-1].d)
            ts[n-1] = (long double)( dis - h[n-1].d ) / h[n-1].s;
        else
            ts[n-1] = 0;
        for(int i = n-2;i>=0;i--) {
            if(dis<=h[i].d) {
                ts[i] = 0;
                continue;
            }
            if( h[i+1].s >= h[i].s ) {
                ts[i] = (long double)(dis - h[i].d)/h[i].s;
                continue;    
            }    
            float t2 = (long double)(dis-h[i].d)/h[i].s;
            
            if( t2>=ts[i+1] ) {
                ts[i] = t2;
                continue;
            }
            ts[i] = ts[i+1];
            
        }
        long double ans;
        ans = (long double)dis/ts[0];
        setprecision(7);
        cout<<"Case #"<<fixed<<j+1<<": "<<ans<<"\n";
    }
    return 0;
}