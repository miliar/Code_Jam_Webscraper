#include<bits/stdc++.h>
using namespace std ;

int t,x,k,ans;
string s,fir,rep;
map<pair<string,int> ,int > dp,vis;

int foo(string s,int i)
{
    if(s==rep)return(0);
    if(i>x-k)return 1e9;
    if(vis[make_pair(s,i)])return(1e9);
    if(dp[make_pair(s,i)])return(dp[make_pair(s,i)]);
    vis[make_pair(s,i)]=1;
    int c1=foo(s,i+1);
    int c2;
    for(int j=0;j<k;j++)
    {
        if(s[i+j]=='+')s[i+j]='-';
        else s[i+j]='+';
    }
    vis[make_pair(s,i)]=1;
    c2=1+foo(s,0);
    return (dp[make_pair(s,i)]=min(c2,c1));
}
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    cin>>t;
     for(int o=1;o<=t;o++)
    {
        dp.clear();
        vis.clear();
        cin>>s>>k;
        fir=s;
        x=s.size();
        rep="";
        for(int i=0;i<x;i++)
        {
            rep+='+';
        }
        ans=foo(s,0);
        cout<<"Case #"<<o<<": ";
        if(ans==1e9)cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
}
