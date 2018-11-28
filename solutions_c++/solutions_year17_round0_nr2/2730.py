#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define ff first
#define ss second
#define MAX  1e6+5;
using namespace std;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t,n;
    cin>>t;
    for(ll i=0;i<t;i++){
        cin>>n;
        vector<ll>v;
        while(n){
            v.pb(n%10);
            n/=10;
        }
        reverse(all(v));
        ll l=v.size();
        ll lc=l;
        for(ll j=l-1;j>0;j--){
            if(v[j-1]>v[j]){
                v[j-1]--;
                lc=j;
            }
        }
        ll ans=0;
        for(ll j=0;j<l;j++){
            ans=ans*10;
            if(j>=lc){
                ans+=9;
            }
            else{
                ans+=v[j];
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }


    return 0;
}

