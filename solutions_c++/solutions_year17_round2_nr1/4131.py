#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define PI 3.14159265359
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<ll,ll> pi;
typedef vector<pi > vpi;

bool comp(pi x,pi y){
    
    return x.ss>y.ss;
    
}
int main() {
    
    ios:: sync_with_stdio(0);
    //cin.tie(NULL),cout.tie(NULL);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++){
        ll d,n,k,s,i;
        cin>>d>>n;
        vpi v(n);
        for(i=0;i<n;i++){
            cin>>k>>s;
            v.pb(mp(s,k));
        }
        sort(v.begin(),v.end(),comp);
        double tm=(d-v[0].ss)*1.0/v[0].ff,curr=0;
        for(i=1;i<n;i++){
            k=v[i].ss;
            s=v[i].ff;
            curr=1.0*(v[i-1].ss-v[i].ss)/(v[i].ff-v[i-1].ff);
            if( curr >0 && curr<tm){
                tm=tm;
            }
            else{
                tm=(d-v[i].ss)*1.0/v[i].ff;
            }
        }
        double ans=d/tm;
        
        
        printf("Case #%d: %.6f\n",t,ans);
        
    }
    
	return 0;
}
