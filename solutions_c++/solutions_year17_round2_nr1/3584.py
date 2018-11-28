#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // ONLINE_JUDGE

int t;
cin>>t;
for(int i=1;i<=t;i++){
    ll n,d;
    cin>>d>>n;
    vector<pair<ll,ll> > v;
    v.resize(n);
    for(int i=0;i<n;i++) cin>>v[i].first>>v[i].second;
    sort(v.begin(),v.end());
    long double time=0.0;
    for(ll i=n-1;i>=0;i--){
        double temp_time;
        temp_time=(1.0)*(d-v[i].first)/(v[i].second*1.0);
        if(time==0.0) time=temp_time;
        else if(temp_time<=time) continue;
        else time=temp_time;
    }
    double ans=d/time;
    cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<ans<<endl;
}
}
