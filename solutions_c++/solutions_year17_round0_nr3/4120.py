#include <vector>
#include <string.h>
#include<iostream>
#include<set>
#include<map>
#include<unordered_map>
#include<string.h>
#include<algorithm>
#include <stdlib.h>
#include<queue>
using namespace std;


typedef long long ll;
const ll mod=1e9+7;
#define out_vector(v) for(auto a:v)cout<<a<<" "; cout<<endl;
typedef long long num;

struct less_than_key{
    inline bool operator() (const pair<int,int>& p1, const pair<int,int>& p2){
        return (p1.first==p2.first?p1.second<p2.second:p1.first > p2.first);
    }
};

ll po(ll b,ll d){
    if(d==0){
        return 1;
    }
    return b*po(b,d-1);
}

pair<ll,ll> divide(ll n){
    ll left=n/2,right=n/2;
    if(n%2==0){
        left--;
    }
    return make_pair(left,right);
}

int main(){
    freopen("/Users/shitian/Downloads/C-large.in", "r", stdin);
    freopen("/Users/shitian/Downloads/C-large.txt", "w", stdout);
    int tcase;
    cin>>tcase;
    for(int tc=1;tc<=tcase;tc++){
        cout<<"Case #"<<tc<<": ";
        
        ll n,k;
        cin>>n>>k;
        map<ll,ll>ma;
        ma.clear();
        ma[n]++;
        while(k){
            auto r =ma.rbegin();
            ll t=r->first,count=r->second;
            pair<ll,ll>left=divide(t);
            k-=count;
            ma.erase(t);
            //cout<<r->second<<endl;
            if(k<=0){
                cout<<left.second<<" "<<left.first<<endl;
                break;
            } else {
                ma[left.first]+=count;
                ma[left.second]+=count;
            }
        }
    }
    return 0;
}
