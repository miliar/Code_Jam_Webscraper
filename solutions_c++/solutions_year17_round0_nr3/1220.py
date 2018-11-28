#include<bits/stdc++.h>
using namespace std;
map<long long,long long> m;
set<long long> s;
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,i;
    long long d,e,n,k;
    cin>>t;
    for(i=1;i<=t;++i){
        cin>>n>>k;
        s.clear();
        m.clear();
        s.insert(-n);
        m[n]=1;
        for(;;){
            d=-*s.begin();s.erase(s.begin());
            e=m[d];
            if(e>=k){
                --d;
                printf("Case #%d: %I64d %I64d\n",i,(d+1)/2,d/2);
                break;
            }
            k-=e;
            --d;
            m[d/2]+=e;s.insert(-d/2);
            m[(d+1)/2]+=e;s.insert(-(d+1)/2);
        }
    }
}
