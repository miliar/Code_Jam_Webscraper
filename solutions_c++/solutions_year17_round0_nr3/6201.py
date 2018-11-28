#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <stack>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cassert>
#include <cmath>
#include <math.h>
using namespace std;

typedef long long ll;

void solve(ll n,ll cur,ll final,map<ll,ll> &m){
    if(cur==final){
        map<ll,ll>::iterator it;
        it=m.find(n);
        if(it!=m.end())
            m[n]+=1;
        else
            m.insert(make_pair(n,1));
        return;
    }
    ll p1,p2;
    if(n%2==0){
        p1=n/2-1;
        p2=n/2;
    }
    else{
        p1=n/2;
        p2=n/2;
    }
    solve(p1,cur+1,final,m);
    solve(p2,cur+1,final,m);
}

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;

    for(int ii=1;ii<=t;ii++){
        ll n,k;
        cin>>n>>k;
        if(n==k){
            cout<<"Case #"<<ii<<": "<<"0 0"<<endl;
            continue;
        }
        map<ll,ll> m;
        ll res=log((double) k)/log(2.0);
        ll var=pow(2,(double) res) - 1;
        var=k-var;
        solve(n,0,res,m);
        map<ll,ll>::reverse_iterator it;
        ll ans=0;
        for(it=m.rbegin();it!=m.rend();++it){
            ll x=it->second;
            if(var<=x){
                ans=it->first;
                break;
            }
            var-=x;
        }
        ll l,r;
        if(ans%2==0)
            l=ans/2-1;
        else
            l=ans/2;
        r=ans/2;
        if(l<r)
            swap(l,r);
        cout<<"Case #"<<ii<<": "<<l<<" "<<r<<endl;



    }
    return 0;
}