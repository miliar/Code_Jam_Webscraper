#include<bits/stdc++.h>
using namespace std;
#define inc(i,x) for(int i=0;i<x;i++)
#define onc(i,x) for(int i=1;i<=x;i++)
typedef long long ll;

void solve(ll a,ll na,ll nb,ll k)
{
    if(na+nb>=k){
        ll blk;
        if(k<=nb){
            blk=a+1;
        }
        else{
            blk=a;
        }
        ll mn=(blk-1)/2;
        ll mx=blk-1-mn;
        cout<<mx<<" "<<mn<<"\n";
        return;
    }
    ll aa=0;
    ll bb=0;
    if(a%2==1){
        aa += na*2;
        aa += nb;
        bb += nb;
    }
    else{
        aa += na;
        bb += na;
        bb += nb*2;
    }
    solve((a-1)/2,aa,bb,k-na-nb);
}

main()
{
    int t;
    cin>>t;
    onc(kase,t){
        ll n,k;
        cin>>n>>k;
        cout<<"Case #"<<kase<<": ";
        solve(n,1,0,k);
    }
}
