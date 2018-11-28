#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
pair<ll,ll> solve(ll lo,ll hi,ll k){
    while(1)
    {
    ll mid=(lo+hi)>>1;
    if(k==1) {
        ll l=mid-lo-1;
        ll r=hi-mid-1;
        return make_pair(max(l,r),min(l,r));
    }
    if(k%2==0)
        {lo=mid;
        }
    else hi=mid;
    k/=2;
    }
}
int main(){
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        ll n,k;
        cin>>n>>k;
        pair<ll,ll> ans=solve(0,n+1,k);
        cout<<"Case #"<<i<<": "<<ans.first<<" "<<ans.second<<endl;
    }


}
