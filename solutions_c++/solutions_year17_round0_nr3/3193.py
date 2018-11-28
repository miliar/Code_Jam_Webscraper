#include <iostream>
#include <algorithm>
#include <cmath>

#define ll long long
#define ii pair<ll,ll>
using namespace std;

ii solve (ll n, ll k) {
    if(k==n)
        return ii(0,0);
    ll x,a,b,y,c,d;
    x=n-1;
    a=x/2;
    b=x-a;
    y=k-1;
    c=y/2;
    d=y-c;
    if(k==1)
        return ii(b,a);
    if(k==2)
        return solve(b,1);
    if(x%2==0)
        return solve(b,d);
    else{
        if(y%2==0)
            return solve(a,c);
        else
            return solve(b,d);
    }
}

int main () {
    freopen("C-large.bin","r",stdin);
    freopen("C_large.txt","w",stdout);
    int tc;
    ll x,y;
    ii ans;
    cin>>tc;
    for(int c=1;c<=tc;c++){
        cin>>x>>y;
        ans=solve(x,y);
        cout<<"Case #"<<c<<": "<<ans.first<<" "<<ans.second<<endl;
    }
    return 0;
}