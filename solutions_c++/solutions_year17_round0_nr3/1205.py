#include<bits/stdc++.h>
#define ll long long
using namespace std;
pair<ll,ll> do_it(ll l,ll h,ll v){
ll mid=(l+h)>>1;
if(v==1){
   return pair<ll,ll> (max(mid-l,h-mid)-1,min(mid-l,h-mid)-1);
}  
if(v%2==0){
return do_it(mid,h,v/2);
}else{
    return do_it(l,mid,v/2);
}

}
int main(){
    ll t,i=1;
    cin>>t;
    while(t--){
        ll x,y;
        cin>>x>>y;
        pair<ll,ll> p=do_it(0,x+1,y);
        cout<<"Case #"<<i++<<": "<<p.first<<" "<<p.second<<endl;
    }
return 0;
}

