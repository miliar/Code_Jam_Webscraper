#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
vector<ll> si,ki;
ll n,d, t;
bool can ( double v){
for(ll i=0;i<n;i++){
//if(t==38)
//printf(" horse no %lld need %.6f to finish and I need %.6f  vitesse %.6f\n ",(((d-ki[i])*1.0)/si[i]*1.0),((d*1.0)/v),v);
    if(((d*1.0)/v)<(((d-ki[i])*1.0)/(si[i]*1.0))){
    return false;
    }
}
return true;
}
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.out","w",stdout);
    ll T;
    cin>>T;
    for( t=0;t<T;t++){

    cin>>d>>n;
    //if(t==38)
    //cout<<" n "<<n<<"d "<<d <<endl;
    si.clear();
    ki.clear();
    si.resize(n);
    ki.resize(n);
    for(ll i=0;i<n;i++){

    cin>>ki[i]>>si[i];
  //  if(t==38)
    //cout<<" ki "<<ki[i]<<" si "<<si[i]<<endl;
    }
    ///finished reading input
    ///time to finish horse 1
     double lo = 0.0, hi =1e18, mid = 0.0, ans = 0.0;
    for (int i = 0; i < 1000; i++) {
    mid = (lo + hi) / 2.0;
    if (can(mid)) { ans = mid; lo=mid; }
    else
    hi = mid;
    }
    // if(t==38)
    printf("Case #%lld: %.6lf\n",t+1,ans);
    }
    return 0;
}
