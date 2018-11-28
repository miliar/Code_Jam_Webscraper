#include<bits/stdc++.h>
using namespace std;
#define ll long long int

ll dp[20][2][10],pw[20];
int ln;
string s;

ll go(int pos,int f,int pre)
{
    if(pos>=ln) return 0LL;
    if(dp[pos][f][pre]!=-1) return dp[pos][f][pre];
    ll val=-100;
    int e=9;
    if(f) e=s[pos]-'0';
    for(int i=0;i<e;i++)
        if(i>=pre)
        {
            ll ans=go(pos+1,0,i);
            if(ans>=0)
             val=max(val,pw[ln-pos-1]*(ll)i+ans);
        }
        if(e>=pre)
         {
             ll ans=go(pos+1,f,e);
             if(ans>=0)
             val=max(val,pw[ln-pos-1]*(ll)e+ans);
         }
    return dp[pos][f][pre]=val;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    pw[0]=1LL;
    for(int i=1;i<20;i++)
        pw[i]=pw[i-1]*(ll)10;

    int t,ts;
    cin>>ts;
    for(int t=1;t<=ts;t++)
    {
        cin>>s;
        ln=s.size();
        for(int i=0;i<=ln;i++)for(int j=0;j<2;j++)for(int k=0;k<10;k++) dp[i][j][k]=-1;
        printf("Case #%d: %lld\n",t,go(0,1,0));
    }
}
