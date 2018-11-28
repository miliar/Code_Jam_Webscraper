#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<ll> sol(ll n,ll k){
    //cout<<n<<' '<<k<<endl;
    ll e=(n-1ll)/2ll,f;
    f=e;
    if(n%2ll==0)f++;
    if(k==1){
        vector<ll> vec;
        vec.push_back(e);
        vec.push_back(f);
        return vec;
    }
    if(k%2ll==1ll){
        return sol(e,k/2ll);
    }
    else{
        return sol(f,k/2ll);
    }
}
int main(){
    ll a,b,c,d,e,f,g,h,k,t,n;
    ios::sync_with_stdio(0);
    //freopen("C-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        cin>>n>>k;
        //cout<<n<<' '<<k<<endl;
        cout<<"Case #"<<ii<<": ";
        vector<ll> vec=sol(n,k);
        cout<<max(vec[0],vec[1])<<' '<<min(vec[0],vec[1])<<endl;
    }
    return 0;
}
