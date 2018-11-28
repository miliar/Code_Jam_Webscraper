#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
//#define INF (1e9+1)
#define INF (1LL<<59)

#define int ll

signed main(){
    int T;
    cin>>T;
    rep(t,T){
        int d,n;
        cin>>d>>n;
        double ans = 0;
        rep(i,n){
            int k,s;
            cin>>k>>s;
            ans = max(ans,(double)(d-k)/s);
        }
        cout<<"Case #"<<t+1<<": ";
        printf("%.20lf\n",d/ans);
    }
}