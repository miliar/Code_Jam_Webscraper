#include <bits/stdc++.h>
#define H second
#define R first
using namespace std;
typedef long double ld;
pair<ld,ld> P[1007];
const ld INF=1e9+69;
const ld pi=acos(-1);
int n,k;
bool vis[1007][1007];
ld dp[1007][1007];
ld Calc(int X,int remaining){
    if(remaining==k)return 0;

    if(X==n) return -INF;

    if(vis[X][remaining])return dp[X][remaining];

    ld answer=0;

    if(remaining==0) answer=max(answer,pi*P[X].R*P[X].R+P[X].H*2*pi*P[X].R+Calc(X+1,remaining+1));

    else  answer=max(answer,P[X].H*2*pi*P[X].R+Calc(X+1,remaining+1));

    answer=max(answer,Calc(X+1,remaining));

    vis[X][remaining]=1;
    return dp[X][remaining]=answer;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2222.txt","w",stdout);
    int t;cin>>t;
    int G=1;
    while(t--){
        cin>>n>>k;

        memset(vis,0,sizeof vis);

        for(int i=0;i<n;i++)

            cin>>P[i].first>>P[i].second;

        sort(P,P+n);

        reverse(P,P+n);

        cout<<"Case #"<<G++<<": ";

        cout<<fixed<<setprecision(9)<<Calc(0,0)<<endl;
    }
    return 0;
}
