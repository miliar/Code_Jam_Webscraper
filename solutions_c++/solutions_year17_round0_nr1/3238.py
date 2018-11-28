#include<bits/stdc++.h>
using namespace std;
#define loop(i,L,R) for(int i=(L);i<=(R);i++)
#define rept(i,L,R) for(int i=(L);i<(R);i++)
#define isc(n) scanf("%d",&n)
#define llsc(n) scanf("%lld",&n)
#define dsc(n) scanf("%lf",&n)
#define enl cout<<endl
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>PI;
typedef pair<pair<int,int>,int>PII;
map<string,bool>vis;
map<string,int>dp;
string en;
int l,d;
int rec(string p)
{
    if(p==en)return 0;
    if(vis[p] && dp[p]<=0)return dp[p]=-1;
    else if(vis[p])return dp[p];
    vis[p]=true;
    dp[p]=-1;
    rept(i,0,l-d+1)
    {
        string temp=p;
        rept(j,i,i+d)
        {
            if(temp[j]=='-')temp[j]='+';
            else temp[j]='-';
        }
        int ans=rec(temp);
        if(ans>=0)
        {
            if(dp[p]<0)dp[p]=ans+1;
            else dp[p]=min(dp[p],ans+1);
        }
    }
    return dp[p];
}
int main()
{
    freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);
    int t,cas=0;
    isc(t);
    while(t--)
    {
        string in;
        cin>>in>>d;
        vis.clear();
        dp.clear();
        en="";
        l=in.size();
        rept(i,0,l)
        {
            en+='+';
        }
        int ans=rec(in);
        if(ans<0)cout<<"Case #"<<++cas<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    return 0;
}
