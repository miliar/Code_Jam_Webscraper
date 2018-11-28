#include <bits/stdc++.h>
#define pii pair<long long,long long>
using namespace std;

inline void in(long long &n){scanf("%lld",&n);}

const double PI=atan(1)*4;
long long T,N,K;

bool cmp(pii a,pii b){
    return a.first*a.second>b.first*b.second;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    in(T);
    for(int t=1;t<=T;++t){
        printf("Case #%d: ",t);
        in(N);in(K);
        vector<pii> v;
        for(int i=0;i<N;++i){
            pii x;
            in(x.first);in(x.second);
            v.push_back(x);
        }
        sort(v.begin(),v.end(),cmp);
        long long r=0;
        double s=0,d=0;
        for(int i=0;i<K-1;++i){
            s+=2*PI*v[i].first*v[i].second;
            r=max(r,v[i].first);
        }
        for(int i=K-1;i<N;++i)
            d=max(d,2*PI*v[i].first*v[i].second+PI*max(r,v[i].first)*max(r,v[i].first));
        cout<<fixed;
        cout<<setprecision(7)<<s+d;
        printf("\n");
    }
}
