#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define ff first
#define ss second
#define MAX  1e6+5;
using namespace std;

ll rec(ll c,ll q,map<ll,ll>m){
    map<ll,ll>::iterator it=m.end();
    map<ll,ll>z;
    ll a,b,d;
    do{
        it--;
        c+=it->second;
        if(c>=q){
            return it->first;
        }
        d=it->first;
        d--;
        a=b=d/2;
        if(d%2)
            a++;
        z[a]+=it->second;
        z[b]+=it->second;
    }while(it!=m.begin());
    return rec(c,q,z);
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t,k,n;
    cin>>t;
    for(ll i=0;i<t;i++){
        cin>>n>>k;
        map<ll,ll>m;
        m[n]=1;
        ll ans=rec(0,k,m);
        ans--;
        ll a,b;
        a=b=ans/2;
        if(ans%2)
            a++;
        cout<<"Case #"<<i+1<<": "<<a<<" "<<b<<endl;
    }


    return 0;
}

