#include<bits/stdc++.h>
#define EPS 1e-10
using namespace std;
typedef long long ll;
typedef long double ld;
vector<pair<int,int>>v;
vector<ll>rh;
ld pi=acosl(-1);
int main(){
    ios_base::sync_with_stdio(0);
    int tc,cc,n,k,i,x,y,j;
    ld d,md;
    cin>>tc;
    for(cc=1;cc<=tc;++cc){
        cin>>n>>k;
        for(i=0;i<n;++i){
            cin>>x>>y;
            v.emplace_back(x,y);
        }
        --k;
        md=0;
        for(i=0;i<n;++i){
            d=pi*v[i].first*v[i].first+2*pi*v[i].first*v[i].second;
            for(j=0;j<n;++j)if(i!=j)rh.push_back(1LL*v[j].first*v[j].second);
            sort(rh.begin(),rh.end(),greater<ll>());
            for(j=0;j<k;++j)d+=2*pi*rh[j];
            rh.clear();
            if(d-md>EPS)md=d;
        }
        cout<<"Case #"<<cc<<": "<<fixed<<setprecision(8)<<md<<'\n';
        v.clear();
    }
    return 0;
}
