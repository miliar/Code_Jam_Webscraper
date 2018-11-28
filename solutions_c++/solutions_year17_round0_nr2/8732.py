#include <bits/stdc++.h>

using namespace std;
#define ll unsigned long long
int k;
set<ll>S;
set<ll> :: iterator it;
vector<ll>vv;
void fnc(int n, ll sum,int last){
    if(n==19)return;
    k++;
    if(sum!=0)vv.push_back(sum);
    //if(last==0)
    for(int i=last; i<=9; i++){
        fnc(n+1,sum*10+i, i);
    }

}

int bin(int l, int h, ll v){
    int ret=-1;
    while(l<=h){
        int mid=(l+h)/2;
        if(vv[mid]<=v){
            ret=mid;
            l=mid+1;
        }else h=mid-1;
    }
    return ret;

}

int main(){

    fnc(0,0,1);
    //cout<<k<<endl;
    sort(vv.begin(),vv.end());
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    int t;
    scanf("%d", &t);

    for(int cs=1; cs<=t; cs++){
        ll x;
        scanf("%llu",&x);
        int ans=bin(0,vv.size()-1,x);
       printf("Case #%d: %llu\n",cs, vv[ans]);
    }
}
