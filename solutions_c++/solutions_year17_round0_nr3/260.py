#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define X first
#define Y second

const int N=1e3+10;

map<ll,ll> ma;
ll n,k;
void solve(){
    ma.clear();
    ma[n]=1;
    k--;
    while (k){
        ll pos=ma.rbegin()->X;
        ll val=min(ma[pos],k);
//        cout<<pos<<" "<<val<<'\n';
        k-=val;
        if (val==ma[pos]) ma.erase(pos);
        else ma[pos]-=val;
        ma[pos/2]=min(k+1,ma[pos/2]+val);
        ma[(pos-1)/2]=min(k+1,ma[(pos-1)/2]+val);
    }
//    for(auto i:ma) cout<<i.X<<"-"<<i.Y<<'\n';
    ll pos=ma.rbegin()->X;
    cout<<pos/2<<" "<<(pos-1)/2<<'\n';
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        cin>>n>>k;
        cout<<"Case #"<<te<<": ";
        solve();
    }
}
