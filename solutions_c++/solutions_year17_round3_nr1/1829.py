#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

ld pi=3.14159265358979323846264338327950;

int n,k,r[1111],h[1111];
pair<ll,ll> p[1111];

ll mem[1111][1111];
ll oo=-1e16;

ll dp(int i,int c){
if(i==n || c==k){
if(c==k)
    return 0;
return oo;
}
if(mem[i][c]!=-1)return mem[i][c];
ll mx=oo;

mx=max(dp(i+1,c+1)+(!c)*p[i].first*p[i].first+2*p[i].first*p[i].second,dp(i+1,c));

return mem[i][c]=mx;
}

bool com(pair<ll,ll> p,pair<ll,ll> pp){
return p.first>pp.first;
}
int main()
{

    freopen("A-large (2).in","rt",stdin);
    freopen("out.txt","wt",stdout);
int t;
cin>>t;
for(int c=1; c<=t; c++){
    cin>>n>>k;
    int a,b;
    for(int i=0; i<n; i++){
        cin>>a>>b;
        p[i]={a,b};
    }
    sort(p,p+n,com);
    memset(mem,-1,sizeof mem);
cout<<"Case #"<<c<<": "<<fixed<<setprecision(8)<<pi*dp(0,0)<<endl;

}
    return 0;
}
