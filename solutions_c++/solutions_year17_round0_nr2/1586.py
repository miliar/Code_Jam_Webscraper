#include <bits/stdc++.h>

using namespace std;

long long dp[20][2][10],pwr[19];
string s;

long long bt(int i, bool g,int pre)
{
    if(i>=s.size())
        return 0;
    if(dp[i][g][pre]!=-1)
        return dp[i][g][pre];
    long long p=pwr[s.size()-i-1];
    long long ans=-1e18;
    for(int f=pre;f<=s[i]-'0'||f<=9&&g;f++)
    {
        ans=max(ans,f*p+bt(i+1,g||s[i]-'0'!=f,f));
    }
    return dp[i][g][pre]=ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    pwr[0]=1;
    for(int f=1;f<19;f++)
        pwr[f]=pwr[f-1]*10;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s;
        memset(dp,-1,sizeof dp);
        cout<<"Case #"<<tc<<": ";
        cout<<bt(0,0,0)<<endl;
    }
}
