#include <bits/stdc++.h>
#define H second
#define R first
using namespace std;
typedef long double ld;
pair<ld,ld> P[1007];
const long double inf=1e9+69;
const long double pi=acos(-1);
int n,k;
bool ok[1007][1007];
ld dp[1007][1007];
long double solve(int id,int tk){
    if(tk==k)return 0;
    if(id==n) return -inf;
    if(ok[id][tk])return dp[id][tk];
    long double res=0;
    if(tk==0) res=max(res,pi*P[id].R*P[id].R+P[id].H*2*pi*P[id].R+solve(id+1,tk+1));
    else  res=max(res,P[id].H*2*pi*P[id].R+solve(id+1,tk+1));
    res=max(res,solve(id+1,tk));
    ok[id][tk]=1;
    return dp[id][tk]=res;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;cin>>t;
    int cs=1;
    while(t--){
        cin>>n>>k;
        memset(ok,0,sizeof ok);
        for(int i=0;i<n;i++)cin>>P[i].first>>P[i].second;
        sort(P,P+n);
        reverse(P,P+n);
        cout<<"Case #"<<cs++<<": ";
        cout<<fixed<<setprecision(9)<<solve(0,0)<<endl;
    }
    return 0;
}
