#include<iostream>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<map>
#include<limits>
#include<cstring>
#include<string>
#include<sstream>
#include<utility>
using namespace std;
typedef long long ll;
pair<ll,ll>solve2(ll n,ll k){
    priority_queue<ll>qu;
    qu.push(n);
    for(ll i=1;i<=k;++i){
        ll t=qu.top();
        qu.pop();
        ll ans1=(t-1)/2,ans2=(t+0)/2;
        if(i==k)
            return make_pair(ans2,ans1);
        qu.push(ans1);
        qu.push(ans2);
    }
    return make_pair(~0u>>1,~0u>>1);
}
pair<ll,ll>solve(ll n,ll k){
    map<ll,ll,greater<ll> >qu;
    qu[n]=1;
    for(ll i=1;i<=k;++i){
        ll t=qu.begin()->first;
        ll c=qu.begin()->second;
        qu.erase(qu.begin());
        ll ans1=(t-1)/2,ans2=(t+0)/2;
        if(k-i+1<=c)
            return make_pair(ans2,ans1);
        i+=c-1;
        qu[ans1]+=c;
        qu[ans2]+=c;
    }
    return make_pair(~0u>>1,~0u>>1);
}
void test(){
    for(int i=1;i<=10000;++i){
        cout<<i<<":"<<endl;
        int n=rand()*rand()%100000+1;
        int k=rand()%n+1;
        auto ans1=solve(n,k);
        auto ans2=solve2(n,k);
        cout<<ans1.first<<" "<<ans1.second<<endl;
        if(ans1!=ans2){
            cout<<"22333\n";
            break;
        }
    }
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //test();
    int T;scanf("%d",&T);
    for(int I=1;I<=T;++I){
        ll n,k;
        cin>>n>>k;
        auto t=solve(n,k);
        cout<<"Case #"<<I<<": "<<t.first<<" "<<t.second<<endl;
    }
    return 0;
}
